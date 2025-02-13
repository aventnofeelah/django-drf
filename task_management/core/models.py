from django.db import models
from django.contrib.auth.models import AbstractUser 

# Create your models here.

ROLE_CHOICES = [ 
        ('admin', 'Admin'), 
        ('manager', 'Manager'), 
        ('employee', 'Employee'), 
] 
class User(AbstractUser): 
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='employee') 

    def __str__(self): 
        return f"{self.username} ({self.role})"
    
class Project(models.Model):
    name = models.CharField(max_length=100, verbose_name="Project title")
    description = models.TextField(verbose_name="Description")
    start_date = models.DateField(verbose_name="Start date")
    end_date = models.DateField(verbose_name="End date")

    def __str__(self):
        return self.name
    
    class Meta:
        indexes = [
            models.Index(fields=['name', 'start_date', 'end_date'])
        ]
        
    
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Category name")

    def __str__(self):
        return self.name

class Priority(models.Model):
    level = models.CharField(max_length=50, verbose_name="Priority")

    def __str__(self):
        return self.level

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    priority = models.ForeignKey(Priority, on_delete=models.SET_NULL, null=True)
    assignee = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    due_date = models.DateField()

    def __str__(self):
        return self.title
    
    class Meta:
        indexes = [
            models.Index(fields=['title', 'project', 'due_date'])
        ]

class Contact(models.Model):
    name = models.CharField(max_length=100) 
    email = models.EmailField() 
    message = models.TextField() 