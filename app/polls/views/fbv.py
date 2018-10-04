# fbc(function-based view)

from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.urls import reverse

from ..models import Question, Choice


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    # question_id에 해당하는 Question 인스턴스를 render함수의 context로 전달
    question = get_object_or_404(Question, pk=question_id)

    # template은 'polls/results.html'을 사용

    # Template에서는 전달받은 Question 인스턴스에 속하는 Choice 목록을 순회하며 보여줌
    # 각 Choice 아이템들의 'choice_text' 및 'votes' 속성값도 같이 출력
    context = {
        'question': question,
    }

    return render(request, 'polls/results.html', context)


def vote(request, question_id):
    # question_id가 pk인 Question 객체를 DB로부터 가져온 데이터로 생
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        context = {
            'question': question,
            'error_message': "You didn't select a choice.",
        }
        return render(request, 'polls/detail.html', context)
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return redirect('polls:results', question.id)


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})
