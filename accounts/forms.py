from django import forms

from .models import Account


class RegistrationForms(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Create password',
               'class': 'form-control',
               }
    ))
    
    confirm_password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Confirm password',
               'class': 'form-control',
               }
    ))
    
    
    
    
    class Meta:
        model = Account
        fields =   ['first_name', 'last_name', 'email', 'phone_number', 'password'] 
        
    def __init__(self, *args, **kwargs):
        super(RegistrationForms, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter Last Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter Email'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Enter Phone Number'
        
        
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            
            
    def clean(self):
        cleaned_data = super(RegistrationForms, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match!")

        return cleaned_data


#----------------------------------------------------------------------------------------------
                            # modern way of code by use ChatGPT
#---------------------------------------------------------------------------------------------

# class RegistrationForms(forms.ModelForm):
#     # Password field
#     password = forms.CharField(
#         widget=forms.PasswordInput(
#             attrs={
#                 'placeholder': 'Create Password',
#                 'class': 'form-control',
#             }
#         )
#     )

#     # Confirm Password field (not stored in the database)
#     confirm_password = forms.CharField(
#         widget=forms.PasswordInput(
#             attrs={
#                 'placeholder': 'Confirm Password',
#                 'class': 'form-control',
#             }
#         )
#     )

#     class Meta:
#         model = Account
#         fields = [
#             'first_name',
#             'last_name',
#             'email',
#             'phone_number',
#             'password',
#         ]

#     def __init__(self, *args, **kwargs):
#         # Call the parent ModelForm constructor
#         super().__init__(*args, **kwargs)

#         # Add placeholder text
#         self.fields['first_name'].widget.attrs['placeholder'] = 'Enter First Name'
#         self.fields['last_name'].widget.attrs['placeholder'] = 'Enter Last Name'
#         self.fields['email'].widget.attrs['placeholder'] = 'Enter Email Address'
#         self.fields['phone_number'].widget.attrs['placeholder'] = 'Enter Phone Number'

#         # Apply Bootstrap class to every field
#         for field in self.fields.values():
#             field.widget.attrs['class'] = 'form-control'

#     def clean(self):
#         # Run the default ModelForm validation first
#         cleaned_data = super().clean()

#         # Get password values
#         password = cleaned_data.get('password')
#         confirm_password = cleaned_data.get('confirm_password')

#         # Check whether both passwords match
#         if password and confirm_password and password != confirm_password:
#             raise forms.ValidationError(
#                 "Passwords do not match!"
#             )

#         return cleaned_data
