from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from .models import Review
from .forms import ReviewForm

class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm # specify the form to be used
    template_name = 'reviews/review.html' # specify the template to be used
    success_url = '/thank_you/' # URL to redirect to after successful form submission
    

def thank_you(request):
    return render( request, 'reviews/thank_you.html', {
        "has_error": False,
    })

class ThankYouView(TemplateView):
    template_name = 'reviews/thank_you.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'This works!'
        return context
    
class ReviewsListView(ListView):
    template_name = 'reviews/review_list.html'
    model = Review
    context_object_name = 'reviews' # name exposed to template - list of reviews

    def get_queryset(self):
        return super().get_queryset()
    
class SingleReviewView(DetailView):
    template_name = 'reviews/single_review.html'
    model = Review

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_review = self.get_object()
        request = self.request
        favorite_id = request.session.get("favorite_review")
        context["is_favorite"] = favorite_id == str(loaded_review.id)
        return context 

class AddFavoriteView(View):
    def post(self, request, pk):
        review_id = request.POST["review_id"]
        request.session['favorite_review'] = review_id
        return HttpResponseRedirect("/reviews/" + review_id)
