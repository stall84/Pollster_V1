from django.db import models

# Create your models here.


class Question(models.Model):               # Question class extends Model.. inherits from it
    # Doc's contain all the available FIELDS
    # Define Fields:
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # this function below basically makes the above class display the actual question text
    # If this is left out, all that would be displayed would be something like: Object object
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    # We want to link the two tables (classes) through a foreign key field
    # 2nd arg to this field is the class/table we want to link to
    # On_Delete=Cascade means if a question is deleted ALL of it's choices will also be
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
