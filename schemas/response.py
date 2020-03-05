from typing import Optional

from pydantic import BaseModel


class ResponseBase(BaseModel):
    error: Optional[int] = 0
