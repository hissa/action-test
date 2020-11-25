from django.db import models


class Student(models.Model):
    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.id}: {self.name}'
