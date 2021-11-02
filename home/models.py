from django.db import models

class questions(models.Model):
    
    q_id=models.AutoField(primary_key=True)
    info=models.TextField(max_length=300)
    upvote=models.IntegerField()
    author=models.CharField(max_length=100)

class answers(models.Model):
    a_id=models.AutoField(primary_key=True)
    info=models.TextField(max_length=300)
    author=models.CharField(max_length=100)
    for_q=models.IntegerField()
    

    
