from django import forms
from .models import Review

# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label="Your name", max_length=100, error_messages={
#         'required': 'Your name must not be empty',
#         'max_length': 'Name is too long'
#     })
#     review_text = forms.CharField(label="Your FeedBack", widget=forms.Textarea, max_length=200)
#     rating = forms.IntegerField(label="Your rating", min_value=1, max_value=5)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        # fields = ['user_name', 'review_text', 'rating']
        #exclude = ['owner_comment']
        fields = '__all__'
        labels = {
            'user_name': 'Your name',
            'review_text': 'Your FeedBack',
            'rating': 'Your rating',
        }
        error_messages = {
            'user_name': {
                'required': 'Your name must not be empty',
                'max_length': 'Name is too long'
            },
            'review_text': {
                'required': 'Your feedback must not be empty',
                'max_length': 'Feedback is too long'
            },
            'rating': {
                'required': 'Rating is required',
                'min_value': 'Rating must be at least 1',
                'max_value': 'Rating cannot exceed 5'
            }
        }

        