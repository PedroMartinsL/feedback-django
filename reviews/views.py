from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView

from .models import Review

class ReviewView(View):
    def get(self, request):
        form = ReviewForm()
        return render(request, 'reviews/review.html', {'form': form})

    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thank_you/')
        return render(request, 'reviews/review.html', {'form': form})

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
    
class SingleReviewView(TemplateView):
    template_name = 'reviews/single_review.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        review_id = self.kwargs.get('review_id')
        context['review'] = Review.objects.get(id=review_id)
        return context