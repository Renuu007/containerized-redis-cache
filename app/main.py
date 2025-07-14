import os
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
import redis

# Read Redis connection info from environment variables
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

# Create Redis client
r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

app = FastAPI()

class SetRequest(BaseModel):
    key: str
    value: str
    ttl: int | None = None  # Time to live in seconds (optional)

class GetResponse(BaseModel):
    key: str
    value: str

@app.get("/")
def read_root():
    return {"message": "Welcome to the Containerized Redis Cache!"}

@app.post("/set")
def set_value(req: SetRequest):
    try:
        if req.ttl:
            r.setex(req.key, req.ttl, req.value)
        else:
            r.set(req.key, req.value)
        return {"message": f"Key '{req.key}' set successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/get", response_model=GetResponse)
def get_value(key: str = Query(..., description="Key to retrieve")):
    value = r.get(key)
    if value is None:
        raise HTTPException(status_code=404, detail="Key not found or expired.")
    return {"key": key, "value": value} 