import datetime

from django.db import models
from django.utils import timezone

# 테이블
class Question(models.Model):
    # 속성
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # 함수
    # 질문 text 반환
    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

# 테이블
class Choice(models.Model):
    # 속성
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)

    # 함수
    # 선택 text 반환
    def __str__(self):
        return self.choice_text