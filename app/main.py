from fastapi import FastAPI
from authentication.routers import router as auth_router
from files.routers import router as files_router

# Create the FastAPI app
app = FastAPI()

# Include the routers
app.include_router(auth_router, prefix="/auth", tags=["authentication"])
app.include_router(files_router, prefix="/files", tags=["files"])


# Test route to check if the app is running
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI is running!"}
