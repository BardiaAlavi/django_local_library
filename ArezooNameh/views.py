from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView,  ListView
from Posts.models import Post
from django.views import generic
from django.http import Http404
from django.contrib.auth import get_user_model
User = get_user_model()
from django.shortcuts import get_object_or_404

class HomePage(TemplateView):
    template_name = 'index.html'
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("test"))
        return super().get(request, *args, **kwargs)
class ThanksPage(TemplateView):
    template_name = 'thanks.html'
class TestPage(ListView):
    model=Post
    template_name = 'test.html'
    queryset = Post.objects.order_by('-created_at')
    
    context_object_name = 'book_list'
