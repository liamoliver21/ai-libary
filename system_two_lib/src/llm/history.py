from __future__ import annotations

from .message import Message, Role


class ConversationHistory:
    def __init__(self) -> None:
        self._messages: list[Message] = []

    def add(self, role: Role, content: str) -> Message:
        message = Message.create(role, content)
        self._messages.append(message)
        return message

    def all(self) -> list[Message]:
        return self._messages.copy()

    def recent(self, count: int) -> list[Message]:
        if count < 0:
            raise ValueError("count must be >= 0")
        return self._messages[-count:] if count else []

    def clear(self) -> None:
        self._messages.clear()

    def __len__(self) -> int:
        return len(self._messages)
