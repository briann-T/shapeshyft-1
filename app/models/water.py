from tortoise import fields, models
import datetime
import uuid

from .audit import AuditableModel

class WaterEntries(AuditableModel):
    uuid = fields.UUIDField(pk=True, default=uuid.uuid4)
    user = fields.ForeignKeyField("models.UserAccount", related_name="water")
    amt = fields.IntField(default=0)
    date = fields.DateField()
    s_time = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "hydration_log"
