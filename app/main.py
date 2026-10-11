from fastapi import FastAPI

app = FastAPI(title="Library Books API")


@app.get("/health")
def health():
    return {"status": "ok"}
