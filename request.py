from pydantic import BaseModel

class Request_DTO(BaseModel):
    text: str