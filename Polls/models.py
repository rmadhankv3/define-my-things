from django.db import models
from django.utils import timezone

# Create your models here.

class Poll_Template(models.Model):
    name = models.TextField()
    active = models.BooleanField(default=False)
    chart_title = models.CharField(max_length=30)
    country = models.TextField()
    description = models.TextField()
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    url = models.URLField()
    status = models.CharField(max_length=30)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now)



class Poll_Question(models.Model):
	active = models.BooleanField(default=False)
	char_limit = models.IntegerField()
	Poll_Template = models.ForeignKey('Poll_Template', on_delete=models.CASCADE)
	mandatory = models.BooleanField(default=False)
	multi_line_text = models.BooleanField(default=False)
	question_text = models.TextField()
	q_type = (('Text','Text'),('Checkbox','Checkbox'),('Radio button','Radio button'))
	question_type = models.CharField(max_length=15,choices=q_type,default='Text')
	sequence = models.IntegerField()
	created_date = models.DateTimeField(default=timezone.now)
	modified_date = models.DateTimeField(default=timezone.now)


class Poll_Question_Options(models.Model):
	active = models.BooleanField(default=False)
	answer_Option = models.TextField()
	Poll_Question = models.ForeignKey('Poll_Question', on_delete=models.CASCADE)
	sequence = models.IntegerField()
	created_date = models.DateTimeField(default=timezone.now)
	modified_date = models.DateTimeField(default=timezone.now)



class Poll_Response_Sheet(models.Model):
    started_on = models.DateTimeField(blank=True, null=True)
    completed_on = models.DateTimeField(blank=True, null=True)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    Poll_Template = models.ForeignKey('Poll_Template', on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now)


class Poll_Response_Answer(models.Model):
    active = models.BooleanField(default=False)
    Poll_Response_Sheet = models.ForeignKey('Poll_Response_Sheet', on_delete=models.CASCADE)
    Poll_Question = models.ForeignKey('Poll_Question', on_delete=models.CASCADE)
    question_text = models.TextField()
    answer_given = models.TextField()
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now)








