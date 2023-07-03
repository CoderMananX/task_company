from django.db import models

# Create your models here.

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Post_blog(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    description = models.TextField()
    content = models.TextField()
    datetime = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

class Like(models.Model):
    like_id = models.AutoField(primary_key=True)
    post_id = models.ForeignKey(Post_blog,on_delete=models.CASCADE)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)


