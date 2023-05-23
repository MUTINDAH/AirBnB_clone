#!/usr/bin/python3
from datetime import datetime
from uuid import uuid4

from models import storage


class BaseModel:
    """Base model class for all other classes."""

    id: str = None
    created_at: datetime = None
    updated_at: datetime = None

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            if not storage.contains(self.id):
                storage.new(self)

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        storage.save(self)

    def to_dict(self):
        """Returns a dictionary representation of the object."""
        dict_ = self.__dict__.copy()
        dict_["__class__"] = self.__class__.__name__
        dict_["created_at"] = dict_["created_at"].isoformat()
        dict_["updated_at"] = dict_["updated_at"].isoformat()
        return dict_
