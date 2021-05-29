from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'detault_phone_number': 'Phone Number',
            'detault_postcode': 'Postal Code',
            'detault_town_or_city': 'Town or City',
            'detault_street_address1':  'Steet Address 1',
            'detault_street_address2': 'Street Address 2',
            'detault_county': 'County, State or Locality',
        }

        self.fields['detault_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'detault_county':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0 profile-form-input'
            self.fields[field].label = False
