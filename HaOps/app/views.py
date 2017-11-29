from django.shortcuts import render,get_object_or_404
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from django.core import serializers
from app.models import *
from app.serializers import *

from datetime import datetime
from django.db.models import Count
from django.utils import timezone
import datetime
import json

# rest风格
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response


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




class SysDetailView(APIView):

    renderer_classes = [TemplateHTMLRenderer]


    def get(self, request, *args, **kwargs):
        systype = request.path.split('/')[-1]
        template_name = "app/sysdetail.html"
        fields = ['title', 'comment']

        context = get_context_data_all()

        return Response(context,template_name=template_name)


class PostView(APIView):

    def get(self,request):
        # 获取所有运营数据
        context = get_context_data_all()

        return Response(context)


    # def post(self, request):
    #     context = dict()
    #
    #     UTC_FORMAT = "%Y-%m-%dT%H:%M:%S+08:00"
    #
    #     startDate = datetime.datetime.strptime(request.POST['startDate'], UTC_FORMAT)
    #     endDate = datetime.datetime.strptime(request.POST['endDate'], UTC_FORMAT)
    #
    #     context['start'] = startDate
    #     context['end'] = endDate
    #
    #     # JiraSys = Dcitemdata.objects.filter(itemno='A01010101').order_by('-itemvalue1')[:5]
    #     JiraSys = Dcitemdata.objects.filter(itemno__itemno='020111',datadate__range=(startDate, endDate))
    #     JiraSys_ser = DcitemdataSer(JiraSys, many=True)
    #     # context['js_JiraSys'] = JSONRenderer().render(JiraSys_ser.data)
    #
    #     #尝试以 json_JiraSys 更新全局变量
    #     context['json_JiraSys'] = JSONRenderer().render(JiraSys_ser.data)
    #
    #     #context = get_context_data_all()
    #     return Response(context)
    def post(self, request):
        context = dict()

        UTC_FORMAT = "%Y-%m-%dT%H:%M:%S+08:00"

        startDate = datetime.datetime.strptime(request.POST['startDate'], UTC_FORMAT)
        endDate = datetime.datetime.strptime(request.POST['endDate'], UTC_FORMAT)

        context['start'] = startDate
        context['end'] = endDate

        # 承保jira趋势
        JiraNBZ = Dcitemdata.objects.filter(itemno__itemno='020101', datadate__range=(startDate, endDate)).order_by(
            'datadate')
        JiraNBZ_ser = DcitemdataSer(JiraNBZ, many=True)
        context['json_JiraNBZ'] = JSONRenderer().render(JiraNBZ_ser.data)

        # 理赔jira趋势
        JiraCLM = Dcitemdata.objects.filter(itemno__itemno='020116', datadate__range=(startDate, endDate)).order_by(
            'datadate')
        JiraCLM_ser = DcitemdataSer(JiraCLM, many=True)
        context['json_JiraCLM'] = JSONRenderer().render(JiraCLM_ser.data)

        # 财务jira趋势
        JiraFIN = Dcitemdata.objects.filter(itemno__itemno='020128', datadate__range=(startDate, endDate)).order_by(
            'datadate')
        JiraFIN_ser = DcitemdataSer(JiraFIN, many=True)
        context['json_JiraFIN'] = JSONRenderer().render(JiraFIN_ser.data)

        #context = JSONRenderer().render(context)

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



