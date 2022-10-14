from django.db import models


class BaseModel(models.Model):
    created_by = models.ForeignKey("accounts.User", null=True, on_delete=models.SET_NULL,
                                   related_name='time_create_user')
    updated_by = models.ForeignKey("accounts.User", null=True, on_delete=models.SET_NULL,
                                   related_name='time_update_user')

    class Meta:
        abstract = True


class TimestampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True


class Setting(BaseModel, TimestampModel):
    key = models.CharField(max_length=200)
    value = models.TextField()
    is_active = models.BooleanField(default=True)
