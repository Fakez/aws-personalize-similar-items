from django.urls import path
from .views import AmazonPersonalizeSimilarItems

app_name = 'api'

urlpatterns = [
    path('getPersonalizeSimilarItems/<prod_ref>', AmazonPersonalizeSimilarItems.as_view()),
]