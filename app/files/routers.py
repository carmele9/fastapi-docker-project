from fastapi import APIRouter

router = APIRouter()


@router.get("/files")
async def get_files():
    return {"message": "Files fetched successfully"}


@router.post("/files")
async def create_file():
    return {"message": "File created successfully"}


@router.get("/files/{id}")
async def get_file(id: int):
    return {"message": f"File {id} fetched successfully"}


@router.post("/files/{id}")
async def update_file(id: int):
    return {"message": f"File {id} updated successfully"}


@router.delete("/files/{id}")
async def delete_file(id: int):
    return {"message": f"File {id} deleted successfully"}


@router.post("/files/merge")
async def merge_files():
    return {"message": "Files merged successfully"}
