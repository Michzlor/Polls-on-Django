from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from random import randrange

from .models import Choice, Question



class IndexView(generic.ListView):
    template_name = "polls/index.html"

    def get_queryset(self):
        pass

        return 0
                

class RecentPollsView(generic.ListView):
    template_name = "polls/polls.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """
        Return the last five published questions exluding quiestions without set answers
        (not including those set to be published in the future).
        """
        list_to_check = Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]
        to_return = []
        for i in list_to_check:
            if Choice.objects.filter(question=i):
                to_return.append(i)

        return to_return

class DailyPollView(generic.ListView):
    template_name = "polls/polls.html"
    context_object_name = "latest_question_list"
    
    def get_queryset(self):
        timezone.datetime.date
        return  Question.objects.filter(pub_date__startswith = timezone.now().date())


class PollsListView(generic.ListView):
    template_name = "polls/list.html"
    context_object_name = "all_question_list"
    
    def get_queryset(self):
        """
        Returns all published questions.
        """
        return Question.objects.all 

class RandomPollView(generic.ListView):
    template_name = "polls/polls.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        id = randrange(len(Question.objects.all()))
        print('id:  ',id)
        return Question.objects.filter(pk__exact = id+1)


class PopularPollsView(generic.ListView):
    template_name = "polls/popular.html"
    context_object_name = "popular_questions_list"

    def get_queryset(self):
        """
        Returns 5 questions with highest ammount of votes.
        """


        return Question.objects.all().order_by("-total_votes")[:3]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        question.total_votes += 1
        question.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
# Create your views here.
