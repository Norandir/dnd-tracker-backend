from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.monsters import router as monster_router

app = FastAPI()

# CORS configuration (Add the domains that should be allowed to make requests)
origins = [
    "http://192.168.40.181:8081",  # Replace with your frontend URL (React app, for example)
    "http://127.0.0.1:19006",  # If using Expo
]

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # You can specify a list of allowed origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Include the router so "/monsters" works
app.include_router(monster_router)

@app.get("/")
def home():
    return {"message": "D&D API Proxy Running"}
