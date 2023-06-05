from django.db import models


class Poll(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        db_table = 'poll'

class Question(models.Model):
    text = models.TextField()
    poll = models.ForeignKey(Poll, related_name='questions', on_delete=models.CASCADE)

    class Meta:
        db_table = 'question'


class Answer(models.Model):
    text = models.TextField()
    is_correct = models.BooleanField()
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)

    class Meta:
        db_table = 'answer'
