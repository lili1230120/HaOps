from app.models import *
from app.serializers import *
from django.core import serializers
from rest_framework.renderers import JSONRenderer

import datetime


def get_context_data_all(startDate=datetime.date(2017, 4, 1), endDate=datetime.date(2017, 7, 6), **kwargs):
    OstartDate = datetime.date(2017, 9, 1)
    OendDate = datetime.date(2017, 11, 1)

    startMonth = '2017-01'

    '''
   生产jira趋势查询

    '''
    ##承保趋势
    Pr_nbz = Dcitemdata.objects.raw("""
 SELECT dataid,itemno,itemname,datadate ,itemvalue1 ,itemvalue2 ,itemvalue3  FROM
(select a.dataid,a.itemno,pkg_operatefunc_dcshow.GetFactorNames(a.dataid,'-') as itemname,a.datadate ,a.itemvalue1 ,a.itemvalue2 ,a.itemvalue3
from syscfg_dcitemdata a
where a.itemno = 'B012001' and length(a.datadate) = 7 and a.datadate >= %s )
where itemname = '承保-总部运维'
order by datadate,dataid""", [startMonth])
    Pr_nbz_ser = DcitemdataSer(Pr_nbz, many=True)

    kwargs['Pr_nbz'] = Pr_nbz
    kwargs['js_Pr_nbz'] = JSONRenderer().render(Pr_nbz_ser.data)

    ##理赔趋势
    Pr_clm = Dcitemdata.objects.raw("""
     SELECT dataid,itemno,itemname,datadate ,itemvalue1 ,itemvalue2 ,itemvalue3  FROM
    (select a.dataid,a.itemno,pkg_operatefunc_dcshow.GetFactorNames(a.dataid,'-') as itemname,a.datadate ,a.itemvalue1 ,a.itemvalue2 ,a.itemvalue3
    from syscfg_dcitemdata a
    where a.itemno = 'B012001' and length(a.datadate) = 7 and a.datadate >= %s )
    where itemname = '理赔-总部运维'
    order by datadate,dataid""", [startMonth])
    Pr_clm_ser = DcitemdataSer(Pr_clm, many=True)
    kwargs['js_Pr_clm'] = JSONRenderer().render(Pr_clm_ser.data)

    ##收付趋势
    Pr_fin = Dcitemdata.objects.raw("""
     SELECT dataid,itemno,itemname,datadate ,itemvalue1 ,itemvalue2 ,itemvalue3  FROM
    (select a.dataid,a.itemno,pkg_operatefunc_dcshow.GetFactorNames(a.dataid,'-') as itemname,a.datadate ,a.itemvalue1 ,a.itemvalue2 ,a.itemvalue3
    from syscfg_dcitemdata a
    where a.itemno = 'B012001' and length(a.datadate) = 7 and a.datadate >= %s )
    where itemname = '收付-总部运维'
    order by datadate,dataid""", [startMonth])
    Pr_fin_ser = DcitemdataSer(Pr_fin, many=True)
    kwargs['js_Pr_fin'] = JSONRenderer().render(Pr_fin_ser.data)

    ##信保趋势
    Pr_xb = Dcitemdata.objects.raw("""
     SELECT dataid,itemno,itemname,datadate ,itemvalue1 ,itemvalue2 ,itemvalue3  FROM
    (select a.dataid,a.itemno,pkg_operatefunc_dcshow.GetFactorNames(a.dataid,'-') as itemname,a.datadate ,a.itemvalue1 ,a.itemvalue2 ,a.itemvalue3
    from syscfg_dcitemdata a
    where a.itemno = 'B012001' and length(a.datadate) = 7 and a.datadate >= %s )
    where itemname = '信保-总部运维'
    order by datadate,dataid""", [startMonth])
    Pr_xb_ser = DcitemdataSer(Pr_xb, many=True)
    kwargs['js_Pr_xb'] = JSONRenderer().render(Pr_xb_ser.data)

    ##周边趋势
    Pr_zb = Dcitemdata.objects.raw("""
     SELECT dataid,itemno,itemname,datadate ,itemvalue1 ,itemvalue2 ,itemvalue3  FROM
    (select a.dataid,a.itemno,pkg_operatefunc_dcshow.GetFactorNames(a.dataid,'-') as itemname,a.datadate ,a.itemvalue1 ,a.itemvalue2 ,a.itemvalue3
    from syscfg_dcitemdata a
    where a.itemno = 'B012001' and length(a.datadate) = 7 and a.datadate >= %s )
    where itemname = '周边-总部运维'
    order by datadate,dataid""", [startMonth])
    Pr_zb_ser = DcitemdataSer(Pr_zb, many=True)
    kwargs['js_Pr_zb'] = JSONRenderer().render(Pr_zb_ser.data)

    ##承保req趋势
    Req_nbz = Dcitemdata.objects.raw("""
     SELECT dataid,itemno,itemname,datadate ,itemvalue1 ,itemvalue2 ,itemvalue3  FROM
    (select a.dataid,a.itemno,pkg_operatefunc_dcshow.GetFactorNames(a.dataid,'-') as itemname,a.datadate ,a.itemvalue1 ,a.itemvalue2 ,a.itemvalue3
    from syscfg_dcitemdata a
    where a.itemno = 'B012001' and length(a.datadate) = 7 and a.datadate >= %s )
    where itemname = '承保-总部运维'
    order by datadate,dataid""", [startMonth])
    Req_nbz_ser = DcitemdataSer(Req_nbz, many=True)

    kwargs['js_Req_nbz'] = JSONRenderer().render(Req_nbz_ser.data)

    ## clm req趋势
    Req_clm = Dcitemdata.objects.raw("""
         SELECT dataid,itemno,itemname,datadate ,itemvalue1 ,itemvalue2 ,itemvalue3  FROM
        (select a.dataid,a.itemno,pkg_operatefunc_dcshow.GetFactorNames(a.dataid,'-') as itemname,a.datadate ,a.itemvalue1 ,a.itemvalue2 ,a.itemvalue3
        from syscfg_dcitemdata a
        where a.itemno = 'B012001' and length(a.datadate) = 7 and a.datadate >= %s )
        where itemname = '承保-总部运维'
        order by datadate,dataid""", [startMonth])
    Req_clm_ser = DcitemdataSer(Req_clm, many=True)
    kwargs['js_Req_clm'] = JSONRenderer().render(Req_clm_ser.data)

    ##fin req趋势
    Req_fin = Dcitemdata.objects.raw("""
             SELECT dataid,itemno,itemname,datadate ,itemvalue1 ,itemvalue2 ,itemvalue3  FROM
            (select a.dataid,a.itemno,pkg_operatefunc_dcshow.GetFactorNames(a.dataid,'-') as itemname,a.datadate ,a.itemvalue1 ,a.itemvalue2 ,a.itemvalue3
            from syscfg_dcitemdata a
            where a.itemno = 'B012001' and length(a.datadate) = 7 and a.datadate >= %s )
            where itemname = '承保-总部运维'
            order by datadate,dataid""", [startMonth])
    Req_fin_ser = DcitemdataSer(Req_fin, many=True)
    kwargs['js_Req_fin'] = JSONRenderer().render(Req_fin_ser.data)

    ##xb req趋势
    Req_xb = Dcitemdata.objects.raw("""
             SELECT dataid,itemno,itemname,datadate ,itemvalue1 ,itemvalue2 ,itemvalue3  FROM
            (select a.dataid,a.itemno,pkg_operatefunc_dcshow.GetFactorNames(a.dataid,'-') as itemname,a.datadate ,a.itemvalue1 ,a.itemvalue2 ,a.itemvalue3
            from syscfg_dcitemdata a
            where a.itemno = 'B012001' and length(a.datadate) = 7 and a.datadate >= %s )
            where itemname = '承保-总部运维'
            order by datadate,dataid""", [startMonth])
    Req_xb_ser = DcitemdataSer(Req_xb, many=True)
    kwargs['js_Req_xb'] = JSONRenderer().render(Req_xb_ser.data)

    ##zb req趋势
    Req_zb = Dcitemdata.objects.raw("""
             SELECT dataid,itemno,itemname,datadate ,itemvalue1 ,itemvalue2 ,itemvalue3  FROM
            (select a.dataid,a.itemno,pkg_operatefunc_dcshow.GetFactorNames(a.dataid,'-') as itemname,a.datadate ,a.itemvalue1 ,a.itemvalue2 ,a.itemvalue3
            from syscfg_dcitemdata a
            where a.itemno = 'B012001' and length(a.datadate) = 7 and a.datadate >= %s )
            where itemname = '承保-总部运维'
            order by datadate,dataid""", [startMonth])
    Req_zb_ser = DcitemdataSer(Req_zb, many=True)
    kwargs['js_Req_zb'] = JSONRenderer().render(Req_zb_ser.data)

    ##承保Pub趋势
    Pub_nbz = Dcitemdata.objects.raw("""
                 SELECT dataid,itemno,itemname,datadate ,itemvalue1 ,itemvalue2 ,itemvalue3  FROM
                (select a.dataid,a.itemno,pkg_operatefunc_dcshow.GetFactorNames(a.dataid,'-') as itemname,a.datadate ,a.itemvalue1 ,a.itemvalue2 ,a.itemvalue3
                from syscfg_dcitemdata a
                where a.itemno = 'B012001' and length(a.datadate) = 7 and a.datadate >= %s )
                where itemname = '承保-总部运维'
                order by datadate,dataid""", [startMonth])
    Pub_nbz_ser = DcitemdataSer(Pub_nbz, many=True)
    kwargs['js_Pub_nbz'] = JSONRenderer().render(Pub_nbz_ser.data)

    ##clm Pub趋势
    Pub_clm = Dcitemdata.objects.raw("""
             SELECT dataid,itemno,itemname,datadate ,itemvalue1 ,itemvalue2 ,itemvalue3  FROM
            (select a.dataid,a.itemno,pkg_operatefunc_dcshow.GetFactorNames(a.dataid,'-') as itemname,a.datadate ,a.itemvalue1 ,a.itemvalue2 ,a.itemvalue3
            from syscfg_dcitemdata a
            where a.itemno = 'B012001' and length(a.datadate) = 7 and a.datadate >= %s )
            where itemname = '承保-总部运维'
            order by datadate,dataid""", [startMonth])
    Pub_clm_ser = DcitemdataSer(Pub_clm, many=True)
    kwargs['js_Pub_clm'] = JSONRenderer().render(Pub_clm_ser.data)

    ##fin Pub趋势
    Pub_fin = Dcitemdata.objects.raw("""
                 SELECT dataid,itemno,itemname,datadate ,itemvalue1 ,itemvalue2 ,itemvalue3  FROM
                (select a.dataid,a.itemno,pkg_operatefunc_dcshow.GetFactorNames(a.dataid,'-') as itemname,a.datadate ,a.itemvalue1 ,a.itemvalue2 ,a.itemvalue3
                from syscfg_dcitemdata a
                where a.itemno = 'B012001' and length(a.datadate) = 7 and a.datadate >= %s )
                where itemname = '承保-总部运维'
                order by datadate,dataid""", [startMonth])
    Pub_fin_ser = DcitemdataSer(Pub_fin, many=True)
    kwargs['js_Pub_fin'] = JSONRenderer().render(Pub_fin_ser.data)

    ##zb Pub趋势
    Pub_zb = Dcitemdata.objects.raw("""
                 SELECT dataid,itemno,itemname,datadate ,itemvalue1 ,itemvalue2 ,itemvalue3  FROM
                (select a.dataid,a.itemno,pkg_operatefunc_dcshow.GetFactorNames(a.dataid,'-') as itemname,a.datadate ,a.itemvalue1 ,a.itemvalue2 ,a.itemvalue3
                from syscfg_dcitemdata a
                where a.itemno = 'B012001' and length(a.datadate) = 7 and a.datadate >= %s )
                where itemname = '承保-总部运维'
                order by datadate,dataid""", [startMonth])
    Pub_zb_ser = DcitemdataSer(Pub_zb, many=True)
    kwargs['js_Pub_zb'] = JSONRenderer().render(Pub_zb_ser.data)

    ##xb Pub趋势
    Pub_xb = Dcitemdata.objects.raw("""
                 SELECT dataid,itemno,itemname,datadate ,itemvalue1 ,itemvalue2 ,itemvalue3  FROM
                (select a.dataid,a.itemno,pkg_operatefunc_dcshow.GetFactorNames(a.dataid,'-') as itemname,a.datadate ,a.itemvalue1 ,a.itemvalue2 ,a.itemvalue3
                from syscfg_dcitemdata a
                where a.itemno = 'B012001' and length(a.datadate) = 7 and a.datadate >= %s )
                where itemname = '承保-总部运维'
                order by datadate,dataid""", [startMonth])
    Pub_xb_ser = DcitemdataSer(Pub_xb, many=True)
    kwargs['js_Pub_xb'] = JSONRenderer().render(Pub_xb_ser.data)

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
    kwargs['js_AreaCal'] = JSONRenderer().render(Pr_zb_ser.data)

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

    
    return kwargs


