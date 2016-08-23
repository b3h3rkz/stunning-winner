from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.views.generic import ListView
from django import forms
from django.template import RequestContext
import django_excel as excel
from .models import UserData


class UserDataList(ListView):
    model = UserData
    queryset = UserData.objects.all()
    context_object_name = 'user_data'


class Importer(forms.Form):
    file = forms.FileField()


def save_to_db(request):
    if request.method == "POST":
        form = Importer(request.POST, request.FILES)
        if form.is_valid():
            request.FILES['file'].save_to_database(
                            name_columns_by_row=2,
                            model=UserData,
                            mapdict=['first_name', 'last_name', 'age', 'gender', 'address']
            )

            return HttpResponseRedirect(reverse('home:list'))
        else:
            return HttpResponseBadRequest()
    else:
        form = Importer()
    return render_to_response('upload_form.html', {'form': form}, context_instance=RequestContext(request))