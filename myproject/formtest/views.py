from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from .forms import NameForm


def index(request):
    return HttpResponse("Hello, world")


def hello_template(request):
    template = loader.get_template('hello.html')
    return HttpResponse(template.render())


def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("/thanks/")

    if request.method == 'GET':
        form = NameForm()

    return render(request, 'form_01.html', {'form': form})
