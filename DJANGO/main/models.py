from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    
    def __str__(self):
        return self.title 
    
### FOR SCHOOL EXAMPLE 
class School(models.Model):
    name=models.CharField(max_length=200)
    estd_date = models.DateField()
    
    def __str__(self):
        return self.name 
    
### FOR ADDRESS   
class Address(models.Model):
    name =models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural="Addresses"
    
### FOR GRADE  
class Grade(models.Model):
    school=models.ForeignKey(School,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    room_no = models.CharField(max_length=10)
    
    def __str__(self):
        return f"{self.school} | {self.name}"
        # return self.room_no
    
    
      
##FOR STUDENT
class Student(models.Model):
    school = models.ForeignKey(School, on_delete=models.DO_NOTHING) #foreign key banauda yo process use garne
    name=models.CharField(max_length=200)
    roll_no = models.IntegerField()
    address = models.ForeignKey(Address, on_delete=models.DO_NOTHING, null=True, blank=True)
    grade= models.ForeignKey(Grade,on_delete=models.SET_NULL, null=True)
    
    
    def __str__(self):
        return self.name 
    
### FOR STUDENT PROFILE
class StudentProfile(models.Model):
    student=models.OneToOneField(Student, on_delete=models.CASCADE)
    description=models.TextField()
    photo = models.ImageField(upload_to="student_photos", null=True, blank=True)
    
    def __str__(self):
        return f"{self.student}'s profile"
    
class Parent(models.Model):
    name = models.CharField(max_length=200)
    
    children = models.ManyToManyField(Student)
    
    def __str__(self):
        return self.name 