# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from fusionapp.models import *

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'last_name','first_name','phonenumber')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = '__all__'

# class AlbumForm(forms.ModelForm):
#     class Meta:
#         model = Album
#         fields = '__all__'

class AlbumForm(forms.Form):
    NONE = 'None'
    JAN = 'January'
    FEB = 'February'
    MAR = 'March'
    APR = 'April'
    MAY = 'May'
    JUN = 'June'
    JUL = 'July'
    AUG = 'August'
    SEP = 'September'
    OCT = 'October'
    NOV = 'November'
    DEC = 'December'
    MONTHS = [
        (NONE,'None'),
        (JAN,'January'),
        (FEB,'February'),
        (MAR,'March'),
        (APR,'April'),
        (MAY,'May'),
        (JUN,'June'),
        (JUL,'July'),
        (AUG,'August'),
        (SEP,'September'),
        (OCT,'October'),
        (NOV,'November'),
        (DEC,'December'),
    ]
    
    # artist = forms.ModelChoiceField(
    #     queryset=Artist.objects.filter().values('artist_name'),
    #     required=True,
    # )
  
    artist = forms.TypedChoiceField(
        choices=[('None','----')] + [('artist_name', choice['artist_name']) for choice in Artist.objects.filter().values('artist_name')],
        required=False,
        empty_value=None,
    )
    artist_if_not_in_list = forms.CharField(
        label="Or Type in Artist Name",
        max_length=250,
        widget=forms.TextInput(attrs={
            'placeholder': ''
        }),
        required=False
    )
    name = forms.CharField(
        label="Name",
        max_length=250,
        widget=forms.TextInput(attrs={
            'placeholder': ''
        }),
        required=True
    )
    genre = forms.CharField(
        label="Genre",
        max_length=150,
        widget=forms.TextInput(attrs={
            'placeholder': ''
        }),
        required=True
    )
    month = forms.ChoiceField(
        choices=MONTHS,
        required=True
    )
    year = forms.IntegerField(
        label="Year",
        min_value=0000,
        # max_value=99999,
        widget=forms.NumberInput(attrs={
            'placeholder': ''
        }),
        required=True
    )

class PlatformForm(forms.ModelForm):
    class Meta:
        model = Platform
        fields = '__all__'

class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = '__all__'

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = '__all__'
        