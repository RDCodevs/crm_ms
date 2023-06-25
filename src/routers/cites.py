from fastapi import APIRouter, status

router = APIRouter(prefix= "/cites")

@router.get("/get_cite/{id_cite}")
async def get_cite_by_id():
    pass

@router.get("/get_all")
async def get_all_cite():
    pass

@router.post("/add_cite")
async def create_cite():
    pass

@router.put("/update_cite")
async def update_cite():
    pass

@router.patch("/edit_cite")
async def patch_cite():
    pass

@router.delete("/delete_cite")
async def delete_cite():
    pass