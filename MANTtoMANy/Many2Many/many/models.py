from django.db import models


class Student(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    sno = models.IntegerField()
    sname = models.CharField(max_length=30)
    loc = models.CharField(max_length=30)

    def __str__(self):
        return self.sname


class Courss(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    cno = models.IntegerField()
    cname = models.CharField(max_length=30)
    cfee = models.IntegerField()

    def __str__(self):
        return self.cname
