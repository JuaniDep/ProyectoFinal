from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'core/blog_list.html', {'blogs': blogs})

def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, 'core/blog_detail.html', {'blog': blog})

