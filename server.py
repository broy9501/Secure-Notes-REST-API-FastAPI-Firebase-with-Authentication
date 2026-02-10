from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends, FastAPI, HTTPException, status, Response
from firebase_admin import auth, credentials

import database
import firebase_config

# Initialize security for bearer tokene authentication
security = HTTPBearer()

# Method to verify the token sent by the client in request to the server and decode token if valid, otherwise raise an error
def verify_token(token: HTTPAuthorizationCredentials = Depends(security)):
    print("verify_token called")  
    if token is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Bearer authentication required",
            headers={'WWW-Authenticate': 'Bearer realm="auth_required"'},
        )
    try:
        # Verify the token and decode it to get user information
        decoded_token = auth.verify_id_token(token.credentials)
        print("token valid")
        # uid = decoded_token['uid']

        # print(uid)
        return decoded_token
    except Exception as err:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Invalid authentication credentials. {err}",
            headers={'WWW-Authenticate': 'Bearer error="invalid_token"'},
        )

app = FastAPI()

# Test route to check if token is valid
@app.get("/test")
def test(user=Depends(verify_token)):
    return {
        "msg": "Token valid",
        "uid": user["uid"],
        "email": user["email"]
    }

# Route to create note, get notes, update note and delete note with the token sent by the client in request to the server and using the user information from the decoded token to interact with the database
@app.post("/notes")
def create_note(user=Depends(verify_token)):
    database.create_note("test note", user["uid"])
    return {
        "msg": "Note created",
        "uid": user["uid"],
        "email": user["email"]
    }

@app.get("/notes")
def get_notes(user=Depends(verify_token)):
    database.get_notes(user["uid"])
    return {
        "msg": "Note retrieved",
        "uid": user["uid"],
        "email": user["email"]
    }

@app.put("/notes/{note_id}")
def update_note(note_id: str, user=Depends(verify_token)):
    ok = database.update_note(note_id, "updated note", user["uid"])
    if not ok:
        raise HTTPException(403, "Not allowed")
    return {
        "msg": f"Note updated with id of {note_id}",
        "uid": user["uid"],
        "email": user["email"]
    }


@app.delete("/notes/{note_id}")
def delete_note(note_id: str, user=Depends(verify_token)):
    ok = database.delete_note(note_id,user["uid"])

    if not ok:
        raise HTTPException(403, "Not allowed")
    
    return {
        "msg": f"Note deleted with id of {note_id}",
        "uid": user["uid"],
        "email": user["email"]
    }