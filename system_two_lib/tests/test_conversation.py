from llm.backend import LLMBackend
from llm.conversation import LLMConversation
from llm.context import RecentContextManager
from llm.message import Message, Role


class FakeBackend(LLMBackend):
    def __init__(self, response: str = "fake response") -> None:
        self.response = response
        self.received: list[Message] = []

    def generate(self, messages: list[Message]) -> str:
        self.received = list(messages)
        return self.response


def test_system_user_assistant_messages_are_supported():
    backend = FakeBackend("hello")
    conversation = LLMConversation(backend)

    conversation.system("Be concise.")
    response = conversation.send("Hi")

    assert response == "hello"
    assert [m.role for m in conversation.messages()] == [
        Role.SYSTEM,
        Role.USER,
        Role.ASSISTANT,
    ]


def test_recent_text_returns_latest_messages():
    backend = FakeBackend()
    conversation = LLMConversation(backend)

    conversation.system("system")
    conversation.user("one")
    conversation.assistant("two")

    assert conversation.recent_text(2) == "user: one\nassistant: two"


def test_context_manager_limits_backend_context():
    backend = FakeBackend()
    conversation = LLMConversation(
        backend,
        context_manager=RecentContextManager(count=2),
    )

    conversation.system("system")
    conversation.user("one")
    conversation.user("two")
    conversation.generate()

    assert [m.content for m in backend.received] == ["one", "two"]
