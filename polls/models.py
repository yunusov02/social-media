import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin
# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


    @admin.display(boolean=True, ordering="pub_date", description="Published recently?")
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
        # return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    

    def __repr__(self):
        return self.question_text[:50]
    
    def __str__(self):
        return self.question_text[:50]
    
    class Meta:
        db_table = 'question'
        ordering = ['-pub_date']


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=120)
    votes = models.IntegerField(default=0)

    def __repr__(self):
        return self.choice_text[:50]
    

    def __str__(self):
        return self.choice_text[:50]
    

    class Meta:
        db_table = 'choice'
        ordering = ['votes']



class TestModel(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)


    def __repr__(self):
        return self.text[:50]
    
