from django.db import models
from django.contrib.auth.admin import User
from django.utils.timezone import now
# Create your models here.
class Post(models.Model):
    id = models.AutoField
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateField(auto_now=True)
    def __str__(self):
        return self.title
    
class Contact(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    message = models.CharField(max_length=500)
    def __str__(self):
        return self.name+" - "+self.email+" - "+self.message[:20]
    
class Comment(models.Model):
    sno = models.AutoField
    comments = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    time = models.DateTimeField(default=now)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    parent = models.ForeignKey('self',on_delete=models.CASCADE,null = True)
 
    def __str__(self):
        return self.user.username+" - "+self.comments[:15]
    