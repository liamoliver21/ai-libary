# LLM Project

A small Python architecture for managing LLM conversations while keeping
conversation state separate from provider-specific implementations.

## Structure

```text
llm_project/
├── pyproject.toml
├── README.md
├── src/
│   └── llm/
│       ├── __init__.py
│       ├── conversation.py
│       ├── history.py
│       ├── message.py
│       ├── backend.py
│       ├── ollama.py
│       └── context.py
└── tests/
    ├── test_conversation.py
    └── test_backend.py
```

## Example

```python
from llm.conversation import LLMConversation
from llm.ollama import OllamaBackend

backend = OllamaBackend("qwen3:8b")
conversation = LLMConversation(backend)

conversation.system("You are a helpful programming assistant.")
response = conversation.send("Explain Python ABCs.")

print(response)
print(conversation.recent_text(4))
```

## Design

`LLMConversation` owns the conversation.

`ConversationHistory` stores messages.

`LLMBackend` is the ABC provider interface.

`OllamaBackend` is one concrete provider implementation.

`ContextManager` determines which part of the history gets sent to the model.
