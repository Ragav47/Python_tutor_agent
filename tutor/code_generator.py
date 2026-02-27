from tutor.ai_client import client
from config import MODEL_NAME

def generate_code(topic):

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": f"Write beginner Python code for {topic} with output."
            }
        ]
    )

    return response.choices[0].message.content