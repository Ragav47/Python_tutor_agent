from tutor.ai_client import client
from config import MODEL_NAME

def explain_error(error):

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": f"Explain this Python error simply and give corrected code:\n{error}"
            }
        ]
    )

    return response.choices[0].message.content