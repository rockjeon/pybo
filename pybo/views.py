from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Question
from django.utils import timezone
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

def index(request):
    """
    pybo 목록 출력
    
    """
    # 입력 파라미터
    page = request.GET.get('page','1') # GET 방식 요청 URL에서 page 값을 가져올때
    question_list = Question.objects.order_by('-create_date') # - 붙히면 역순으로 정렬됨
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj}

    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    
    return render(request, 'pybo/question_detail.html', context)


# question_id 매개변수에는 url 매핑 정보값이 넘어온다. ex) pybo/answer/create/2 -> 2가 넘어온다.
# request 매개변수에는 pybo/qeustion_detail.html 에서 textarea에 입력된 데이터가 담겨 넘어온다.

@login_required(login_url='common:login')
def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user 
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)

@login_required(login_url='common:login')
# QuestionForm 클래스로 생성한 객체 form을 사용 할 것이다. 
def question_create(request):
    if request.method == 'POST':
        # QuestionForm(request.POST)처럼 화면에서 전달받은 데이터로 폼의 값이 채워지도록 객체를 생성했다.
        form = QuestionForm(request.POST) # form이 유효한지 검사한다.
        if form.is_valid():
            question = form.save(commit=False) # 임시저장을 의미한다. 이유는 폼으로 질문 데이터를 저장할 경우 Question create_date 에 값이 설정되지 않아 오류가 나기 때문
            question.author = request.user
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)