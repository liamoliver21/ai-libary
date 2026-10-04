from llm.backend import LLMBackend
from llm.message import Message, Role


class FakeBackend(LLMBackend):
    def generate(self, messages: list[Message]) -> str:
        return messages[-1].content


def test_backend_can_generate_from_messages():
    backend = FakeBackend()
    messages = [
        Message.create(Role.SYSTEM, "system"),
        Message.create(Role.USER, "hello"),
    ]

    assert backend.generate(messages) == "hello"
