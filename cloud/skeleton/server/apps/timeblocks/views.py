from django.http import HttpResponse
from django.views import View

# Create your views here


class HelloView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, World!')
