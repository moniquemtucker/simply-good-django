from django import forms
from .models import SignUp

from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Submit


# class SignUpForm(forms.ModelForm):
#     class Meta:
#         error_css_class = 'error'
#         required_css_class = 'required'
#         model = SignUp


class SignUpForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-7'
        self.helper.layout = Layout('first_name', 'last_name', 'email', )
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

    first_name = forms.CharField(
        label='First Name:',
        max_length=80,
        required=True,
    )

    last_name = forms.CharField(
        label='Last Name:',
        max_length=80,
        required=True,
    )

    email = forms.CharField(
        label='Email',
        max_length=80,
        required=True,
    )

    class Meta:
        model = SignUp