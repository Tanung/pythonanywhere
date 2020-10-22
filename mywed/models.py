from django.db import models

#class Question(models.Model):
 #   question_text = models.CharField(max_length=200)
 #   pub_date = models.DateTimeField('date published')

#    def _str_(self):
#        return f'{self.question_text}'

#class Choice(models.Model):
#    question = models.ForeignKey(Question, on_delete=models.CASCADE)
#    choice_text = models.CharField(max_length=200)
#    votes = models.IntegerField(default=0)

#    def _str_(self):
#        return f'{self.question.question.text} - {self.choice_text} - {self.votes}'


class Animal_Type(models.Model):
    text = models.CharField(max_length=200,blank=True)

    def _str_(self):
        return f'{self.text}'


class Animal(models.Model):
    name = models.CharField(max_length=200,blank=True)
    img = models.CharField(max_length=200,blank=True)
    video = models.CharField(max_length=1000,blank=True)
    detail = models.CharField(max_length=1000,blank=True)

    def _str_(self):
        return f'{self.name} - {self.img} - {self.video} - {self.detail}'






