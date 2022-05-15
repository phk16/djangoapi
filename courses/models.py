from django.db import models

# Create your models here.
class Course(models.Model):
    name=models.CharField(max_length=45)
    language=models.CharField(max_length=30)
    price=models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.name
