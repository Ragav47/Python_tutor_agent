from tutor.ai_client import client
from config import MODEL_NAME

def explain_topic(topic):

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": f"""
Teach Python topic: {topic}

Return STRICTLY in this format:

DEFINITION:
...

SYNTAX:
...

EXAMPLE:
...

OUTPUT:
...
"""
            }
        ]
    )

    return response.choices[0].message.content