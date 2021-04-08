from django import forms
from .models import AuctionListing, Comment, Bid


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