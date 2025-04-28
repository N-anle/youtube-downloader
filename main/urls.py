from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage,  name = 'homepage'),
    path('<int:vid_id>/download',views.download_content, name = 'download')
]
