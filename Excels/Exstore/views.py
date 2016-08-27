from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.http import HttpResponseBadRequest, HttpResponseRedirect, HttpResponse
from django.views.generic import ListView
from django.template import RequestContext
import django_excel as excel
import pyexcel_xls
import pyexcel_xlsx
from .models import UserData, Log
from .forms import Importer
from djcelery import celery
from .tasks import *



class UserDataList(ListView):
    model = UserData
    queryset = UserData.objects.all()
    context_object_name = 'user_data'


class LogView(ListView):
    model = Log
    queryset = Log.objects.all()
    context_object_name = 'logs'


def save_to_db(request):
    if request.method == "POST":
        form = Importer(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            import_data.delay(file)
            file_name = request.FILES['file'].name
            new_log = Log(action='file_upload', message=file_name)
            new_log.save()
            return HttpResponseRedirect(reverse('app:list'))
        else:
            return HttpResponseBadRequest()
    else:
        form = Importer()
    return render_to_response('Exstore/upload_form.html', {'form': form}, context_instance=RequestContext(request))


def test_celery(request):
	result = tasks.sleeptask.delay(10)
	result_one = tasks.sleeptask.delay(10)
	result_two = tasks.sleeptask.delay(10)
	return HttpResponse(result.task_id)