from django.db import models

# Create your models here.
from module_management.models import Module
from django.utils.text import slugify
from accounts.models import User

class Lesson(models.Model):

    title = models.CharField(max_length=200)

    description = models.TextField(null=True)

    module = models.ForeignKey(Module,on_delete=models.CASCADE)

    slug = models.SlugField(max_length=250,unique=True,null=True)

    order = models.PositiveIntegerField(null=True)

    video_url = models.URLField()

    created_at = models.DateTimeField(auto_now_add=True)
    
    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(User,on_delete=models.CASCADE)

    resource_link = models.CharField(max_length=200,null=True)

    duration = models.FloatField()


    def save(self,*args,**kwargs):
        if not self.id:

              lesson_object = Lesson.objects.filter(models=self.module).last()

              if lesson_object:

                   self.order = lesson_object.order + 1
              else:
                   self.order = 1
        if not self.slug:
             self.slug = slugify(self.title)

        super().save(*args,**kwargs)
    

    def __str__(self):
            return f"{self.module.title} - {self.title}"
    
    class Meta:
        ordering = ["order"]
        unique_together = ["module", "order"]