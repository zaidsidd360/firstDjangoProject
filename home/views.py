from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    context = {
        'variable': "peepeepoopoo"
    }
    return render(request, 'index.html', context)
    # return HttpResponse("This is home page")


def about(request):
    return HttpResponse("This is about page")


def services(request):
    return HttpResponse("This is services page")


def contact(request):
    return HttpResponse("This is contact page")
