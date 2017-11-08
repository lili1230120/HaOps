from django.shortcuts import render,get_object_or_404
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from django.core import serializers
from app.models import *
from datetime import datetime
from django.db.models import Count
from django.utils import timezone
import datetime

# rest风格
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from app.serializers import *


from datetime import date, timedelta
from django.shortcuts import render
from django import forms
from django_bootstrap3_daterangepicker.fields import DateRangeField

class TestForm(forms.Form):

    date_start = forms.DateField()
    date_end = forms.DateField()


class IndexView(APIView):

    #配置主页模板
    template_name = 'app/index.html'
    renderer_classes = [TemplateHTMLRenderer]

    #########

    style = {'template_pack': 'rest_framework/vertical/'}

    period = TestForm(initial={"date_start": (date.today() - timedelta(days=7)), "date_end": date.today()})

    def get(self,request):
        period = TestForm(initial={"date_start": (date.today() - timedelta(days=7)), "date_end": date.today()})

        # 获取所有运营数据
        context = get_context_data_all()

        context['style'] = self.style

        return Response(context)

    def post(self,request):

        # 获取所有运营数据
        context = get_context_data_all()

        context['style'] = self.style

        return Response(context)
        #return HttpResponse(context, content_type="application/json")




    #
    # 待结构化调整
    # def post(self, request):
    #     period = None
    #     Review_form = OpsReviewSerializer(data=request.data)
    #
    #     form = TestForm(request.POST)
    #     #period = form.cleaned_data['period']
    #
    #     if Review_form.is_valid():
    #         Review_form.save(account='liuqx',user_name='liuqx')
    #         return HttpResponseRedirect('/')
    #     else:
    #         queryset = OpsReview.objects.all()
    #         serializer = OpsReviewSerializer(queryset, many=True)
    #
    #         context = get_context_data_all()
    #     return Response(context)
    #



 #
 # 序列化示例
 #    def post(self, request):
 #        form = SchoolSerializer(data=request.data)
 #        if form.is_valid():
 #            form.save()
 #            return HttpResponseRedirect('/')
 #        else:
 #            queryset = School.objects.all()
 #            serializer = SchoolSerializer(queryset, many=True)
 #            return Response({'data': serializer.data, 'form': form})
 #





class ReviewCreate(APIView):

    renderer_classes = [TemplateHTMLRenderer]


    def get(self, request, *args, **kwargs):
        model = Dcitemdata
        template_name = "app/review_add.html"
        fields = ['title', 'comment']
        context = {
               '1': 1
               }
        return Response(context,template_name=template_name)


class PostView(APIView):

    def get(self,request):
        # 获取所有运营数据
        context = get_context_data_all()

        return Response(context)


    def post(self, request):
        context = dict()

        UTC_FORMAT = "%Y-%m-%dT%H:%M:%S+08:00"

        startDate = datetime.datetime.strptime(request.POST['startDate'], UTC_FORMAT)
        endDate = datetime.datetime.strptime(request.POST['endDate'], UTC_FORMAT)

        context['start'] = startDate
        context['end'] = endDate

        # JiraSys = Dcitemdata.objects.filter(itemno='A01010101').order_by('-itemvalue1')[:5]
        JiraSys = Dcitemdata.objects.filter(itemno__parentno='0301',datadate__range=(startDate, endDate))
        JiraSys_ser = DcitemdataSer(JiraSys, many=True)
        # context['js_JiraSys'] = JSONRenderer().render(JiraSys_ser.data)

        #尝试以 json_JiraSys 更新全局变量
        context['json_JiraSys'] = JSONRenderer().render(JiraSys_ser.data)

        #context = get_context_data_all()
        return Response(context)



