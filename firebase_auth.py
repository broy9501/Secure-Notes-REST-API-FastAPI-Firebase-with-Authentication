# File not use


import pyrebase
# from firebase import Firebase
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends, FastAPI, HTTPException, status, Response
import firebase_admin 

from firebase_admin import auth, credentials

# Client config
firebaseConfig = {
  'apiKey': "APIkey",
  'authDomain': "rest-api-auth-note.firebaseapp.com",
  'projectId': "rest-api-auth-note",
  'storageBucket': "rest-api-auth-note.firebasestorage.app",
  'messagingSenderId': "762827454588",
  'appId': "1:762827454588:web:ae9242c9450e198ba731f9",
  'measurementId': "G-BYPTQPPFT6",
  "databaseURL": ""
}

firebase = pyrebase.initialize_app(firebaseConfig)
authenticate = firebase.auth()

# Server config
cred = credentials.Certificate("credentials.json")
firebase = firebase_admin.initialize_app(cred)

def signup():
    print("signu up")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    try:
        user = auth.create_user(email=email, password=password)
        print("User created")
    except Exception as e:
        print(f"Error creating user: {e}")

def login():
    
    try:
        login =  authenticate.sign_in_with_email_and_password(email, password)
        print("User logged in")
        # print(auth.get_account_info(login['idToken']))
        token = login['idToken']
        print(token)
        return token
    except Exception as e:
        print(f"Error creating user: {e}")

security = HTTPBearer()

# res: Response
def verify_token(token: HTTPAuthorizationCredentials = Depends(security)):
    if token is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Bearer authentication required",
            headers={'WWW-Authenticate': 'Bearer realm="auth_required"'},
        )
    try:
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
    # res.headers['WWW-Authenticate'] = 'Bearer realm="auth_required"'
    # return uid
app = FastAPI()
@app.get("/test")
def test(user=Depends(verify_token)):
    return {
        "msg": "Token valid",
        "uid": user["uid"],
        "email": user["email"]
    }

answer = input("Not a new user? (y/n): ")
if answer.lower() == 'y':
    token = login()
    test(token)
    # verify_token()
else:
    signup()
