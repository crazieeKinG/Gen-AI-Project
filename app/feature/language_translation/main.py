from app.core.constants.routes import LANGUAGE_TRANSLATE_ROUTES
from app.data.usecase.language_translation_invoker.main import translate_invoker
from app.core.services.logger.main import logger
from app.domain.language_translation.main import LanguageTranslationBody

from fastapi import APIRouter


router = APIRouter(
    prefix=LANGUAGE_TRANSLATE_ROUTES["prefix"], tags=LANGUAGE_TRANSLATE_ROUTES["tags"]
)


@router.post("/")
def translate_response(body: LanguageTranslationBody):
    """
    Language translation endpoint
    """
    logger.info(
        "=== Generating response for text: %s, target language: %s ===",
        body.text,
        body.target_language,
    )
    response = translate_invoker.invoke(
        {"text": body.text, "target_language": body.target_language}
    )

    logger.info(
        "=== Response generated successfully for text: %s, target language: %s ===",
        body.text,
        body.target_language,
    )

    return response.dict()
