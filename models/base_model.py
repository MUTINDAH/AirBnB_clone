from uuid import uuid4
from datetime import datetime
import json


class BaseModel:
    """Base model class for all other models."""

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

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()
        storage.save(self)

    def to_dict(self):
        """Returns a dictionary representation of the model."""
        dict_ = self.__dict__.copy()
        dict_['__class__'] = self.__class__.__name__
        dict_['created_at'] = dict_['created_at'].isoformat()
        dict_['updated_at'] = dict_['updated_at'].isoformat()
        return dict_

    def from_dict(self, dict_):
        for key, value in dict_.items():
            if key != "__class__":
                setattr(self, key, value)
        self.updated_at = datetime.now()


if __name__ == "__main__":
    from engine.file_storage import FileStorage

    storage = FileStorage()
    storage.reload()

    model = BaseModel()
    storage.new(model)
    storage.save()
    storage.reload()
    print(storage.all())
