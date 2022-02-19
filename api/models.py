from django.db import models

# Create your models here.

class task(models.Model):
    task_name = models.CharField(max_length=200, primary_key=True)
    task_description = models.TextField()
    task_completed = models.BooleanField(default=False)
    task_created = models.DateTimeField(auto_now_add=True)
    task_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        texto = "{0} - {1}"
        return texto.format(self.task_name, self.task_description)