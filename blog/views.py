from django.shortcuts import render,redirect , HttpResponse
from blog.models import Post,Comment
# Create your views here.
from blog.templatetags import extras
def bloghome(request):
    posts = Post.objects.all()[::-1]
    param = {'posts':posts}
    return render(request,'blog/bloghome.html',param)
def blodpost(request,slug):
    post = Post.objects.get(title=slug)
    comment = Comment.objects.filter(post=post,parent=None)
    reply = Comment.objects.filter(post=post).exclude(parent=None)
    replydict = {}
    for rep in reply:
        if rep.parent.pk not in replydict.keys():
            replydict[rep.parent.pk] = [rep]
        else:
            replydict[rep.parent.pk].append(rep)

    param = {'post':post,'comments':comment,'replies':replydict}
    return render(request,'blog/blogpost.html',param)
def PostComment(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        parentpost = request.POST.get('parentpost')
        post = Post.objects.get(id=request.POST.get('post')) 
        print(parentpost)   
        if parentpost == "":
            c = Comment(comments=comment,user=request.user,post=post)
        else:
            print("its a child")
            parentcmt = Comment.objects.get(pk=parentpost) 
            c = Comment(comments=comment,user=request.user,post=post,parent=parentcmt)
            
        c.save()    

        return redirect(f'/blog/{post}')
    else:
        return HttpResponse("404 - page not found")