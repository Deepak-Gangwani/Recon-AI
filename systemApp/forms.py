# forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
from django.contrib.auth.password_validation import validate_password
from django.utils.translation import gettext as _
from .models import Attendance
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']

    # Custom validation for email
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("This field is required.")
        if '@' not in email or '.' not in email:
            raise forms.ValidationError("Enter a valid email address.")
        return email

    # Custom validation for name
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError("This field is required.")
        return name

    # Custom validation for message
    def clean_message(self):
        message = self.cleaned_data.get('message')
        if not message:
            raise forms.ValidationError("This field is required.")
        return message

class RegistrationForm(forms.Form):
    TRADE_CHOICES = [
    ('', 'Select Regiment'),
    ('Rajput Regiment', 'Rajput Regiment'),
    ('Sikh Regiment', 'Sikh Regiment'),
    ('Gorkha Regiment', 'Gorkha Regiment'),
    ('Jat Regiment', 'Jat Regiment'),
    ('Madras Regiment', 'Madras Regiment'),
    ('Assam Regiment', 'Assam Regiment'),
    ('Maratha Light Infantry', 'Maratha Light Infantry'),
    ('Kumaon Regiment', 'Kumaon Regiment'),
    ('Grenadiers Regiment', 'Grenadiers Regiment'),
    ('Parachute Regiment', 'Parachute Regiment'),
]

    trade = forms.ChoiceField(choices=TRADE_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}), required=True,
                              label='Regiment Name')
    rollNumber = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=True,
                                 label='Cadet ID')
    userName = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=True,
                               label='Full Name')

    # You can add more fields for other form elements if needed

    def clean_trade(self):
        trade = self.cleaned_data.get('trade')
        if trade == '':
            raise forms.ValidationError('Please select a valid trade.')
        return trade


class AttendanceForm(forms.Form):
    TRADE_CHOICES = [
    ('', 'Select Regiment'),
    ('Rajput Regiment', 'Rajput Regiment'),
    ('Sikh Regiment', 'Sikh Regiment'),
    ('Gorkha Regiment', 'Gorkha Regiment'),
    ('Jat Regiment', 'Jat Regiment'),
    ('Madras Regiment', 'Madras Regiment'),
    ('Assam Regiment', 'Assam Regiment'),
    ('Maratha Light Infantry', 'Maratha Light Infantry'),
    ('Kumaon Regiment', 'Kumaon Regiment'),
    ('Grenadiers Regiment', 'Grenadiers Regiment'),
    ('Parachute Regiment', 'Parachute Regiment'),
]

    trade = forms.ChoiceField(choices=TRADE_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}),
                              required=True, label='Regiment Name')
    rollNumber = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=True,
                                 label='Cadet ID')
    captureType = forms.ChoiceField(choices=[('face', 'Face'), ('eye', 'Eye'), ('voice', 'Voice')])
    
                                 


class ShowAttendanceForm(forms.Form):
    TRADE_CHOICES = [
    ('', 'Select Regiment'),
    ('Rajput Regiment', 'Rajput Regiment'),
    ('Sikh Regiment', 'Sikh Regiment'),
    ('Gorkha Regiment', 'Gorkha Regiment'),
    ('Jat Regiment', 'Jat Regiment'),
    ('Madras Regiment', 'Madras Regiment'),
    ('Assam Regiment', 'Assam Regiment'),
    ('Maratha Light Infantry', 'Maratha Light Infantry'),
    ('Kumaon Regiment', 'Kumaon Regiment'),
    ('Grenadiers Regiment', 'Grenadiers Regiment'),
    ('Parachute Regiment', 'Parachute Regiment'),
]

    trade = forms.ChoiceField(choices=TRADE_CHOICES, required=True, label='Regiment Name')
    rollNumber = forms.CharField(max_length=255, required=True, label='Cadet ID')


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label=_("Username"),
        max_length=150,
        help_text=_(""),
        error_messages={
            'unique': _("A user with that username already exists."),
        }
    )
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput,
        help_text=_(""),
        validators=[validate_password],
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput,
        strip=False,
        help_text=_(""),
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(_("The two password fields didn't match."))
        return password2


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        fields = ('username', 'password')
