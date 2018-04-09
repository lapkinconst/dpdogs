from django.shortcuts import render, render_to_response, get_object_or_404, HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from blog.forms import CommentForm, ContactForm
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.models import *
from django.core.mail import send_mail, BadHeaderError
# from django.contrib import auth


class PostList(ListView):
    template_name = 'blog/post_list.html'
    model = Post
    context_object_name = 'posts'

    def get_queryset(self):
        posts = Post.objects.filter(status=True)
        posts = posts.order_by('-published_date')
        paginator = Paginator(posts, 5)
        page = self.request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        return posts


class PostView(DetailView):
    model = Post
    context_object_name = 'post'

    def dispatch(self, request, *args, **kwargs):
        post = get_object_or_404(Post, slug=self.kwargs['slug'])
        comment = Comment.objects.filter(post=post, moder=True)
        if request.method == "POST":
            form = CommentForm(request.POST)
            if form.is_valid():
                comm = form.save(commit=False)
                comm.author = request.user
                comm.post = post
                comm.save()
        else:
            form = CommentForm()
        return render(request, 'blog/post_detail.html', {"post": post, "form": form, "comment": comment})


class CategoryPostsList(ListView):
    template_name = 'blog/category_post_list.html'
    model = Category
    context_object_name = 'category'

    def get(self, request, *args, **kwargs):
        context = {}
        category = get_object_or_404(Category, slug=self.kwargs['slug'])

        context['category'] = category
        return render_to_response(template_name=self.template_name, context=context)


# def category_post_list(request, slug):
#     category = Category.objects.select_related().get(slug=slug)
#     posts = category.post_set.all()
#     return render(request, 'blog/category_post_list.html', {'posts': posts, 'category': category})


def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            sender = form.cleaned_data['sender']
            message = form.cleaned_data['message']
            copy = form.cleaned_data['copy']
            recepients = ['constlapkin@gmail.com']

            if copy:
                recepients.append(sender)
            try:
                send_mail(subject, message, 'constlapkin@gmail.com', recepients)
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return HttpResponseRedirect('/thanks/')
    else:
        form = ContactForm()

    return render(request, 'blog/feedback.html', {'form': form})
    #, 'username': auth.get_uset(request).username})


def thanks(request):
    return render(request, 'blog/thanks.html', {})


def handler404(request):
    response = render_to_response('blog/404.html', {}, RequestContext(request))
    response.status_code = 404
    return response
