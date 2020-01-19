from django.shortcuts import render, get_object_or_404
from .models import Question, Answer
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'QuestionSite/index.html'
    context_object_name = 'latest_questions'

    def get_queryset(self):
        return Question.objects.order_by('question_pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'QuestionSite/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'QuestionSite/results.html'


def vote(request, question_id):

    # Firstly we get question object or 404. Next we get id of answer by POST dict with key 'choice'. As we know
    #    'choice' is name of input in detail template, so it post sth like choice=<answer_id>. If id does not exist
    #    or sth other gone wrong, user will be redirected to voting page. If everything goes well, view increment number
    #    of votes in answer with given id and it will save object. At the end user will be redirected to detail page
    #    again

    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.answer_set.get(pk=request.POST['choice'])
    except(KeyError, Answer.DoesNotExist):
        return render(request, 'QuestionSite/detail.html', {'question': question})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('results', args=(question.id,)))


"""

                                        VIEWS WITHOUT GENERIC!


def index(request):

    # latest_questions get five latest questions trough database API and send them to template in context dict

    latest_questions = Question.objects.order_by('question_pub_date')[:5]
    context = {'latest_questions': latest_questions}
    return render(request, 'QuestionSite/index.html', context)


def detail(request, question_id):

    # detail send question object to template if object is present in database. Otherwise view return 404

    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'QuestionSite/detail.html', {'question': question})


def vote(request, question_id):

    # Firstly we get question object or 404. Next we get id of answer by POST dict with key 'choice'. As we know
    #    'choice' is name of input in detail template, so it post sth like choice=<answer_id>. If id does not exist
    #    or sth other gone wrong, user will be redirected to voting page. If everything goes well, view increment number
    #    of votes in answer with given id and it will save object. At the end user will be redirected to detail page
    #    again

    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.answer_set.get(pk=request.POST['choice'])
    except(KeyError, Answer.DoesNotExist):
        return render(request, 'QuestionSite/detail.html', {'question': question})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('results', args=(question.id,)))


def results(request, question_id):

    # Now we get question object or 404. We have access to all answers from question, so in template we can show
    #    how many votes was given on each option

    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'QuestionSite/results.html', {'question': question})"""
