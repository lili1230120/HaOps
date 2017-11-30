from app.models import *
from app.serializers import *
from django.core import serializers
from rest_framework.renderers import JSONRenderer

import datetime


'''
定义通用查询模板
'''
def sql_raw(itemno,itemfilter):

    itemname = Dcitemdata.objects.raw("""

SELECT a.dataid,pkg_operatefunc_dcshow.GetFactorNames(a.dataid) itemname,a.datadate,a.itemvalue1,a.itemvalue2,a.itemvalue3
from syscfg_dcitemdata a where a.itemno = %s
and pkg_operatefunc_dcshow.IsMonthDate(a.datadate) = 1 and a.datadate >= '2017-01'
and pkg_operatefunc_dcshow.CheckFactorList(a.dataid,%s) = 1  """,[itemno,itemfilter])
    itemname_ser = DcitemdataSer(itemname, many=True)
    json = JSONRenderer().render(itemname_ser.data)

    return json



def get_context_data_all(startDate=datetime.date(2017, 4, 1), endDate=datetime.date(2017, 7, 6), **kwargs):
    OstartDate = datetime.date(2017, 9, 1)
    OendDate = datetime.date(2017, 11, 1)

    startMonth = '2017-01'

    '''
   生产jira趋势查询

    '''
    ##承保趋势
    kwargs['js_Pr_nbz'] = sql_raw( 'B010001','P0001:11')


    ##理赔趋势
    kwargs['js_Pr_clm'] = sql_raw( 'B010001','P0001:12')

    ##收付趋势
    kwargs['js_Pr_fin'] = sql_raw( 'B010001','P0001:13')

    ##信保趋势
    kwargs['js_Pr_xb'] = sql_raw( 'B010001','P0001:14')

    ##周边趋势
    kwargs['js_Pr_zb'] = sql_raw( 'B010001','P0001:16')

    ##承保req趋势
    kwargs['js_Req_nbz'] = sql_raw( 'B020001','P0003:11')

    ## clm req趋势
    kwargs['js_Req_clm'] = sql_raw( 'B020001','P0003:12')

    ##fin req趋势
    kwargs['js_Req_fin'] = sql_raw( 'B020001','P0003:13')

    ##xb req趋势
    kwargs['js_Req_xb'] = sql_raw( 'B020001','P0003:16')

    ##zb req趋势
    kwargs['js_Req_zb'] = sql_raw( 'B020001','P0003:15')

    ##承保Pub趋势
    kwargs['js_Pub_nbz'] = sql_raw( 'B030001','P0001:11')

    ##clm Pub趋势
    kwargs['js_Pub_clm'] = sql_raw( 'B030001','P0001:12')

    ##fin Pub趋势
    kwargs['js_Pub_fin'] = sql_raw( 'B030001','P0001:13')

    ##zb Pub趋势
    kwargs['js_Pub_zb'] = sql_raw( 'B030001','P0001:15')

    ##xb Pub趋势
    kwargs['js_Pub_xb'] = sql_raw( 'B030001','P0001:14')


    ##xb Pub趋势
    kwargs['js_Pub_xb'] = sql_raw('B030001', 'P0001:14')

    ##  明细趋势
    kwargs['js_Pr_detail_01'] = sql_raw('B012001', 'P0001:11,P0006:11')
    kwargs['js_Pr_detail_02'] = sql_raw('B012001', 'P0001:11,P0006:12')
    kwargs['js_Pr_detail_03'] = sql_raw('B012001', 'P0001:11,P0006:13')
    kwargs['js_Pr_detail_04'] = sql_raw('B012001', 'P0001:11,P0006:14')

    #万单
    kwargs['js_Pr_detail_wan'] = sql_raw('B011001', 'P0001:11')



    # ## num 趋势
    # Pub_xb1 = Dcitemdata.objects.raw("""
    #                  SELECT dataid,itemno,itemname,datadate ,itemvalue1 ,itemvalue2 ,itemvalue3  FROM
    #                 (select a.dataid,a.itemno,pkg_operatefunc_dcshow.GetFactorNames(a.dataid,'-') as itemname,a.datadate ,a.itemvalue1 ,a.itemvalue2 ,a.itemvalue3
    #                 from syscfg_dcitemdata a
    #                 where a.itemno = 'B012001' and length(a.datadate) = 7 and a.datadate >= %s )
    #                 where itemname = '承保-总部运维'
    #                 order by datadate,dataid""", [startMonth])
    # Pub_xb1_ser = DcitemdataSer(Pub_xb1, many=True)
    # kwargs['js_Pub_xb1'] = JSONRenderer().render(Pub_xb1_ser.data)



    # 地区统计-all
    AreaCal = Dcitemdata.objects.raw("""
         SELECT dataid,itemno,itemname,datadate ,itemvalue1 ,itemvalue2 ,itemvalue3  FROM
        (select a.dataid,a.itemno,pkg_operatefunc_dcshow.GetFactorNames(a.dataid,'-') as itemname,a.datadate ,a.itemvalue1 ,a.itemvalue2 ,a.itemvalue3
        from syscfg_dcitemdata a
        where a.itemno = 'A01001' and length(a.datadate) = 7 and a.datadate >= %s )
        where rownum < 6
        order by datadate,dataid  """, [startMonth])
    AreaCal_ser = DcitemdataSer(AreaCal, many=True)
    kwargs['AreaCal'] = AreaCal
    kwargs['js_AreaCal'] = JSONRenderer().render(AreaCal_ser.data)

    # 系统问题占比
    Pr_sys = Dcitemdata.objects.raw(
        """ select a.dataid,pkg_operatefunc_dcshow.GetFactorNames(a.dataid) itemname,a.datadate,a.itemvalue1,a.itemvalue2,a.itemvalue3 from syscfg_dcitemdata a where a.itemno = 'B010001' and pkg_operatefunc_dcshow.IsMonthDate(a.datadate) = 1 and  a.datadate  = '2017-10'  """)[
             :5]
    Pr_sys_ser = DcitemdataSer(Pr_sys, many=True)

    kwargs['Pr_sys'] = Pr_sys
    kwargs['js_Pr_sys'] = JSONRenderer().render(Pr_sys_ser.data)

    # 系统可用率
    js_Sys_avl = Dcitemdata.objects.raw(
        """ SELECT a.dataid,pkg_operatefunc_dcshow.GetFactorNames(a.dataid) itemname,a.datadate,a.itemvalue1,a.itemvalue2,a.itemvalue3 FROM syscfg_dcitemdata a
where a.itemno = 'C010001' and pkg_operatefunc_dcshow.IsMonthDate(a.datadate) = 1 and a.datadate  >= %s """,
        [startMonth])
    js_Sys_avl_ser = DcitemdataSer(js_Sys_avl, many=True)
    kwargs['js_Sys_avl'] = JSONRenderer().render(js_Sys_avl_ser.data)


    # 时效01
    Pr_time_01 = Dcitemdata.objects.raw(
        """ SELECT a.dataid,pkg_operatefunc_dcshow.GetFactorNames(a.dataid) itemname,a.datadate,a.itemvalue1,a.itemvalue2,a.itemvalue3 FROM syscfg_dcitemdata a
where a.itemno = 'C010001' and pkg_operatefunc_dcshow.IsMonthDate(a.datadate) = 1 and a.datadate  >= %s """,
        [startMonth])
    Pr_time_01_ser = DcitemdataSer(Pr_time_01, many=True)
    kwargs['js_Pr_time_01'] = JSONRenderer().render(Pr_time_01_ser.data)

    # 时效02
    Pr_time_02 = Dcitemdata.objects.raw(
        """ SELECT a.dataid,pkg_operatefunc_dcshow.GetFactorNames(a.dataid) itemname,a.datadate,a.itemvalue1,a.itemvalue2,a.itemvalue3 FROM syscfg_dcitemdata a
where a.itemno = 'C010001' and pkg_operatefunc_dcshow.IsMonthDate(a.datadate) = 1 and a.datadate  >= %s """,
        [startMonth])
    Pr_time_02_ser = DcitemdataSer(Pr_time_02, many=True)
    kwargs['js_Pr_time_02'] = JSONRenderer().render(Pr_time_02_ser.data)

    # SLA_01  总部运维
    SLA_ops = Dcitemdata.objects.raw("""

    SELECT a.dataid,pkg_operatefunc_dcshow.GetFactorNames(a.dataid) itemname,a.datadate,a.itemvalue1,a.itemvalue2,a.itemvalue3
    from syscfg_dcitemdata a where a.itemno = 'B012001'
    and pkg_operatefunc_dcshow.IsMonthDate(a.datadate) = 1 and a.datadate = '2017-10'
    and pkg_operatefunc_dcshow.CheckFactorList(a.dataid,'P0001:%%,P0006:13') = 1
    """)[:5]
    SLA_ops_ser = DcitemdataSer(SLA_ops, many=True)
    kwargs['js_SLA_ops'] = JSONRenderer().render(SLA_ops_ser.data)

    # SLA_02    总部二线
    SLA_spt = Dcitemdata.objects.raw("""
       SELECT a.dataid,pkg_operatefunc_dcshow.GetFactorNames(a.dataid) itemname,a.datadate,a.itemvalue1,a.itemvalue2,a.itemvalue3
       from syscfg_dcitemdata a where a.itemno = 'B012001'
       and pkg_operatefunc_dcshow.IsMonthDate(a.datadate) = 1 and a.datadate = '2017-10'
       and pkg_operatefunc_dcshow.CheckFactorList(a.dataid,'P0001:%%,P0006:14') = 1  """)[:5]
    SLA_spt_ser = DcitemdataSer(SLA_spt, many=True)
    kwargs['js_SLA_spt'] = JSONRenderer().render(SLA_spt_ser.data)






    return kwargs


