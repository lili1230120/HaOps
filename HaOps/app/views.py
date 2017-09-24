from django.shortcuts import render,get_object_or_404
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from django.core import serializers
from app.models import *
from datetime import datetime
from django.db.models import Count
from django.utils import timezone

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
    template_name = 'app/index.html'
    renderer_classes = [TemplateHTMLRenderer]

    period = TestForm(initial={"date_start": (date.today() - timedelta(days=7)), "date_end": date.today()})

    def get(self,request):
        period = TestForm(initial={"date_start": (date.today() - timedelta(days=7)), "date_end": date.today()})

        # 获取所有运营数据
        context = get_context_data_all()

        return Response(context)

    def post(self, request):
        period = None
        Review_form = OpsReviewSerializer(data=request.data)

        form = TestForm(request.POST)
        #period = form.cleaned_data['period']

        if Review_form.is_valid():
            Review_form.save()
            return HttpResponseRedirect('/')
        else:
            queryset = OpsReview.objects.all()
            serializer = OpsReviewSerializer(queryset, many=True)

            context = get_context_data_all()
        return Response(context)


    #
    # def post(self, request):
    #     form = SchoolSerializer(data=request.data)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect('/')
    #     else:
    #         queryset = School.objects.all()
    #         serializer = SchoolSerializer(queryset, many=True)
    #         return Response({'data': serializer.data, 'form': form})



class ReviewCreate(APIView):

    renderer_classes = [TemplateHTMLRenderer]


    def get(self, request, *args, **kwargs):
        model = OpsReview
        template_name = "app/review_add.html"
        fields = ['title', 'comment']
        context = {
               '1': 1
               }
        return Response(context,template_name=template_name)


class HaOpsView(APIView):
    # template_name = 'app/index.html'
    # renderer_classes = [TemplateHTMLRenderer]

    renderer_classes = (TemplateHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        load_template = request.path.split('/')[-1]
        template_name = 'app/' + load_template

    #获取所有运营数据
        context = get_context_data_all()

    # The template to be loaded as per HaOps.
    # All resource paths for HaOps end in .html.


    # Pick out the html file name from the url. And load that template.
        return Response(context,template_name = template_name)

        #return HttpResponse(template_name.render(context, request))




#
# class ReviewCreate(CreateView):
#     model = Review
#     template_name="books/book/add_review.html"
#     fields = ['comment']
#     # success_url="/books/"
#     # context_object_name = 'books'
#     def get_context_data(self, **kwargs):
#         return dict(
#             super(ReviewCreate,self).get_context_data(**kwargs),
#             # book_id=self.kwargs.get('pk')
#             book_info=Book.objects.filter(pk=self.kwargs.get('pk'))
#         )
#
#     def form_valid(self,form):
#         review = form.save(commit=False)
#         review_check = Review.objects.filter(user=self.request.user,book=self.kwargs.get('pk'))
#         if review_check:
#             form._errors[forms.forms.NON_FIELD_ERRORS]=ErrorList([
#             u'Review already created'
#             ])
#             return self.form_invalid(form)
#
#         else:
#             review.user = self.request.user
#             review.book_id = self.kwargs.get('pk')
#             return super(ReviewCreate, self).form_valid(form)
#     def get_success_url(self,**kwargs):
#         return reverse('books:book-detail', kwargs={'pk':self.kwargs.get('pk')})



def get_context_data_all(**kwargs):
    kwargs['todo'] = Todo.objects.get(id='2')

    opsCal  = OpsCal.objects.all
    #serializers = OpsCalSerializer(opsCal, many=True)


    # jira分布情况


    kwargs['opsJira'] = OpsJira.objects.filter(d_date__startswith=datetime(2017, 9, 4)).order_by('-num')[:5]

    opsJira = OpsJira.objects.filter(d_date__startswith=datetime(2017, 9, 4)).order_by('-num')[:5]
    opsJira_ser = OpsJiraSerializer(opsJira, many=True)
    kwargs['json_opsJira'] = JSONRenderer().render(opsJira_ser.data)

    # 机构考核数据
    kwargs['opsExamine'] = OpsExamine.objects.order_by('-d_sum')[:10]

    # 标签统计
    kwargs['jiraTag'] = OpsJiraDtl.objects.all().values('tag').annotate(total=Count('tag') * 15).order_by('total')

    # 产能统计
    kwargs['capacity'] = OpsCapacity.objects.filter(input_date__startswith=datetime(2017, 9, 20)).order_by('-num')[:5]

    # 地区统计
    kwargs['jiraArea'] = OpsJiraDtl.objects.all().values('area').annotate(total=Count('area') * 15).order_by('-total')

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
    kwargs['opsReview'] = OpsReview.objects.all()
    opsReview = OpsReview.objects.all()
    kwargs['opsReview_ser'] = OpsReviewSerializer(opsReview, many=True)
   # kwargs['js_opsReview'] = JSONRenderer().render(opsReview_ser.data)
    Review_form = OpsReviewSerializer()

    kwargs['Review_form'] = Review_form

    return kwargs
    # The template to be loaded as per HaOps.
    # All resource paths for HaOps end in .html.


# def CategoryOverview(req):
#     categories = Category.objects.all()
#     category_table = dict()
#     for category in categories:
#         category_table[category.id] = (category.GetArticleNum(), category.id, category)
#     order_table = sorted(category_table.items(), key=operator.itemgetter(1, 1), reverse=True)
#     context = {'categories':categories, 'order_table':order_table}
#     return render_to_response('blog/category_overview.html', context)
#
# class ArticleDetailView(DetailView):
#     model = Article
#     template_name = "blog/detail.html"
#     context_object_name = "article"
#     pk_url_kwarg = 'article_id'
#
#     def get_object(self, queryset=None):
#         obj = super(ArticleDetailView, self).get_object()
#         # 未发表文章不能显示
#         if obj.status == 'd':
#             raise Http404
#         add_views_or_likes(target_article=obj, views_or_likes='views')
#         obj.save()
#         obj.body = markdown2.markdown(
#             obj.body, ['codehilite'], extras=['fenced-code-blocks'])
#         obj.attachment_url = obj.attachment_url.split('/')
#         client_ip = get_client_ip(self.request)
#         save_client_ip.delay(client_ip, obj.id)
#
#         return obj
#
#     def get_context_data(self, **kwargs):
#         kwargs['comment_list'] = self.object.comment.all()
#         kwargs['comment_nums'] = self.object.comment.count()
#         kwargs['form'] = BlogCommentForm()
#         return super(ArticleDetailView, self).get_context_data(**kwargs)