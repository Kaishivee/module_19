from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Post


def post_list(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 2)
    page_number = request.GET.get('page')
    posts_per_page = request.GET.get('per_page', 2)
    paginator = Paginator(post_list, posts_per_page)
    page_obj = paginator.get_page(page_number)
    return render(request, 'second_task/post_list.html', {'page_obj': page_obj})
