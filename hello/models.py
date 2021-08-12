from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Question(models.Model):
    question_text = models.CharField(max_length=150)
    pub_date = models.DateTimeField(auto_now=True)
    is_opened = models.BooleanField(default=False)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
    votes_amount = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

    
 """ Homework №15 """
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    # There are 2 options for author field, I think with CharField it will be faster, but with ForeignKey it has author exists validation
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    publication_date = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category, related_name = "categories")
    
    def __str__(self):
        return self.title
 
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.PROTECT, unique = True)
    author = models.ForeignKey(User,on_delete = models.CASCADE)
    comment_text =  models.TextField(default = "comment")
    publication_date = models.DateTimeField(auto_now=True)
    comment_like = models.ManyToManyField(User, blank = True, related_name = "comments_likes")
    comment_dislike = models.ManyToManyField(User, blank = True,related_name = "comments_dislikes")
    
    def __str__(self):
        return str(self.author)
    
class Category(models.Model):
    category_name = models.CharField(max_length=200)
    slug = models.SlugField()
    
    def __str__(self):
        return str(self.category_name)
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.PROTECT, unique = True)
    avatar = models.ImageField(upload_to = '/uploads/')
    is_baned = models.BooleanField(default = False)
    scores_factor = models.PositiveSmallIntegerField(default = 1)
    
