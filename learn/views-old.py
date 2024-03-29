# coding:utf-8
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404,render
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.http import Http404
from django.urls import reverse
import logging, traceback, pprint
from django.views import generic
from .models import Question,Choice

logging.basicConfig(level=logging.INFO)
#@login_required



def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
   #output = ', '.join([q.question_text for q in latest_question_list])
    #template = loader.get_template('index.html')
    context = {
        'late_question_list': latest_question_list,
    }
    return render(request, 'learn/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'learn/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'learn/results.html', {'question': question})



def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'learn/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('results', args=(question.id,)))