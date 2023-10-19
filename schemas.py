from pydantic import BaseModel


class ApiRequest(BaseModel):
    method: str
    path: str
    url: str
