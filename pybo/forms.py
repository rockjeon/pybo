from django import forms
from pybo.models import Question,Answer,Comment

# 이 같은 클래스를 장고 폼이라 한다.
# form 에는 2개의 폼이 존재한다. forms.Form을 상속받으면 '폼' / forms.ModelForm '모델 폼' 모델 폼은 말 그대로 모델과 연결된 폼이며, 
# 모델 폼 객체를 저장하면 연결된 모델의 데이터를 저장할 수 있다
# 장고 모델 폼에는 meta class 를 반드시 가져야 한다. 

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content']
        labels = {
            'subject': '제목',
            'content': '내용',
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': '댓글내용',
        }

