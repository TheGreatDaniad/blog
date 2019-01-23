from django.shortcuts import render,get_object_or_404
from .models import Post    
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.
def post_list(request):
    object_list = Post.objects.all()
    paginator= Paginator(object_list,5)
    page=request.GET.get('page')
    try:
        posts=paginator.page(page)
    except PageNotAnInteger:
        posts=paginator.page(1)
    except EmptyPage:
        posts=paginator.page(paginator.num_pages)

    return render(request,"post/list.html",{'posts':posts})

def post_details (request,year,month,day,post):
    post=get_object_or_404(Post,status='published',publish__year=year,publish__month=month,publish__day=day)
    return render(request,'post/details.html',{'post':post})
