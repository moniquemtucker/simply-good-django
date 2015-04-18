from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required

from forms import UserProfileForm

import json
from django.http import HttpResponse
from .models import UserProfile
# Create your views here.

@login_required
def user_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/diary/%s' % request.user.profile.id)
    else:
        user = request.user
        profile = user.profile
        form = UserProfileForm(instance=profile)

    args = {}
    args.update(csrf(request))

    args['form'] = form
    args['username'] = request.user.username
    args['user_profile_id'] = request.user.profile.id
    return render_to_response('profile.html', args)


# def list_api(request):
#     item_list = UserProfile.objects.all()
#     output_list = []
#
#     for item in item_list:
#         output_item = {}
#         output_item["system_id"] = item.id
#         output_item["first_name"] = item.first_name
#         output_list.append(output_item)
#
#     return HttpResponse(
#         json.dumps(output_list),
#         content_type="application/json"
#     )