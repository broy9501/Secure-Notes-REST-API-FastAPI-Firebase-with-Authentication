import pyrebase
import requests

# Client config
firebaseConfig = {
  'apiKey': "apiKey",
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


# Method to sign up and creete an account with email and password
def signup():
    print("signu up")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    try:
        user = authenticate.create_user_with_email_and_password(email=email, password=password)
        print("User created")
    except Exception as e:
        print(f"Error creating user: {e}")

# Method to log in with email and password and return the token
def login():
    print("log in")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    try:
        login = authenticate.sign_in_with_email_and_password(email=email, password=password)
        # db = firebase.database()
        # db.push({"test": "testing"}, login['idToken'])
        token = login['idToken']
        print(token)
        return token
    except Exception as e:
        print(f"Error logging in: {e}")

# Check if user is signing up or logginn in and getting the token
answer = input("Not a new user? (y/n): ")
if answer.lower() == 'y':
    token = login()
else:
    signup()

# Using the token to make a request to the server
header = {
    "Authorization": f"Bearer {token}"
}

# A test note id for deleting or updating note
note_id = "-Ol74yq0ekXuNnG3intD"

# Request to server to complete an action with the token (create, get, update or delete note) 
# http://127.0.0.1:8000/notes/ for get and post, http://127.0.0.1:8000/notes/{note_id} for put and delete
repsonse = requests.delete(
    f"http://127.0.0.1:8000/notes/{note_id}",
    headers=header
)

print(repsonse.json())
