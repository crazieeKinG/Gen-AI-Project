from app.data.datasource.app_user_guide_rag.main import pdf_retriever
from app.core.services.open_ai.main import llm
from app.core.constants.app_user_guide import (
    pdf_document_prompt,
    chat_history_aware_prompt,
)
from app.domain.app_user_guide.main import AppUserGuideResponse, ChatLogs
from app.core.services.logger.main import logger
from app.feature.language_translation.main import translate_invoker

import json
from typing import List
from langchain.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser

logger.info("=== App User Guide: Initializing structured LLM and prompt template ===")

# Structured LLM & Agent
structured_llm = llm.with_structured_output(AppUserGuideResponse)

# Prompt template
pdf_template = ChatPromptTemplate.from_template(pdf_document_prompt)


def format_query_with_chatlogs(query: str, chat_logs: List[ChatLogs]):
    """
    Format the query with chat logs and return a list of messages.

    For AI Message and User Message
    """
    formatted_query = []

    # Add the PDF document prompt as the first message
    formatted_query.append(SystemMessage(content=chat_history_aware_prompt))

    # Add the chat logs as messages
    for chat_log in chat_logs:
        if chat_log.type == "user":
            formatted_query.append(HumanMessage(content=chat_log.message))
        elif chat_log.type == "assistant":
            formatted_query.append(AIMessage(content=chat_log.message))

    # Add the query as the last message
    formatted_query.append(HumanMessage(content=query))

    return formatted_query


def pdf_rag_invoker(query: str, target_lang: str, chat_logs: List[ChatLogs] = []):
    """
    Function to invoke the PDF retrieval and response generation process.

    Also, translate the response to the target language.
    """
    prompt_with_logs = format_query_with_chatlogs(query, chat_logs)

    # Prompt template
    chat_history_template = ChatPromptTemplate(prompt_with_logs)

    # Runnables
    chat_history_invoker = (
        {"input": RunnablePassthrough()}
        | chat_history_template
        | llm
        | StrOutputParser()
    )

    rag_invoker = (
        {
            "pdf_context": pdf_retriever,
            "query": chat_history_invoker,
        }
        | pdf_template
        | structured_llm
    )

    rag_response = rag_invoker.invoke(query)

    translate_response = translate_invoker.invoke(
        {"text": json.dumps(rag_response.dict()), "target_language": target_lang}
    )

    if translate_response.source_lang != translate_response.target_lang:
        rag_response.translated_response = json.loads(translate_response.response)

    return rag_response


logger.info("=== App User Guide PDF rag invoker initialized successfully ===")
