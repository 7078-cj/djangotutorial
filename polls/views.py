from django.shortcuts import render
from django.http import HttpResponse
from .models import Questions
from django.template import loader
from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404

# Create your views here.

def index(request):
    latest_question_list = Questions.objects.order_by("-pub_date")[:5]
    context = {
        "latest_question_list": latest_question_list,
    }
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    # try:
    #     question = Questions.objects.get(pk=question_id)
    # except Questions.DoesNotExist:
    #     raise Http404("Question does not exist")
    question = get_object_or_404(Questions, pk=question_id)
    return render(request, "polls/details.html", {"question": question})

def result(request, question_id):
    response = "You're looking at the result of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
