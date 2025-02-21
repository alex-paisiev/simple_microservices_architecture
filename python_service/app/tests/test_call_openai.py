import pytest
from app.api import utils
from openai._exceptions import APIConnectionError

# --- Dummy classes to simulate the OpenAI client ---


class DummyMessage:
    def __init__(self, content: str):
        self.content = content


class DummyChoice:
    def __init__(self, message: DummyMessage):
        self.message = message


class DummyResponse:
    def __init__(self, content: str):
        self.choices = [DummyChoice(DummyMessage(content))]


class DummyCompletions:
    async def create(self, **kwargs) -> DummyResponse:
        # Simulate a successful API response
        return DummyResponse("dummy response")


class DummyChat:
    def __init__(self):
        self.completions = DummyCompletions()


class DummyClient:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.chat = DummyChat()


# --- Test: Successful API call ---


@pytest.mark.asyncio
async def test_call_openai_api_success(monkeypatch):
    """
    Test that call_openai_api returns the expected text on a successful call.
    """
    # Patch AsyncOpenAI to return our DummyClient
    monkeypatch.setattr(utils, "AsyncOpenAI", lambda api_key: DummyClient(api_key))

    prompt = "Test prompt"
    result = await utils.call_openai_api(prompt)
    assert result == "dummy response"


# --- Test: Exception raised by the API call ---


@pytest.mark.asyncio
async def test_call_openai_api_exception(monkeypatch):
    """
    Test that call_openai_api propagates exceptions raised by the OpenAI client.
    """

    # Create dummy classes that simulate an exception during the API call
    class DummyCompletionsException:
        async def create(self, **kwargs):
            # Raise the exception with the required 'request' argument
            raise APIConnectionError(request="Simulated request")

    class DummyChatException:
        def __init__(self):
            self.completions = DummyCompletionsException()

    class DummyClientException:
        def __init__(self, api_key: str):
            self.api_key = api_key
            self.chat = DummyChatException()

    monkeypatch.setattr(
        utils, "AsyncOpenAI", lambda api_key: DummyClientException(api_key)
    )

    prompt = "Test prompt"
    with pytest.raises(APIConnectionError):
        await utils.call_openai_api(prompt)
