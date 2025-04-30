from django import forms

class ReviewForm(forms.Form):
    user_name = forms.CharField(label="Your name", max_length=100, error_messages={
        'required': 'Your name must not be empty',
        'max_length': 'Name is too long'
    })
    review_text = forms.CharField(label="Your FeedBack", widget=forms.Textarea, max_length=200)
    rating = forms.IntegerField(label="Your rating", min_value=1, max_value=5)