from django.db import models

# Create your models here.


class News(models.Model):
    news_name = models.CharField(max_length=100)
    news_link = models.CharField(max_length=2000)
    news_date = models.DateTimeField(auto_now=True)
    news_text = models.TextField()
    news_source = models.CharField(max_length=20)
    news_category = models.CharField(max_length=20, default='General')
    news_image = models.ImageField(upload_to='media/', blank=True, null=True)
    
    @property
    def comsay(self):
        say = Comments.objects.filter(news_id=self.id).count()
        return say

class Comments(models.Model):
    news_id = models.ForeignKey(News, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=15)
    user_surname = models.CharField(max_length=20)
    user_email = models.EmailField(max_length=30)
    user_comment = models.TextField()
    comment_date = models.DateTimeField(auto_now=True)