from django.shortcuts import render,get_object_or_404
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.all()


    return render(request,"post/list.html",{'posts':posts})

def post_details (request,year,month,day,post):
    post=get_object_or_404(Post,status='published',published__year=year,published__month=month,published__day=day)
    return render(request,'post/detail.html',{'post':post})
