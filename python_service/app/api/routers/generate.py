import logging

from app.api.schemas.generate_schema import GenerateResponse, PromptRequest
from app.api.utils import call_openai_api, reverse_string
from app.core.config import settings
from fastapi import APIRouter, HTTPException, status
from openai._exceptions import (
    APIConnectionError,
    AuthenticationError,
    OpenAIError,
    RateLimitError,
)

LOGGER = logging.getLogger(__name__)

router = APIRouter()


@router.post(
    "/generate", response_model=GenerateResponse, status_code=status.HTTP_200_OK
)
async def generate_text(request: PromptRequest) -> GenerateResponse:
    if not request.prompt:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No prompt provided. Please provide a prompt.",
        )
    LOGGER.info(f"Received prompt: {request.prompt}")
    try:
        if settings.OPENAI_API_KEY:
            result = await call_openai_api(request.prompt)
            LOGGER.info(f"Generated text from OpenAI: {result}")
            return GenerateResponse(result=result)

    except (OpenAIError, APIConnectionError, RateLimitError, AuthenticationError) as e:
        LOGGER.error("Error in generate_text when calling OpenAI: %s", e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while processing your request with OpenAI.",
        )

    result = reverse_string(request.prompt)
    LOGGER.info(f"Generated text (reversed string): {result}")
    return GenerateResponse(status_code=status.HTTP_200_OK, result=result)
