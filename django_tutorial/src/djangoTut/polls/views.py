from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.urls.base import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.http import HttpResponse, Http404, HttpResponseRedirect

from .models import Question, Choice
from django.contrib.auth.views import LoginView

# def index (request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     output = ', '.join([q.question_text for q in latest_question_list])

#     context = {
#         'latest_question_list': latest_question_list,
#     }

    # return render(request, 'polls/index.html', context)

class CustomLoginView(LoginView):
    template_name = 'polls/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('polls:index')

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:10]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class BonusView(generic.ListView):
    template_name = 'polls/bonus.html'
    context_object_name = 'question_list'

    def get_queryset(self):

        return Question.objects.order_by('-pub_date')

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
    
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
  
        return HttpResponseRedirect(reverse('polls:index'))

class QuestionCreate(LoginRequiredMixin, CreateView):
    model = Question
    fields = '__all__' 
    success_url = reverse_lazy('polls:index')
    template_name = 'polls/questioncreate.html' 
    context_object_name = 'question'

class QuestionDelete(LoginRequiredMixin, DeleteView):
    model = Question
    template_name = 'polls/questiondelete.html'
    context_object_name = 'question'
    success_url = reverse_lazy('polls:index')
    def delete(self, *args, **kwargs):
       
        return super().delete(*args, **kwargs)

class AddChoice(LoginRequiredMixin, CreateView):
    model = Choice
    fields = ['choice_text', 'question']
    template_name = 'polls/choiceadd.html'
    success_url = reverse_lazy('polls:index')

    

    
    