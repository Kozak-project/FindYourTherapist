import logging

from openai import OpenAI

from app.config import OPENAI_API_KEY
from app.database.db_services import get_conversation_history

# llm = ChatOpenAI(temperature=0.6, openai_api_key=OPENAI_API_KEY)


def handle_response(text: str, user):
    new_message: str = text.lower()

    client = OpenAI()

    conversation = get_conversation_history(user)

    conversation.append({'role': 'user', 'content': new_message})

    response = client.responses.create(
        model='gpt-4.1',
        input=conversation
    )

    return response
