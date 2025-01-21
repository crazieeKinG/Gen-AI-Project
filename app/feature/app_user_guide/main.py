from app.core.constants.routes import APP_USER_GUIDE_ROUTES
from app.data.usecase.app_user_guide_rag_invoker.main import pdf_rag_invoker
from app.core.services.logger.main import logger
from app.domain.app_user_guide.main import AppUserGuideBody

from fastapi import APIRouter


router = APIRouter(
    prefix=APP_USER_GUIDE_ROUTES["prefix"], tags=APP_USER_GUIDE_ROUTES["tags"]
)


@router.post("/")
def generate_response(body: AppUserGuideBody):
    logger.info(
        "=== Generating response for query: %s, target language: %s ===",
        body.query,
        body.target_language,
    )
    response = pdf_rag_invoker(body.query, body.target_language)

    logger.info(
        "=== Response generated successfully for query: %s, target language: %s ===",
        body.query,
        body.target_language,
    )

    return response.dict()
