from hello_app.views import HelloWorldView
from django.urls import path


urlpatterns = [
    path('', view = HelloWorldView.as_view()),
]