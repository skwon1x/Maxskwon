from django.urls import path
from .views import index, top_sellers, advertisment_post, advertisment

urlpatterns = [
    path('', index, name='main-page'),
    path('top-sellers/', top_sellers, name='top-sellers'),
    path('advertisement-post/', advertisment_post, name='advertisement-post'),
    path('advertisement/', advertisment, name='advertisement'),
]