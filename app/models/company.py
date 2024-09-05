from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime
from typing import Literal

class CompanyModel(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    description: str = Field(default="")
    mode: Literal['online', 'offline', 'hybrid'] = Field(default='online')
    rating: float = Field(ge=0, le=5)

class CompanyViewModel(BaseModel):
    id: UUID
    name: str
    description: str
    mode: Literal['online', 'offline', 'hybrid']
    rating: float
    created_at: datetime | None = None
    
    class Config:
        from_attributes = True
