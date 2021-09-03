from App.models import Category
from django.db import models


# Create your models here.
class Travel(models.Model):
        title = models.CharField(max_length=100)
        write_by = models.CharField(max_length=100)
        discription = models.TextField()
        step1 = models.TextField()
        step2 = models.TextField()
        step3 = models.TextField()
        step4 = models.TextField()
        step5 = models.TextField()
        timestamp = models.DateTimeField(auto_now_add=True)
        view_count = models.IntegerField(default = 0)
        author = models.CharField(max_length=100)
        author_img = models.ImageField(upload_to='images/author')
        thumbnail = models.ImageField(upload_to='images/thumbnail/')
        categories = models.ForeignKey(Category, on_delete= models.CASCADE)
        featured = models.BooleanField()
    
    
def __str__(self):
        return self.title