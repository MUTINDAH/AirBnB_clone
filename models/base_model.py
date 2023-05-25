#!/usr/bin/python3
import uuid
from datetime import datetime


class BaseModel:
    """Base class for all other models."""

    id: str = None
    created_at: datetime = None
    updated_at: datetime = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary representation of the model."""
        dict_ = self.__dict__.copy()
        dict_["__class__"] = self.__class__.__name__
        dict_["created_at"] = dict_["created_at"].isoformat()
        dict_["updated_at"] = dict_["updated_at"].isoformat()
        return dict_
