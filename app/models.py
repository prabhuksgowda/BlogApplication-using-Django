from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=150)
    def __str__(self):
        return self.name 
    
category = ( 
    ("News", "News"), 
    ("Sports", "Sports"), 
    ("Entertainment", "Entertainment"), 
    ("Technology", "Technology"), 
) 

class Post(models.Model):
    title = models.CharField(max_length=250 )
    title_tag=models.CharField(max_length=150 )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=150, choices = category,  default = 'News' )
    content = RichTextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    
    #banner_image=models.ImageField(null=True, blank=True, upload_to="images/")

    #likes= models.ManyToManyField(User, related_name='blogpost')
    def __str__(self):
        return self.title +' | '+str(self.author)

    # def total_likes(self):
    #     return self.likes.count()

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pick = models.ImageField(null=True, blank=True, upload_to="profile/")
    fb_url = models.CharField(max_length=250,null=True, blank=True )
    website_url = models.CharField(max_length=250,null=True, blank=True )



    def __str__(self):
        return str(self.user)