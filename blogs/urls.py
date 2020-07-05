from django.urls import path
from .views import (blog_create_view,
                    blog_list_view,
                    blog_detail_view,
                    blog_update_view,
                    blog_delete_view)

app_name="blogs"
urlpatterns = [
    path('', blog_list_view.as_view(), name="blog_list"),
    path('create/', blog_create_view.as_view(), name="blog_create"),
    path('<int:id>/', blog_detail_view.as_view(), name="blog_detail"),
    path('<int:id>/update', blog_update_view.as_view(), name="blog_update"),
    path('<int:id>/delete', blog_delete_view.as_view(), name="blog_delete"),
]
