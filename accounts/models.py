from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):

    phone = models.CharField(max_length=15,unique=True)

    ROLE_CHOICES=(
        ("tutor","tutor"),
        ("student","student")
    )

    role = models.CharField(max_length=200,choices=ROLE_CHOICES,default="student")



class TrainerProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="trainer_profile",
    )
    bio = models.TextField(blank=True,null=True)
    expertise = models.CharField(max_length=255, blank=True)
    experience_years = models.PositiveIntegerField(default=0)
    organization = models.CharField(max_length=255, blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"TrainerProfile: {self.user.username}"


class StudentProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="student_profile",
    )
    bio = models.TextField(blank=True,null=True)
    education = models.CharField(max_length=255, blank=True,null=True)
    skills = models.CharField(max_length=255, blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"StudentProfile: {self.user.username}"


from django.db.models.signals import post_save

def Created_Tranier_profile(sender,instance,created,**kwargs):

    if created and instance.role == "tutor":

        TrainerProfile.objects.create(user=instance)

post_save.connect(Created_Tranier_profile,sender=User)

def created_student_profile(sender,instance,created,**kwargs):

    if created and instance.role == "student":

        StudentProfile.objects.create(user=instance)

post_save.connect(created_student_profile,sender=User)