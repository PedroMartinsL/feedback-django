from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here. 
from .forms import ReviewForm

def review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        
        if form.is_valid():
            print(form.cleaned_data)
        return HttpResponseRedirect('/thank_you/')
    else:
        form = ReviewForm()

    return render(request, 'reviews/review.html', {
        "form": form,
    })

def thank_you(request):
    # This view can be used to display a thank you message after form submission
    return render( request, 'reviews/thank_you.html', {
        "has_error": False,
    })