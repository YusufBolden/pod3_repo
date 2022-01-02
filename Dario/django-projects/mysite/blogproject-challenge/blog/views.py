from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Post
from .forms import EditorForm

# Create your views here.
def blog(request):
    # get QuerySet object containing posts in descending order of post_id
    posts = Post.objects.all().order_by('-post_id')
    return render(request=request, template_name='blog.html', context={ 'posts': posts })
        
def edit(request, post_id):
    if request.method == 'GET':
        # get Post object by its post_id
        post = Post.objects.get(pk=post_id)
        # get a list of tag_id from ManyRelatedManager object
        tags = []
        for tag in post.tags.all():
            tags.append(tag.tag_id)
        # pre-populate form with values of the post
        form = EditorForm(initial={ 'title': post.title, 'body': post.body, 'tags': tags, 'img_link': post.img_link })
        return render(request=request, template_name='edit.html', context={ 'form': form, 'id': post_id })
    if request.method == 'POST':    
        # capture POST data as EditorForm instance
        form = EditorForm(request.POST)
        # validate form
        if form.is_valid():
            # if form was submitted by clicking Save
            if 'save' in request.POST:
                # get cleaned data from form
                title = form.cleaned_data['title']
                img_link = form.cleaned_data['img_link']
                body = form.cleaned_data['body']
                tags = form.cleaned_data['tags']
                # filter QuerySet object by post_id
                posts = Post.objects.filter(pk=post_id)
                # update QuerySet object with cleaned title, body, img_link
                posts.update(title=title, body=body, img_link=img_link)
                # set cleaned tags to ManyRelatedManager object
                posts[0].tags.set(tags)
            if 'create' in request.POST:
                # get cleaned data from form
                title = form.cleaned_data['title']
                img_link = form.cleaned_data['img_link']
                body = form.cleaned_data['body']
                tags = form.cleaned_data['tags']
                # filter QuerySet object by post_id
                posts = Post.objects.filter(pk=post_id)
                # update QuerySet object with cleaned title, body, img_link
                posts.update(title=title, body=body, img_link=img_link)
                # set cleaned tags to ManyRelatedManager object
                posts[0].tags.set(tags)
            # if form was submitted by clicking Delete
            elif 'delete' in request.POST:
                # filter QuerySet object by post_id and delete it
                Post.objects.filter(pk=post_id).delete()
        # redirect to 'blog/'
        return HttpResponseRedirect(reverse('blog'))