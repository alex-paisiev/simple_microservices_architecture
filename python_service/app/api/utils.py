import logging

from app.core.config import settings
from openai import AsyncOpenAI
from openai._exceptions import (
    APIConnectionError,
    AuthenticationError,
    OpenAIError,
    RateLimitError,
)

LOGGER = logging.getLogger(__name__)


async def call_openai_api(prompt: str) -> str:
    """
    Call the OpenAI API with the given prompt and return the raw text response.
    """

    client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)
    try:
        response = await client.chat.completions.create(
            model=settings.OPENAI_MODEL,
            messages=[{"role": "system", "content": prompt}],
            max_tokens=settings.OPENAI_MODEL_MAX_TOKENS,
            temperature=settings.OPENAI_MODEL_TEMPERATURE,
        )
        result_text = response.choices[0].message.content
        LOGGER.debug("Raw API response: %s", result_text)
        return result_text
    except (OpenAIError, APIConnectionError, RateLimitError, AuthenticationError) as e:
        LOGGER.error("Error calling OpenAI API: %s", e)
        raise e


def reverse_string(text: str) -> str:
    """Return the reversed version of the input text."""
    return text[::-1]
