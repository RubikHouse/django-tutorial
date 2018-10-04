# cbv(class-based view)
from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic, View

from ..models import Question, Choice


class IndexView(generic.ListView):
    model = Question
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    ordering = ('-pub_date',)

    def get_queryset(self):
        return super().get_queryset()[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    pk_url_kwarg = 'question_id'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
    pk_url_kwarg = 'question_id'


class VoteView(View):
    def post(self, request, question_id):
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
