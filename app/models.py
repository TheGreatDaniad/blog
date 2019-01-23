from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).filter(status='published')
class Post(models.Model):


    objects=models.Manager()
    published = PublishedManager()

    def get_absolute_url(self):
       
        return reverse('blog:post_details',kwargs={'year':self.publish.year,'month':self.publish.month,'day':self.publish.day,'post':self.slug})
    STATUS_CHOICES = (
        ('draft','Draft'),
        ('published','Published')
    )
    title= models.CharField(max_length=250)
    slug=models.SlugField(max_length=250,unique_for_date='publish')
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
    body=models.TextField()
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')

    class meta:
        ordering=('-publish',)

    def __str__(self):
        return self.title

