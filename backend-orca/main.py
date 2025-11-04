from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "Hello, world!"}


if __name__ == "__main__":
    # Run with: uvicorn backend-orca.main:app --reload
    # or use the helper below for direct launch (requires uvicorn installed).
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
