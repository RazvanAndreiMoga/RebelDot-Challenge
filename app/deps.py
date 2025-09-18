from fastapi import Header, HTTPException

API_TOKEN = "supersecret"

def get_token(x_token: str = Header(...)):
    if x_token != API_TOKEN:
        raise HTTPException(status_code=403, detail="Invalid token")
    return x_token
