from __future__ import annotations

from .backend import LLMBackend
from .context import ContextManager, RecentContextManager
from .history import ConversationHistory
from .message import Message, Role


class LLMConversation:
    """Public conversation/session object used by application code."""

    def __init__(
        self,
        backend: LLMBackend,
        context_manager: ContextManager | None = None,
    ) -> None:
        self.backend = backend
        self.history = ConversationHistory()
        self.context_manager = context_manager or RecentContextManager()

    def add(self, role: Role, content: str) -> Message:
        return self.history.add(role, content)

    def system(self, content: str) -> Message:
        return self.add(Role.SYSTEM, content)

    def user(self, content: str) -> Message:
        return self.add(Role.USER, content)

    def assistant(self, content: str) -> Message:
        return self.add(Role.ASSISTANT, content)

    def tool(self, content: str) -> Message:
        return self.add(Role.TOOL, content)

    def send(self, content: str) -> str:
        """Add a user message, generate, and store the assistant response."""
        self.user(content)
        return self.generate()

    def generate(self) -> str:
        """Generate from the current conversation without adding a user message."""
        messages = self.context_manager.build(self.history)
        response = self.backend.generate(messages)
        self.assistant(response)
        return response

    def messages(self) -> list[Message]:
        return self.history.all()

    def recent(self, count: int = 5) -> list[Message]:
        return self.history.recent(count)

    def recent_text(self, count: int = 5) -> str:
        return "\n".join(
            f"{message.role.value}: {message.content}"
            for message in self.recent(count)
        )

    def context(self) -> list[Message]:
        return self.context_manager.build(self.history)

    def clear(self) -> None:
        self.history.clear()
