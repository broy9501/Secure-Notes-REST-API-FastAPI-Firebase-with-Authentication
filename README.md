# 🔐 Secure Notes REST API (FastAPI + Firebase)

A secure REST API built with **FastAPI** and **Firebase Authentication** that allows users to create, read, update, and delete personal notes using **JWT-based authentication** through Firebase and **Firebase Realtime Database**.

This project demonstrates backend development skills including authentication, authorization, RESTful APIs, and cloud database integration.

---

## 🚀 Features

- ✅ Firebase Email/Password Authentication
- ✅ JWT Token Verification
- ✅ Protected API Endpoints
- ✅ CRUD Operations for Notes
- ✅ User Authorization (Users can only access their own notes)
- ✅ Firebase Realtime Database Integration
- ✅ RESTful API Design

---

## 🛠️ Tech Stack

- **Backend:** FastAPI (Python)
- **Authentication:** Firebase Auth
- **Database:** Firebase Realtime Database
- **Security:** JWT (Firebase ID Tokens)
- **HTTP Client:** Requests
- **Server:** Uvicorn

---

## 📂 Project Structure
├── server.py # FastAPI server
├── database.py # Database operations
├── firebase_config.py # Firebase setup
├── client.py # Test client

---

## 🤖 Run The Server
uvicorn server:app --reload

---

## 🔐 Authentication Flow

1. User logs in via Firebase
2. Firebase returns an ID Token
3. Client sends token in Authorization header
4. FastAPI verifies token using Firebase Admin
5. User UID is extracted
6. Database access is granted

---

## 📈 Security Features

- Token validation on every request
- Route protection using FastAPI dependencies
- User ownership verification
- Unauthorized access blocked
- Secure Firebase credentials
