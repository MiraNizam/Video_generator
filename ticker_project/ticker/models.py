from django.db import models
from django.utils import timezone


class UserInquiry(models.Model):
    """ Model describes input text."""
    input_text = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)

    def str(self):
        return self.input_text
