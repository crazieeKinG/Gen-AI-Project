from pydantic import BaseModel, Field


class LanguageTranslationResponse(BaseModel):
    """Format the response of the language translation template"""

    text: str = Field(
        description="The provided text. The text section of the response.",
    )
    response: str = Field(
        description="The translated response. The result section of the response.",
    )
    source_lang: str = Field(
        description="The source language of the text. The source_lang section of the response.",
    )
    target_lang: str = Field(
        description="The target language of the text. The target_lang section of the response.",
    )
    created_at: str = Field(description="The created time stamp of responses on utc")


class LanguageTranslationBody(BaseModel):
    """Format the request body of the language translation template"""

    text: str = "Hi"
    target_language: str = "en"
