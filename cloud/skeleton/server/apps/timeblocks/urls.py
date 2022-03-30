from django.urls import path

from .api_views import HelloApiView
from .views import HelloView

# Add your routes here

urlpatterns = [
    path('hello/', HelloView.as_view(), name='hello'),
    path('api/hello/', HelloApiView.as_view(), name='hello'),
]
