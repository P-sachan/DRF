from django.db import models

class File(models.Model):
  file = models.FileField(upload_to='upload/', blank=False, null=False)
  # remark = models.CharField(max_length=20)
  timestamp = models.DateTimeField(auto_now_add=True)