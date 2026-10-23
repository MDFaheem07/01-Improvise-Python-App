# 01-Improvise-Python-App

A simple FastAPI app that accepts JSON text and returns:
- list of tokens
- checksum of the text
- confirmation message

## Run

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Open:
- API root: http://127.0.0.1:8000/
- Docs: http://127.0.0.1:8000/docs

## Endpoint

### `POST /tokenize`
Request body:
```json
{
  "text": "hello world from fastapi"
}
```

Response:
```json
{
  "tokens": ["hello", "world", "from", "fastapi"],
  "checksum": 2400,
  "message": "Text processed successfully."
}
```
