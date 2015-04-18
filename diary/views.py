import json
import datetime

from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.context_processors import csrf
from django.contrib import messages
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from diary.models import DiaryEntry
from userprofile.models import UserProfile
from django.contrib.auth.models import User

from chartit import DataPool, Chart
from chartit.chartdata import DataPool

# Create your views here.

# day based archive view


@login_required
def diary(request, user_profile_id):
    if DiaryEntry.objects.filter(user_profile_id=user_profile_id, entry_date=datetime.date.today()).exists():
        curr_entry = DiaryEntry.objects.get(user_profile_id=user_profile_id, entry_date=datetime.date.today())
        return render_to_response('diary/diary_detail.html', {'user_profile_id': user_profile_id,
            'username': request.user.username, 'whole_foods': range(1, curr_entry.whole_foods + 1),
            'processed_foods': range(1, curr_entry.processed_foods + 1), 'notes': curr_entry.notes})
    else:
        u = DiaryEntry(user_profile_id=user_profile_id, entry_date=datetime.date.today(), notes="")
        u.save()
        return render_to_response('diary/diary_detail.html', {'user_profile_id': user_profile_id,
                                                            'username': request.user.username})

@login_required
def ajax_get_date(request):
    if request.is_ajax() and request.method == "GET":
        response = {}
        request_date = request.GET["date"]
        request_user = request.GET["userId"]

        if DiaryEntry.objects.filter(user_profile_id=request_user, entry_date=request_date).exists():
            entry = DiaryEntry.objects.get(user_profile_id=request_user, entry_date=request_date)
            response.update({"whole_foods": entry.whole_foods, "processed_foods": entry.processed_foods,
                             "notes": entry.notes})
            return HttpResponse(json.dumps(response), content_type="application/json")
        else:
            new_entry = DiaryEntry(user_profile_id=request_user, entry_date=request_date, notes="")
            new_entry.save()
            response.update({"whole_foods": new_entry.whole_foods, "processed_foods": new_entry.processed_foods,
                             "notes": new_entry.notes})
            return HttpResponse(json.dumps(response), content_type="application/json")
    else:
        return Http404

@login_required
def ajax_post_items(request):
    if request.is_ajax() and request.POST:
        response = {}
        request_date = request.POST["date"]
        request_wf = request.POST["wf_total"]
        request_pf = request.POST["pf_total"]
        request_notes = request.POST["notes_total"]
        request_id = request.user.profile.id
        update_entry = DiaryEntry.objects.get(user_profile_id=request_id, entry_date=request_date)
        update_entry.whole_foods = request_wf
        update_entry.processed_foods = request_pf
        update_entry.notes = request_notes
        update_entry.save()
        response["wf_total"] = update_entry.whole_foods
        response["pf_total"] = update_entry.processed_foods
        response["notes_total"] = update_entry.notes
        return HttpResponse(json.dumps(response), content_type="application/json")
    else:
        return Http404


@login_required
def trends(request, user_profile_id):
    return render_to_response('diary/trends.html', {'user_profile_id': request.user.profile.id})

# @login_required
# def ajax_get_trends(request):
#     if request.is_ajax() and request.method == "GET":
#         response = {}
#         request_date = request.GET["date"]
#         request_user = request.GET["userId"]
#         request_wf = request.GET["wf_total"]
#         request_pf = request.GET["pf_total"]
#
#         if DiaryEntry.objects.filter(user_profile_id=request_user, entry_date=request_date).exists():
#             entry = DiaryEntry.objects.get(user_profile_id=request_user, entry_date=request_date)
#             response.update({"whole_foods": entry.whole_foods, "processed_foods": entry.processed_foods,
#                              "notes": entry.notes})
#             return HttpResponse(json.dumps(response), content_type="application/json")
#         else:
#             new_entry = DiaryEntry(user_profile_id=request_user, entry_date=request_date, notes="")
#             new_entry.save()
#             response.update({"whole_foods": new_entry.whole_foods, "processed_foods": new_entry.processed_foods,
#                              "notes": new_entry.notes})
#             return HttpResponse(json.dumps(response), content_type="application/json")
#     else:
#         return Http404
