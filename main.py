from typing import Optional, List
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel

from api import users, courses, sections


app = FastAPI(
    title="FastAPI LMS",
    description="LMS for managing courses and students.",
    version="0.1.0",
    contact={
        "name": "Toufiq Ahmed",
        "email": "toufiq@example.com",
    },
    license_info={
        "name": "MIT License",
    },
)

app.include_router(users.router)
app.include_router(courses.router)
app.include_router(sections.router)
