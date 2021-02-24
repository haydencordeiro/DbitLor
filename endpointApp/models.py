
from django.db import models
from django.contrib.auth.models import User


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return "%s's profile" % self.user


class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return "%s's profile" % self.user


class Status(models.Model):
    status = models.CharField(max_length=100)

    def __str__(self):
        return str(self.status)


class Application(models.Model):

    student = models.ForeignKey(
        StudentProfile, on_delete=models.CASCADE, null=True)
    teacher = models.ForeignKey(
        TeacherProfile, on_delete=models.CASCADE, null=True)
    status = models.ForeignKey(
        Status, on_delete=models.CASCADE, null=True)
    date = models.DateField(auto_now_add=True, blank=True, null=True)
    time = models.TimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return (self.status.status)
