from django.db import models

# Create your models here.
class Tasks(models.Model):
  task_type = models.CharField(max_length=100),
  completed_by = models.CharField(max_length=50),
  completed_on = models.DateTimeField(auto_now_add=True)

  def __str__(self):
        return self.id
