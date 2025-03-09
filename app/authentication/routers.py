from fastapi import APIRouter

router = APIRouter()


@router.post("/register")
async def register():
    return {"message": "User registered successfully"}


@router.post("/login")
async def login():
    return {"message": "User logged in successfully"}


@router.post("/logout")
async def logout():
    return {"message": "User logged out successfully"}


@router.get("/introspect")
async def introspect():
    return {"message": "User introspection successful"}
