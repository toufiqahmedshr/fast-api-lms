import fastapi


router = fastapi.APIRouter()


@router.get("/courses")
async def read_courses():
    return {"courses": []}


@router.post("/courses")
async def create_course_api():
    return {"courses": []}


@router.get("/courses/{course_id}")
async def read_course():
    return {"courses": []}


@router.patch("/courses/{course_id}")
async def update_course():
    return {"courses": []}


@router.delete("/courses/{course_id}")
async def delete_course():
    return {"courses": []}