class HaOpsView(APIView):

    renderer_classes = (TemplateHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        load_template = request.path.split('/')[-1]
        template_name = 'app/' + load_template

        #获取所有运营数据
        context = get_context_data_all()

    # The template to be loaded as per HaOps.


    # Pick out the html file name from the url. And load that template.
        return Response(context,template_name = template_name)

        #return HttpResponse(template_name.render(context, request))



def get_context_data_all(**kwargs):

    startDate = datetime.date(2017, 11, 1)

    endDate = datetime.date(2017, 11, 1)

    ######### jira分布情况  #######
    #直接查询
    #kwargs['JiraSys'] = Dcitemdata.objects.filter(itemno='0').order_by('-itemvalue1')[:5]

    #关联查询
    kwargs['JiraSys'] = Dcitemdata.objects.filter(itemno__parentno='0301',datadate__range=(startDate, endDate)).order_by('-itemvalue1')[:5]

    #sql查询
    # kwargs['JiraSys'] = Dcitemdata.objects.raw('SELECT * FROM SysCfg_DCItemData WHERE itemno in （ SELECT itemno FROM SysCfg_DCItemData where itemcode="Pr_sys")')

    JiraSys = Dcitemdata.objects.filter(itemno__parentno='0301',datadate__range=(startDate, endDate)).order_by('-itemvalue1')[:5]
    JiraSys_ser = DcitemdataSer(JiraSys, many=True)
    kwargs['json_JiraSys'] = JSONRenderer().render(JiraSys_ser.data)



    # 获取全部OpsCal（页顶 指标）数据
    kwargs['opsCal']  = Dcitemdata.objects.filter(itemno__parentno='0301',datadate__range=(startDate, endDate)).order_by('-id')[:6]

    # 产能统计
    kwargs['capacity'] = Dcitemdata.objects.filter(itemno__parentno='0301',datadate__range=(startDate, endDate)).order_by('-id')[:5]

    # 重点反馈
    kwargs['opsReview'] = Dcitemdata.objects.filter(itemno__parentno='0301',datadate__range=(startDate, endDate)).order_by('-id')[:7]

    # 地区统计
    kwargs['jiraArea'] = Dcitemdata.objects.filter(itemno__parentno='0301',datadate__range=(startDate, endDate)).order_by('-id')[:6]

    # 生产发布计划
    kwargs['ReleasePlan'] = Dcitemdata.objects.filter(itemno__parentno='0301',datadate__range=(startDate, endDate)).order_by('-id')[:7]

    # 机构考核数据
    kwargs['opsExamineUser'] = Dcitemdata.objects.filter(itemno__parentno='0301',datadate__range=(startDate, endDate)).order_by('-id')[:5]

    ''' 待结构化
    
    # test
    # kwargs['todo'] = Todo.objects.get(id='2')
    
    
    # 获取全部OpsCal（页顶 指标）数据
    #kwargs['opsCal']  = OpsCal.objects.all
    #serializers = OpsCalSerializer(opsCal, many=True)

    # 通过sql查询OpsCal数据
    #kwargs['opsCal'] = Dcitemdata.objects.raw(
    #    'SELECT * FROM SysCfg_DCItemData WHERE itemno < 7')
    
    # 机构考核数据
    kwargs['opsExamine'] = OpsExamine.objects.order_by('-d_sum')[:10]

    # 机构考核数据
    kwargs['opsExamineUser'] = OpsExamine.objects.order_by('-d_sum')[:5]

    # 标签统计
    kwargs['jiraTag'] = JiraSysDtl.objects.filter(jira_type = 'pr').values('tag').annotate(total=Count('tag') * 15).order_by('total')

    # 产能统计
    kwargs['capacity'] = OpsCapacity.objects.filter(input_date__startswith=datetime(2017, 9, 20)).order_by('-num')[:5]

    # 地区统计
    kwargs['jiraArea'] = JiraSysDtl.objects.filter(jira_type = 'pr').values('area').annotate(total=Count('area') * 15).order_by('-total')

    #时间筛选
    kwargs['form'] = TestForm(initial={"period": (date.today() - timedelta(days=7), date.today())})

    #js测试
    kwargs['results'] = {'name': 123, 'name1': 456, 'sysname': ['单证', '理赔'], "items":
        [{"name": "name1", "sector": "sector1"},
         {"name": "name2", "sector": "sector2"},
         {"name": "name3", "sector": "sector3"}]}

    #test
    kwargs['iosper'] = OpsCal.objects.get(id='2')

    #重点反馈
    kwargs['opsReview'] = OpsReview.objects.all().order_by('-created_at')
    opsReview = OpsReview.objects.all().order_by('-created_at')
    kwargs['opsReview_ser'] = OpsReviewSerializer(opsReview, many=True)

    Review_form = OpsReviewSerializer()

    kwargs['Review_form'] = Review_form

    #生产发布计划
    kwargs['ReleasePlan'] = JiraSysDtl.objects.filter(jira_type = 'publish').order_by('update_date')
'''
    return kwargs
    # The template to be loaded as per HaOps.
    # All resource paths for HaOps end in .html.

