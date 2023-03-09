from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BlogItems(models.Model):
    blog_tittle=models.CharField(max_length=100)
    blog_description=models.TextField(max_length=350)
    created_date=models.DateTimeField(auto_now_add=True)
    blog_author=models.ForeignKey(User,on_delete=models.CASCADE)
    blog_image=models.ImageField()

    def __str__(self):
        return(self.blog_tittle)

