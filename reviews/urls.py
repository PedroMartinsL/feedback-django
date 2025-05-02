from django.urls import path
from . import views

urlpatterns = [
    path("", views.ReviewView.as_view(), name="review"),
    path("thank_you/", views.ThankYouView.as_view(), name="thank_you"),
    path("reviews", views.ReviewsListView.as_view(), name="reviews_list"),
    path("revies/<int:review_id>/", views.SingleReviewView.as_view(), name="single_review"),
]
