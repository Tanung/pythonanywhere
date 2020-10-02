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
    text = models.CharField(max_length=200)

    def _str_(self):
        return f'{self.animal_type.text} - {self.name} - {self.score} score.'


class Animal(models.Model):
    animal_type = models.ForeignKey(Animal_Type, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    score = models.IntegerField(default=0)

    def _str_(self):
        return f'{self.text}'






