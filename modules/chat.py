# ✅ Chat module using DialoGPT-small
# File: modules/chat.py

from transformers import pipeline, Conversation
import functools

# Cache model so it's not reloaded every time
@functools.lru_cache(maxsize=1)
def get_chat_pipeline():
    return pipeline("conversational", model="microsoft/DialoGPT-small")

# Store conversation history as a simple list
def generate_response(user_input, history):
    chat_pipeline = get_chat_pipeline()

    # Convert history to proper Conversation object
    if history:
        conversation = Conversation(past_user_inputs=history[::2], generated_responses=history[1::2])
        conversation.add_user_input(user_input)
    else:
        conversation = Conversation(text=user_input)

    result = chat_pipeline(conversation)
    response = result.generated_responses[-1]

    # Update and trim history (last 3 exchanges = 6 entries)
    history.append(user_input)
    history.append(response)
    if len(history) > 6:
        history = history[-6:]

    return response, history
