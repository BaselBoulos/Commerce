from django import forms
from .models import AuctionListing, Comment


class AuctionListingForm(forms.ModelForm):
    class Meta:
        model = AuctionListing
        fields = [
            'title',
            'description',
            'start_bid',
            'image',
            'category',
        ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'listing',
            'body',
            'user',
        ]