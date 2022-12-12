from hello_app.views import HelloWorldView, HelloView
from django.urls import path


urlpatterns = [
    path('world', view = HelloWorldView.as_view()),
    path('<str:name>', view = HelloView.as_view()),
]