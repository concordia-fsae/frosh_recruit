from django.urls import path
from . import views


app_name = 'recruit_app'
urlpatterns = [
    path('', views.page_submit, name="page_submit"),
    path('submit/', views.submit, name="submit")
]
