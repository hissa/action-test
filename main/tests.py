from django.test import TestCase
from . import models

# Create your tests here.


class StudentTest(TestCase):
    def test_to_str(self):
        self.assertEqual(models.Student.objects.count(), 0)
        student = models.Student(name="TestTaro")
        student.save()
        self.assertEqual(models.Student.objects.count(), 1)
        self.assertEqual(str(student), f'{student.id}: {student.name}')
