from .audit import AuditableModel
from enum import Enum
from tortoise import fields, models
import uuid


class Steps(AuditableModel):
    user = fields.ForeignKeyField("models.UserAccount", related_name="steps")
    steps = fields.CharField(max_length=100, default="0")


# IF WE ADD EXERCISE ENTRIES:
# class ExerciseEntry(AuditableModel):
#     uuid = fields.UUIDField(pk=True, default=uuid.uuid4)
#     user = fields.ForeignKeyField("models.UserAccount", related_name="exercises")
#     name = fields.CharField(max_length=100)
#     type = fields.CharField(max_length=100)
#     muscle = fields.CharField(max_length=100)
#     equipment = fields.CharField(max_length=100)
#     difficulty = fields.CharField(max_length=100)
#     instructions = fields.CharField(max_length=5000)
