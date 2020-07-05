from django.shortcuts import render, get_object_or_404, redirect

from .models import Article
from .forms import BlogForm
from django.urls import reverse

from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView
)
# Create your views here.
############ function base views
# def blog_create_view(request):
#     form = BlogForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = BlogForm()
#
#     context = {
#         "form": form
#     }
#
#     return render(request, "blogs/blog_create.html", context)

# def blog_list_view(request):
#     queryset = Article.objects.all()
#     context = {
#         "object_list": queryset
#     }
#     return render(request, "blogs/blog_list.html", context)

# def blog_detail_view(request, id):
#     obj = get_object_or_404(Article, id=id)
#     context = {
#         "object": obj
#     }
#     return render(request, "blogs/blog_detail.html", context)

# def blog_update_view(request, id):
#     obj = get_object_or_404(Article, id=id)
#     form = BlogForm(request.POST or None, instance=obj)
#     if form.is_valid():
#         form.save()
#
#     context = {
#         "form": form
#     }
#
#     return render(request, "blogs/blog_create.html", context)

# def blog_delete_view(request, id):
#     obj = get_object_or_404(Article, id=id)
#     if request.method == "POST":
#         obj.delete()
#         return redirect("../../")
#
#     context = {
#         "object": obj
#     }
#
#     return render(request, "blogs/blog_delete.html", context)


########## class base views

class blog_list_view(ListView):
    template_name = "blogs/blog_list.html"
    queryset = Article.objects.all()

class blog_detail_view(DetailView):
    template_name = "blogs/blog_detail.html"
    # queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id");
        return get_object_or_404(Article, id=id_)

class blog_create_view(CreateView):
    template_name = "blogs/blog_create.html"
    form_class = BlogForm
    queryset = Article.objects.all()
    # success_url = "/blogs"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class blog_update_view(UpdateView):
    template_name = "blogs/blog_create.html"
    form_class = BlogForm
    queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id");
        return get_object_or_404(Article, id=id_)


    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class blog_delete_view(DeleteView):
    template_name = "blogs/blog_delete.html"
    # success_url = "/blogs"

    def get_object(self):
        id_ = self.kwargs.get("id");
        return get_object_or_404(Article, id=id_)

    def get_success_url(self):
        return reverse("blogs:blog_list")
