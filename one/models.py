from django.db import models

# \\\\\\\\Create your models here.

class Fate(models.Model):
    fate=models.CharField(max_length=100)

    def __str__(self):
        return self.fate

class Movie(models.Model):
    Moviename=models.CharField(max_length=100,primary_key=True)
    movimg=models.ImageField(null=True)
    year=models.IntegerField(null=True)
    bo=models.CharField(max_length=400)
    fate=models.ForeignKey(Fate,on_delete=models.CASCADE)
    director=models.CharField(max_length=400)
    producer=models.CharField(max_length=400)
    cast=models.TextField(null=True)
    rating=models.CharField(max_length=100)
    synopsis=models.TextField(null=True)

def __str__(self):
    return self.mname

class Profile(models.Model):
    
    user=models.CharField(max_length=100)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    age=models.IntegerField(null=True)
    email=models.EmailField(null=True)
    password=models.CharField(max_length=100)
    
    def __str__(self):
        return self.user

class Userreview(models.Model):
    
    Username=models.CharField(max_length=100)
    Moviename=models.ManyToManyField(Movie)
    Review=models.TextField(null=True)
    Rating=models.CharField(max_length=100)
    pic=models.ImageField(null=True)

    def __str__(self):
        return self.user

class Criticreview(models.Model):
    Criticname=models.CharField(max_length=100)
    Moviename=models.ManyToManyField(Movie)
    Review=models.TextField(null=True)
    Experience=models.CharField(max_length=100)
    Rating=models.CharField(max_length=100)
    Pic=models.ImageField(null=True)

    def __str__(self):
        return self.cname
    