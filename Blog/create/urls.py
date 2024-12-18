from django.urls import path
from . import views
urlpatterns = [
    path('free/', views.render_free,name ='free' )
]