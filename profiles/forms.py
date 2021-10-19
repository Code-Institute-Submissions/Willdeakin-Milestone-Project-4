from django import forms
from .widgets import CustomClearableFileInput
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)


    def __init__(self, *args, **kwargs):
        """ Add placeholders and classes """

        super().__init__(self, *args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County or State',
        }

        image = forms.ImageField(label='Image', required=False, 
        widget=CustomClearableFileInput)

        for field in self.fields:
                if field != 'default_country' or 'default_profile_picture':
                    if self.fields[field].required:
                        placeholder = f'{placeholders[field]} *'
                    else:
                        placeholder = placeholders[field]
                    self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].widget.attrs['class'] = 'border-black rounded-0 profile-form-input'
                self.fields[field].label = False