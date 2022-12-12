from django.views import View
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

class HelloWorldView(View):
    def get(self, request):
        return render(request, template_name='hello_world.html')