from tortoise import fields, models
import datetime, time
import uuid

from .audit import AuditableModel

class WaterEntries(AuditableModel):
    uuid = fields.UUIDField(pk=True, default=uuid.uuid4)
    user = fields.ForeignKeyField("models.UserAccount", related_name="water")
    amt = fields.IntField(default=0)
    date = fields.DateField()
    time = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "hydration_log"

class SleepEntries(AuditableModel): 
    uuid = fields.UUIDField(pk=True, default=uuid.uuid4)
    user = fields.ForeignKeyField("models.UserAccount", related_name="sleep")
    date = fields.DateField()
    s_time = fields.TimeField()
    e_time = fields.TimeField()
    h_slept = fields.FloatField(default=0)

    class Meta:
        table = "sleep_log"