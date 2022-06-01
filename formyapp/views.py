from turtle import title
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import ArticleForm, ArticleModelForm
from .models import Article

def formRender(request):

    context = {} 

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ArticleModelForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponse("Thanks for your data!")
        
        # If the form was invalid send the user back to fix it
        else:
            context['form'] = form
            return render(request, 'formyapp/formPage.html', context)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ArticleModelForm()
        context['form'] = form

    return render(request, 'formyapp/formPage.html', context)

