from ctypes import pointer
from datetime import date
from pyexpat import model
from tabnanny import verbose

from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from django.core.validators import MinValueValidator, MaxValueValidator

#from proton.settings import MIN_POINTS_VAL, SEX_CHOICES

class Group(models.Model):
    name = models.CharField(max_length=10, name=_('class'))
    points = models.IntegerField(validators=[
        MinValueValidator(settings.MIN_POINTS_VAL),
        MaxValueValidator(settings.MAX_POINTS_VAL)
    ])
    
    def __str__(self):
        return self.name

class Student(models.Model):
    first_name = models.CharField(max_length=50) #, name=_('First name')
    last_name = models.CharField(max_length=100) #, name=_('Last name')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, name=_('class'))
    sex = models.IntegerField(choices=settings.SEX_CHOICES)
    points = models.IntegerField(validators=[
        MinValueValidator(settings.MIN_POINTS_VAL),
        MaxValueValidator(settings.MAX_POINTS_VAL)
    ])
    
    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return '%s %s %s' % (self.first_name, self.last_name, self.group)
    
    
    
class Event(models.Model):
    name = models.CharField(max_length=500),
    date = models.DateField(default=date.today, auto_now=False, auto_now_add=False)
    
class ClassLog(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    points = models.IntegerField(validators=[
        MinValueValidator(settings.MIN_POINTS_VAL),
        MaxValueValidator(settings.MAX_POINTS_VAL)
    ])
    
class StudentLog(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    points = models.IntegerField(validators=[
        MinValueValidator(settings.MIN_POINTS_VAL),
        MaxValueValidator(settings.MAX_POINTS_VAL)
    ])