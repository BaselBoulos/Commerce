from django import forms
from .models import AuctionListing, Comment, Bid, Category


category_choices = Category.objects.all().values_list('name', 'name')
choice_list = []
for item in category_choices:
    choice_list.append(item)


class AuctionListingForm(forms.ModelForm):
    class Meta:
        model = AuctionListing
        fields = ['title', 'description', 'start_bid', 'image', 'category']
        widgets = {
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        labels = {
            "body": "Comment"
        }
        fields = [
            'body',
        ]


class BidForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = [
            'price',
        ]