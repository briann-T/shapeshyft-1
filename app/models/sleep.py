from tortoise import fields, models
import datetime
from datetime import time
import uuid

from .audit import AuditableModel

class SleepEntries(AuditableModel):
    uuid = fields.UUIDField(pk=True, default=uuid.uuid4)
    user = fields.ForeignKeyField("models.UserAccount", related_name="sleep")
    date = fields.DateField()
    s_time = fields.TimeField()
    e_time = fields.TimeField()
    h_slept = fields.FloatField(default=0)

    class Meta:
        table = "sleep_log"
