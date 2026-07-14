from typing import Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict, model_validator


class CreateBlog(BaseModel):
    title: str
    slug: str = ""
    content: Optional[str] = None

    @model_validator(mode="before")
    @classmethod
    def generate_slug(cls, values):
        if "title" in values:
            values["slug"] = values["title"].replace(" ", "-").lower()
        return values

class UpdateBlog(CreateBlog):
    pass



class ShowBlog(BaseModel):
    title: str
    content: Optional[str]
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)