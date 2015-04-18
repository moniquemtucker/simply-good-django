from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SGRegisterForm(UserCreationForm):
    # password1 = forms.CharField(widget=forms.PasswordInput())
    # password2 = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SGRegisterForm, self).__init__(*args, **kwargs)
        self.fields['email'].label = "Email"
        self.fields.get('username').widget = forms.TextInput(attrs={'placeholder': 'create a username'})
        self.fields.get('email').widget = forms.TextInput(attrs={'placeholder': 'enter your email address'})

    def __unicode__(self):
        return self.username

    def save(self, commit=True):
        user = super(SGRegisterForm, self).save(commit=False)
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        user.set_password(self.cleaned_data['password1'])

        if commit:
            user.save()

            return user