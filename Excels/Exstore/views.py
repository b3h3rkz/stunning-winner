from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.views.generic import ListView
from django import forms
from django.template import RequestContext
import django_excel as excel
import pyexcel_xls
import pyexcel_xlsx
from .models import UserData


class UserDataList(ListView):
    model = UserData
    queryset = UserData.objects.all()
    context_object_name = 'user_data'


class Importer(forms.Form):
    file = forms.FileField()

    # def clean(self):
    #     try:
    #         UserData.objects.get(
    #                             first_name=self.cleaned_data['first_name'],
    #                             last_name=self.cleaned_data['last_name'],
    #                             age=self.cleaned_data['age'],
    #                             gender=self.cleaned_data['gender'],
    #                             address=self.cleaned_data['address'])
    #         raise forms.ValidationError("Exists already!")
    #     except UserData.DoesNotExist:
    #         pass
    #     return self.cleaned_data


def save_to_db(request):
    if request.method == "POST":
        form = Importer(request.POST, request.FILES)
        if form.is_valid():
            request.FILES['file'].save_to_database(
                name_columns_by_row=2,
                model=UserData,
                mapdict=['first_name', 'last_name', 'age', 'gender', 'address'])
            return HttpResponseRedirect(reverse('list'))
        else:
            return HttpResponseBadRequest()
    else:
        form = Importer()
    return render_to_response('Exstore/upload_form.html', {'form': form}, context_instance=RequestContext(request))