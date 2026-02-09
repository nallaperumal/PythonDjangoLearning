from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def products(request):
    # return HttpResponse("Hello.. Welcome to our products Page")
    myProducts = [
        {'Name': 'Vanilla cake','Price': 300, 'Description': 'This is a vanilla cake'},
        {'Name': 'Chocolate cake','Price': 320, 'Description': 'This is a chocolate cake'},
         {'Name': 'Red Velvet cake','Price': 350, 'Description': 'This is a red velvet cake'},
         {'Name': 'Black Forest cake','Price': 400, 'Description': 'This is a black forest cake'},
         {'Name': 'Pineapple cake','Price': 250, 'Description': 'This is a pineapple cake'}
    ]
    context = {
        'myProducts': myProducts
    }
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render(context, request))