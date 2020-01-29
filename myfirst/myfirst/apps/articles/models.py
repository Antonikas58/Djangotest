import datetime

from django.db import models

from django.utils import timezone


class Article(models.Model):
    article_title = models.CharField('Article title', max_length=200)
    article_text = models.TextField('Text field')
    pub_date = models.DateTimeField('Date of publishing')

    def __str__(self):
        return self.article_title

    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=7))


class Comment(models.Model):
  
  
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author_name = models.CharField('Name of author', max_length=200)
    comment_text = models.CharField('Text of comment', max_length=200)

    def __str__(self):
        return self.comment_text