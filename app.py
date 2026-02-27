from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from tutor.explainer import explain_topic
from tutor.code_generator import generate_code
from tutor.quiz_generator import generate_quiz
from tutor.error_helper import explain_error


app = FastAPI(title="AI Python Tutor")

# Serve CSS / JS
app.mount("/static", StaticFiles(directory="static"), name="static")


# ==============================
# Request Models
# ==============================

class TopicRequest(BaseModel):
    topic: str


class ErrorRequest(BaseModel):
    error: str


# ==============================
# Home Page
# ==============================

@app.get("/", response_class=HTMLResponse)
def home():
    try:
        with open("templates/index.html", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return HTMLResponse(
            content=f"<h2>Error loading page</h2><p>{str(e)}</p>",
            status_code=500
        )


# ==============================
# Learning Endpoint
# ==============================

@app.post("/learn")
def learn(data: TopicRequest):

    if not data.topic.strip():
        raise HTTPException(status_code=400,
                            detail="Topic cannot be empty")

    try:
        explanation = explain_topic(data.topic)
        code = generate_code(data.topic)
        quiz = generate_quiz(data.topic)

        return {
            "topic": data.topic,
            "explanation": explanation,
            "code": code,
            "quiz": quiz
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"AI Tutor Error: {str(e)}"
        )


# ==============================
# Error Fix Endpoint
# ==============================

@app.post("/error")
def error_help(data: ErrorRequest):

    if not data.error.strip():
        raise HTTPException(
            status_code=400,
            detail="Error message required"
        )

    try:
        fix = explain_error(data.error)
        return {"solution": fix}

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error explanation failed: {str(e)}"
        )