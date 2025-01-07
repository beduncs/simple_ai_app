from pydantic import BaseModel


class SummarizeInput(BaseModel):
    input: str


class SummarizeOutput(BaseModel):
    output: str
