from openai import OpenAI

from app.config import OPENAI_API_KEY

# llm = ChatOpenAI(temperature=0.6, openai_api_key=OPENAI_API_KEY)


def handle_response(text: str):
    processed: str = text.lower()

    client = OpenAI()

    response = client.responses.create(
        model='gpt-4.1',
        input=processed
    )

    return response
