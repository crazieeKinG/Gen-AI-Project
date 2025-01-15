from pydantic import BaseModel, Field
from typing import Optional


class AppUserGuideResponse(BaseModel):
    """Format the response of the app user guide template"""

    query: str = Field(
        description="The provided query",
    )
    ref: str = Field(description="The responses of Ref section ")
    response: str = Field(
        description="The response of the app user guide template of 'Response' section. Format the repsonse in conversational tone and structed way. for each section in response",
    )
    source: Optional[str] = Field(
        description="The source of the app user guide template responses only if it is relevant"
    )
    created_at: str = Field(description="The created time stamp of responses on utc")
