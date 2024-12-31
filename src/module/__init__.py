from pydantic import BaseModel

# this variable does not even exist but prefect would be fine deploying it
from .config import USELESS_PLACEHOLDER


class Params(BaseModel):
    name: str
