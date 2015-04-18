from django.shortcuts import render, render_to_response, RequestContext
from django.contrib import messages

from .forms import SignUpForm
from .models import SignUp


# Create your views here.


def home(request):

    form = SignUpForm(request.POST or None)

    if form.is_valid():
        save_post = form.save()
        messages.success(request, "Congrats on getting started with Simply Good!")

    return render_to_response("signup.html", locals(), context_instance=RequestContext(request))
