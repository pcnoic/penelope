from pydantic import BaseModel


class Data(BaseModel):
    input: dict
    input_lan: str
    output_lan: str
