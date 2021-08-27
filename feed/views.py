from django.contrib import messages
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

    #creating a method inside the class to make request exist for success message
    #messages need to be enabled in the base.html because it should be in all pages
    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        #creating a new post on the home.html
        new_object = Post.objects.create(
            text=form.cleaned_data['text'],
            image=form.cleaned_data['image']
        )
        messages.add_message(self.request, messages.SUCCESS, 'You have successfully submitted your post!')
        return super().form_valid(form)
