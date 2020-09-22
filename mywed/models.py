from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def _str_(self):
        return f'{self.question_text}'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def _str_(self):
        return f'{self.question.question.text} - {self.choice_text} - {self.votes}'

class TypeStory(models.Model):
    text = models.CharField(max_length=200)

    def _str_(self):
        return f'{self.type_story.text} - {self.name} - {self.favour} favour.'


class Title(models.Model):
    type_story = models.ForeignKey(TypeStory, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    favour = models.IntegerField(default=0)

    def _str_(self):
        return f'{self.text}'

