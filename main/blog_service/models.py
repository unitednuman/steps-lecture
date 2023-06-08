from django.db import models


# Create your models here.
class Reporter(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()


class Publisher(models.Model):
    name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_no = models.CharField(max_length=100)


class Article(models.Model):
    headline = models.CharField(max_length=100)
    details = models.TextField()
    reporter = models.ForeignKey(to=Reporter, on_delete=models.CASCADE)
    publisher = models.ManyToManyField(to=Publisher)
