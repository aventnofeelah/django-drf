from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=30, verbose_name="First name")
    last_name = models.CharField(max_length=30, verbose_name="Last name")
    email = models.EmailField(unique=True, verbose_name="Email")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Project(models.Model):
    name = models.CharField(max_length=100, verbose_name="Project title")
    description = models.TextField(verbose_name="Description")
    start_date = models.DateField(verbose_name="Start date")
    end_date = models.DateField(verbose_name="End date")

    def __str__(self):
        return self.name
    
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