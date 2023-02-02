from pydantic import BaseModel

class Body(BaseModel):
    action: str
    release: Release