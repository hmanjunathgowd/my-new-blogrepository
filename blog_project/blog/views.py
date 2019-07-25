from django.shortcuts import render,get_object_or_404
from blog.models import Post
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
# Create your views here.
from taggit.models import Tag
def post_list_view(request,tag_slug=None):
    post_list=Post.objects.all()
    tag=None
    if tag_slug:
        tag=get_object_or_404(Tag,slug=tag_slug)
        post_list=post_list.filter(tags__in=[tag])
    paginator=Paginator(post_list,3)
    page_number=request.GET.get('page')
    try:
        post_list=paginator.page(page_number)
    except PageNotAnInteger:
        post_list=paginator.page(1)
    except EmptyPage:
        post_list=paginator.page(paginator.num_pages)
    return render(request,"testapp/blog.html",{'post_list':post_list,'tag':tag})

"""from django.views.generic import ListView
class PostListView(ListView):
    model=Post
    paginate_by=1"""
from blog.forms import commentform
def post_detail_view(request,year,month,day,post):

    post=get_object_or_404(Post,slug=post,
                                     status='published',
                                     publish__year=year,
                                     publish__month=month,
                                     publish__day=day)
    comments=post.comments.filter(active=True)
    csubmit=False
    if request.method=='POST':
        form=commentform(request.POST)
        if form.is_valid():
            new_comment=form.save(commit=False)
            new_comment.post=post
            new_comment.save()
            csubmit=True
    else:
        form=commentform()
    return render(request,'testapp/post_detail.html',{'post':post,'csubmit':csubmit,'form':form,'comments':comments})

from django.core.mail import send_mail
from blog.forms import emailsendform
def mail_send_view(request,id):
    post=get_object_or_404(Post,id=id,status='published')
    sent=False
    if request.method=='POST':
        form=emailsendform(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            subject='{}({}) recommends you to read"{}"'.format(cd['name'],cd['email'],post.title)
            post_url=request.build_absolute_uri(post.get_absolute_url())
            message='Read Post At:\n {}\n\n{}\'s comments:\n{}'.format(post_url,cd['name'],cd['comments'])
            send_mail(subject,message,'manju@blog.com',[cd['to']])
            sent=True
    form=emailsendform()
    return render(request,'testapp/sharebymail.html',{'form':form,'post':post,'sent':sent})
