from django.shortcuts import render,get_object_or_404
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from django.core import serializers
from datetime import date, timedelta
from django.shortcuts import render
from django import forms
from django_bootstrap3_daterangepicker.fields import DateRangeField


# rest风格
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

class TestForm(forms.Form):
    period = DateRangeField()


# Create your views here.

class IndexView(APIView):
    period = DateRangeField()
    template_name = 'index.html'
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request):
        period = None
        form = TestForm(initial={"period": (date.today() - timedelta(days=7), date.today())})
        context = {
            'form': form,
            'period': period,
                   }
        return Response(context)

    def post(self, request):
        period = None
        if request.POST:
            form = TestForm(request.POST)
            if form.is_valid():
                period = form.cleaned_data['period']
            else:
                form = TestForm(initial={"period": (date.today() - timedelta(days=7), date.today())})
        context = {'form': form,
                   'period': period,
                   }
        return Response(context)