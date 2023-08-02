from django.db import models

# Create your models here.
class chat_history(models.Model):
    ques=models.CharField(max_length=4000)
    ans=models.TextField(max_length=4000)

    def __str__(self):
        return self.ques