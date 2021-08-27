from django.views.generic import TemplateView, DetailView, FormView
from .forms import PostForm
from .models import Post

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Welcome'] = "Hello and Welcome! This is a Website Made with Django :)"
        context['posts'] = Post.objects.all().order_by('-id')
        return context

class PostDetailView(DetailView):
    template_name = 'detail.html'
    model = Post
    
class AddPostView(FormView):
    template_name = 'new_post.html'
    form_class = PostForm
    success_url = '/' #add a separate html later with home link?

    def form_valid(self, form):
        #creating a new post on the home.html
        new_object = Post.objects.create(
            text=form.cleaned_data['text'],
            image=form.cleaned_data['image']
        )
        return super().form_valid(form)
