from tutor.ai_client import client
from config import MODEL_NAME

def generate_quiz(topic):

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": f"Create 3 MCQ questions about {topic} with answers."
            }
        ]
    )

    return response.choices[0].message.content