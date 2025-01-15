from app.core.constants.routes import APP_USER_GUIDE_ROUTES
from app.data.usecase.app_user_guide_rag_invoker.main import pdf_rag_invoker
from app.core.services.logger.main import logger

from fastapi import APIRouter


router = APIRouter(
    prefix=APP_USER_GUIDE_ROUTES["prefix"], tags=APP_USER_GUIDE_ROUTES["tags"]
)


@router.get("/")
def generate_response(query: str = "Hi"):
    logger.info("=== Generating response for query: %s ===", query)
    response = pdf_rag_invoker.invoke(query)

    logger.info("=== Response generated successfully for query: %s ===", query)

    return response.dict()