def get_context_data_all(startDate = datetime.date(2017, 4, 1) , endDate = datetime.date(2017, 7, 6),**kwargs):

    OstartDate = datetime.date(2017, 9, 1)
    OendDate = datetime.date(2017,11, 1)

    startMonth = '2017-01'

    '''
   生产jira趋势查询

    '''
    ##承保趋势
    nbzJira =  Dcitemdata.objects.raw("""
 SELECT dataid,itemno,itemname,datadate ,itemvalue1 ,itemvalue2 ,itemvalue3  FROM
(select a.dataid,a.itemno,pkg_operatefunc_dcshow.GetFactorNames(a.dataid,'-') as itemname,a.datadate ,a.itemvalue1 ,a.itemvalue2 ,a.itemvalue3
from syscfg_dcitemdata a
where a.itemno = 'B012001' and length(a.datadate) = 7 and a.datadate > %s )
where itemname = '承保-总部运维'
order by datadate,dataid""" ,[startMonth])
    nbzJira_ser = DcitemdataSer(nbzJira, many=True)

    kwargs['nbzJira'] = nbzJira
    kwargs['js_nbzJira'] = JSONRenderer().render(nbzJira_ser.data)

    ##理赔趋势
    clmJira = Dcitemdata.objects.raw("""
     SELECT dataid,itemno,itemname,datadate ,itemvalue1 ,itemvalue2 ,itemvalue3  FROM
    (select a.dataid,a.itemno,pkg_operatefunc_dcshow.GetFactorNames(a.dataid,'-') as itemname,a.datadate ,a.itemvalue1 ,a.itemvalue2 ,a.itemvalue3
    from syscfg_dcitemdata a
    where a.itemno = 'B012001' and length(a.datadate) = 7 and a.datadate > %s )
    where itemname = '理赔-总部运维'
    order by datadate,dataid""", [startMonth])
    clmJira_ser = DcitemdataSer(clmJira, many=True)
    kwargs['js_clmJira'] = JSONRenderer().render(clmJira_ser.data)

    ##收付趋势
    finJira = Dcitemdata.objects.raw("""
     SELECT dataid,itemno,itemname,datadate ,itemvalue1 ,itemvalue2 ,itemvalue3  FROM
    (select a.dataid,a.itemno,pkg_operatefunc_dcshow.GetFactorNames(a.dataid,'-') as itemname,a.datadate ,a.itemvalue1 ,a.itemvalue2 ,a.itemvalue3
    from syscfg_dcitemdata a
    where a.itemno = 'B012001' and length(a.datadate) = 7 and a.datadate > %s )
    where itemname = '收付-总部运维'
    order by datadate,dataid""", [startMonth])
    finJira_ser = DcitemdataSer(finJira, many=True)
    kwargs['js_finJira'] = JSONRenderer().render(finJira_ser.data)





    ##信保趋势
    xbJira = Dcitemdata.objects.raw("""
     SELECT dataid,itemno,itemname,datadate ,itemvalue1 ,itemvalue2 ,itemvalue3  FROM
    (select a.dataid,a.itemno,pkg_operatefunc_dcshow.GetFactorNames(a.dataid,'-') as itemname,a.datadate ,a.itemvalue1 ,a.itemvalue2 ,a.itemvalue3
    from syscfg_dcitemdata a
    where a.itemno = 'B012001' and length(a.datadate) = 7 and a.datadate > %s )
    where itemname = '信保-总部运维'
    order by datadate,dataid""", [startMonth])
    xbJira_ser = DcitemdataSer(xbJira, many=True)
    kwargs['js_xbJira'] = JSONRenderer().render(xbJira_ser.data)

    ##周边趋势
    zbJira = Dcitemdata.objects.raw("""
     SELECT dataid,itemno,itemname,datadate ,itemvalue1 ,itemvalue2 ,itemvalue3  FROM
    (select a.dataid,a.itemno,pkg_operatefunc_dcshow.GetFactorNames(a.dataid,'-') as itemname,a.datadate ,a.itemvalue1 ,a.itemvalue2 ,a.itemvalue3
    from syscfg_dcitemdata a
    where a.itemno = 'B012001' and length(a.datadate) = 7 and a.datadate > %s )
    where itemname = '周边-总部运维'
    order by datadate,dataid""", [startMonth])
    zbJira_ser = DcitemdataSer(zbJira, many=True)
    kwargs['js_zbJira'] = JSONRenderer().render(zbJira_ser.data)

    # 地区统计-all
    AreaCal = Dcitemdata.objects.raw("""
         SELECT dataid,itemno,itemname,datadate ,itemvalue1 ,itemvalue2 ,itemvalue3  FROM
        (select a.dataid,a.itemno,pkg_operatefunc_dcshow.GetFactorNames(a.dataid,'-') as itemname,a.datadate ,a.itemvalue1 ,a.itemvalue2 ,a.itemvalue3
        from syscfg_dcitemdata a
        where a.itemno = 'A01001' and length(a.datadate) = 7 and a.datadate > %s )
        where rownum < 6
        order by datadate,dataid  """, [startMonth])
    AreaCal_ser = DcitemdataSer(AreaCal, many=True)
    kwargs['AreaCal'] = AreaCal
    kwargs['js_AreaCal'] = JSONRenderer().render(zbJira_ser.data)


    '''

    '''

    '''  待清理
    ######### jira分布情况  #######
    #直接查询
    #kwargs['JiraSys'] = Dcitemdata.objects.filter(itemno='0').order_by('-itemvalue1')[:5]

    #关联查询
    kwargs['JiraSys'] = Dcitemdata.objects.filter(itemno__parentno='0301',datadate__range=(OendDate, OendDate)).order_by('-itemvalue1')[:5]

    #sql查询
    # kwargs['JiraSys'] = Dcitemdata.objects.raw('SELECT * FROM SysCfg_DCItemData WHERE itemno in （ SELECT itemno FROM SysCfg_DCItemData where itemcode="Pr_sys")')

    JiraSys = Dcitemdata.objects.filter(itemno__parentno='0301',datadate__range=(OendDate, OendDate)).order_by('-itemvalue1')[:5]
    JiraSys_ser = DcitemdataSer(JiraSys, many=True)
    kwargs['json_JiraSys'] = JSONRenderer().render(JiraSys_ser.data)


    #承保jira趋势
    JiraNBZ = Dcitemdata.objects.filter(itemno__itemno='020101', datadate__range=(startDate, endDate)).order_by('datadate')
    JiraNBZ_ser = DcitemdataSer(JiraNBZ, many=True)
    kwargs['json_JiraNBZ'] = JSONRenderer().render(JiraNBZ_ser.data)

    # 理赔jira趋势
    JiraCLM = Dcitemdata.objects.filter(itemno__itemno='020116', datadate__range=(startDate, endDate)).order_by(
        'datadate')
    JiraCLM_ser = DcitemdataSer(JiraCLM, many=True)
    kwargs['json_JiraCLM'] = JSONRenderer().render(JiraCLM_ser.data)

    # 财务jira趋势
    JiraFIN = Dcitemdata.objects.filter(itemno__itemno='020128', datadate__range=(startDate, endDate)).order_by(
        'datadate')
    JiraFin_ser = DcitemdataSer(JiraFIN, many=True)
    kwargs['json_JiraFIN'] = JSONRenderer().render(JiraFin_ser.data)

    # 二线支持
    kwargs['JiraSPT'] = Dcitemdata.objects.filter(itemno__parentno='0303', datadate__range=(OstartDate, OstartDate)).order_by(
        'datadate')
    # JiraSPT_ser = DcitemdataSer(JiraSPT, many=True)
    # kwargs['JiraSPT'] = JSONRenderer().render(JiraSPT_ser.data)

    # 问题趋势统计
    kwargs['JiraType'] = Dcitemdata.objects.filter(itemno__itemno='0303',
                                                  datadate__range=(startDate, endDate)).order_by(
        'datadate')

    # # 需求缺陷
    # JiraREQ = Dcitemdata.objects.filter(itemno__itemno='030302', datadate__range=(OstartDate, OendDate)).order_by(
    #     'datadate')
    # JiraREQ_ser = DcitemdataSer(JiraREQ, many=True)
    # kwargs['json_JiraREQ'] = JSONRenderer().render(JiraREQ_ser.data)
    #
    # # 超期未完成
    # JiraOUT = Dcitemdata.objects.filter(itemno__itemno='030303', datadate__range=(OstartDate, OendDate)).order_by(
    #     'datadate')
    # JiraOUT_ser = DcitemdataSer(JiraOUT, many=True)
    # kwargs['json_JiraOUT'] = JSONRenderer().render(JiraOUT_ser.data)


    # 获取标签数据
    kwargs['opsTag'] = Dcitemdata.objects.filter(itemno__parentno='0202',
                                                 datadate__range=(startDate, endDate)).order_by('-datadate')[:3]

    # 获取KPI数据
    kwargs['opsKPI'] = Dcitemdata.objects.filter(itemno__parentno='0202',
                                                 datadate__range=(OstartDate, OstartDate)).order_by('-itemvalue1')[:6]

    # 获取承保KPI数据
    kwargs['NBZ_KPI'] = Dcitemdata.objects.filter(itemno__parentno ='0201',
                                                  datadate__range=(startDate, endDate)).order_by('-datadate')

    # 获取理赔KPI数据
    kwargs['CLM_KPI'] = Dcitemdata.objects.filter(itemno__parentno='0202',
                                                  datadate__range=(startDate, endDate)).order_by('-datadate')


    # 获取MQ数据
    kwargs['opsMQ'] = Dcitemdata.objects.filter(itemno__parentno='0206',
                                                 datadate__range=(OstartDate, OstartDate)).order_by('-datadate')[:6]

    # 获取MQ数据-all
    kwargs['MQ_KPI'] = Dcitemdata.objects.filter(itemno__parentno='0206',
                                                datadate__range=(startDate, OendDate)).order_by('-datadate')

    # 获取全部OpsCal（页顶 指标）数据
    kwargs['opsCal']  = Dcitemdata.objects.filter(itemno__parentno='0104',datadate__range=(OstartDate,OstartDate)).order_by('itemno')[:6]

    # 产能统计
    kwargs['capacity'] = Dcitemdata.objects.filter(itemno__itemno='020111',datadate__range=(startDate, endDate)).order_by('-itemvalue1')[:5]

    # 重点反馈
    kwargs['opsReview'] = Dcitemdata.objects.filter(itemno__itemno='020111',datadate__range=(startDate, endDate)).order_by('-itemvalue1')[:7]

    # 地区统计
    kwargs['jiraArea'] = Dcitemdata.objects.filter(itemno__parentno='0302',datadate__range=(startDate, endDate)).order_by('-itemvalue1')[:5]

    # 地区统计-all
    AreaAll = Dcitemdata.objects.filter(itemno__parentno='0302', datadate__range=(OendDate, OendDate)).order_by(
        'datadate')
    AreaAll_ser = DcitemdataSer(AreaAll, many=True)
    kwargs['json_AreaAll'] = JSONRenderer().render(AreaAll_ser.data)

    # 生产发布计划
    kwargs['ReleasePlan'] = Dcitemdata.objects.filter(itemno__parentno='0304',datadate__range=(startDate, endDate)).order_by('-itemvalue1')[:7]

    # 机构考核数据
    kwargs['opsExamineUser'] = Dcitemdata.objects.filter(itemno__itemno='020111',datadate__range=(startDate, endDate)).order_by('-itemvalue1')[:5]
    '''


    return kwargs


