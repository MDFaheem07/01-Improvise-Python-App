from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Improvise Python App API")


class TextRequest(BaseModel):
    text: str


class TokenResponse(BaseModel):
    tokens: list[str]
    checksum: int
    message: str


def generate(text: str) -> list[str]:
    # Simple tokenization by whitespace
    return text.split()


def checksum_text(text: str) -> int:
    # Deterministic checksum from characters
    return sum(ord(ch) for ch in text)


@app.get("/")
def welcome():
    return {"message": "Welcome to Improvise Python App API - by MDFaheem07"}


@app.post("/tokenize", response_model=TokenResponse)
def tokenize(payload: TextRequest):
    """
    Accepts a JSON body with one field: "text".
    Returns:
    - tokens: list of words
    - checksum: checksum of input text
    - message: friendly confirmation
    """
    tokens = generate(payload.text)
    checksum = checksum_text(payload.text)
    return {
        "tokens": tokens,
        "checksum": checksum,
        "message": "Text processed successfully."
    }
