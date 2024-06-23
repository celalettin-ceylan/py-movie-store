import uuid
from peewee import Model,DateTimeField,UUIDField
import datetime
from db import db

class BaseModel(Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4)
    created_at = DateTimeField(default=datetime.datetime.now)
    updated_at = DateTimeField(default=datetime.datetime.now)
    deleted_at = DateTimeField(null=True)

    class Meta:
        database=db
        legacy_table_names = False