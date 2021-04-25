from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = models.Manager()
    subject = models.CharField(max_length=200) # 글자 수 를 제한하는 
    content = models.TextField() # 글자 수 제한이 없는 
    create_date = models.DateTimeField() # 날짜 시간 관련 속성은 DateTimeField
    def __str__(self):
        return self.subject
    


class Answer(models.Model):
    # 어떤 모델이 다른 모델을 속성으로 가지면 ForeignKey 를 이용한다 (다른 모델과의 연결)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # 답볌에 연결된 질문이 삭제되면 답변도 함께 삭제
    content = models.TextField()
    create_date = models.DateTimeField()





