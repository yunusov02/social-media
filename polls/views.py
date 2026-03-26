from django.http import Http404, HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.db.models import F
from django.urls import reverse
from django.views import generic

from polls.models import Choice, Question



class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:5]
    


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"



def index(request: HttpRequest):

    latest_question_list = Question.objects.order_by("-pub_date")[:5]

    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)

    context = {
        "latest_question_list": latest_question_list
    }

    # template = loader.get_template('polls/index.html')
    # return HttpResponse(template.render(context, request))

    return render(request, 'polls/index.html', context)


def detail(request: HttpRequest, question_id):

    # try:
    #     question = Question.objects.get(id=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question doesn't exists")

    question = get_object_or_404(Question, pk=question_id)

    return render(request, "polls/detail.html", context={"question": question})

def results(request: HttpRequest, question_id):

    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})

    response = "You are looking at the results of question %s"
    return HttpResponse(response % question_id)


def vote(request: HttpRequest, question_id):

    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        
        return render(
            request=request,
            template_name="polls/detail.html",
            context={
                "question": question,
                "error_message": "You didn't select a choice"
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()

        # Always return an HttpRedirect after successfully deailing with POST data

        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))




    return HttpResponse("You are voting on question %s" % question_id)



