from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    objects = models.Manager()
    subject = models.CharField(max_length=200) # 글자 수 를 제한하는 
    content = models.TextField() # 글자 수 제한이 없는 
    create_date = models.DateTimeField() # 날짜 시간 관련 속성은 DateTimeField
    modify_date = models.DateTimeField(null = True, blank = True) # null 을 사용한다 / 입력 폼 데이터 검사 시 값이 없어도 된다.
    # 게시판 서비스를 사용해 봤다면 글 1개에 여러 명이 추천할 수 있고, 
    # 반대로 1명이 여러 개의 글을 추천할 수 있음을 쉽게 알 수 있다. 그리고 이런 경우에는 모델의 다대다(ManyToMany) 관계
    voter = models.ManyToManyField(User, related_name='voter_question')  # voter 추가
    def __str__(self):
        return self.subject
    


class Answer(models.Model):
    # 어떤 모델이 다른 모델을 속성으로 가지면 ForeignKey 를 이용한다 (다른 모델과의 연결)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # 답볌에 연결된 질문이 삭제되면 답변도 함께 삭제
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null = True, blank = True)
    voter = models.ManyToManyField(User, related_name='voter_answer')


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)
