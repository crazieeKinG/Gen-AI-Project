from pydantic import BaseModel, Field
from typing import Optional, List


class AppUserGuideResponse(BaseModel):
    """Format the response of the app user guide template"""

    query: str = Field(
        description="The provided query",
    )
    ref: str = Field(description="The responses of Ref section ")
    response: str = Field(
        description="The response of the app user guide template of 'Response' section. Do not provide raw data, organize different section in paragraph and format the repsonse in conversational tone for each section in response if needed else use a single paragraph to convey the response.",
    )
    source: Optional[str] = Field(
        description="The source of the app user guide template responses only if it is relevant. Set source empty if no information found."
    )
    translated_response: Optional[dict] = None


class ChatLogs(BaseModel):
    """Chat Logs base model"""

    type: str
    message: str


class AppUserGuideBody(BaseModel):
    """Format the request body of the app user guide template"""

    query: str = "Hi"
    chat_logs: List[ChatLogs] = []
    target_language: str = "en"
