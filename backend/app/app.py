from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models.interpreter import Interpreter
from data import data
from app.greetings import get_updated_string
from app.spelling_fix import correct_spelling
import uvicorn
import random

__interpreter = Interpreter.load_interpreter("new_stem")
__interpreter.parse("hello")
__app = FastAPI(title="JITBOT", description="A College Enquiry Chat bot of JIT College Nashik")

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:8000",
]

__app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@__app.get("/query/{q}")
async def query(q: str):
    reply = {}
    q = correct_spelling(q)
    try:
        klass = __interpreter.parse(q)
        response = ""
        for res in data.responses:
            if res["intent"] == klass:
                response = random.choice(res["responses"])
                if res["intent"] == "welcomegreeting":
                    response = get_updated_string(response)
                break
        related = []
        for rel in data.related:
            if rel["intent"] == klass:
                related = rel["related"]
                break
        reply = {
            "status": 200,
            "message": response,
            "related": related,
        }
    except Exception as e:
        reply = {
            "status": 400,
            "message" : str(e)
        }
    finally:
        return reply

@__app.get("/direct/{klass}")
async def direct(klass: str):
    response = ""
    related = []
    for res in data.responses:
        if res["intent"] == klass:
            response = random.choice(res["responses"])
            if res["intent"] == "welcomegreeting":
                response = get_updated_string(response)
            break
    for rel in data.related:
        if rel["intent"] == klass:
            related = rel["related"]
            break
    return {
        "status": 200,
        "message": response,
        "related": related,
    }

@__app.get("/{path:path}")
async def not_found_404(path: str):
    return {
        "status": 404,
        "message": f"Path{' '+path} not found on server!, please check the Endpoint",
    }


def run_app():
    uvicorn.run(__app)