from django.urls import path

from .views import (my_fbv, CourseView, CourseListView, CourseCreateView, CourseUpdateView, CourseDeleteView)

app_name = 'courses'
urlpatterns = [
    # path('', CourseView.as_view(template_name="home.html"), name="courses"),
    path('', CourseListView.as_view(), name="courses"),
    path('create/', CourseCreateView.as_view(), name="courses"),
    path('<int:id>/', CourseView.as_view(), name="courses"),
    path('<int:id>/update', CourseUpdateView.as_view(), name="courses"),
    path('<int:id>/delete', CourseDeleteView.as_view(), name="courses"),
    # path('', my_fbv, name="courses"),
]
