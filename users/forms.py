from django import forms

class UpdateProfileForm(forms.Form):
    """Update profile validation form"""
    profile_picture = forms.ImageField()
    web_site = forms.URLField(max_length=200, required=True)
    biography = forms.CharField(max_length=500, required=False)
    phone_number = forms.CharField(max_length=20, required=False)