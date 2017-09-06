from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
import json
from django.core import serializers
#from todos.models import Todo
from app.models import Todo,OpsCal,OpsJira,OpsExamine
from datetime import datetime

def index(request):
    todo = Todo.objects.get(id='2')
    opsCal = OpsCal.objects.all

    #jira分布情况
    opsJira = OpsJira.objects.filter(d_date=datetime(2017, 9, 4)).order_by('-num')[:5]
    json_opsJira = serializers.serialize("json", opsJira)

    #机构考核数据
    opsExamine = OpsExamine.objects.order_by('-d_sum')[:10]


    results = {'name': 123, 'name1': 456, 'sysname': ['单证','理赔'],"items":
        [{"name": "name1", "sector": "sector1"},
         {"name": "name2", "sector": "sector2"},
         {"name": "name3", "sector": "sector3"}]}

    #todo = Todo.objects.get
    #context = {'todo': todo}
    iosper = OpsCal.objects.get(id = '2')
    context = {'todo': todo,'opsCal':opsCal,'iosper':iosper,'opsJira':opsJira,'results':results,'json_opsJira':json_opsJira,
               'opsExamine':opsExamine
               }
    template = loader.get_template('app/index.html')
    return HttpResponse(template.render(context, request))


def gentella_html(request):
    # 机构考核数据
    opsExamine = OpsExamine.objects.order_by('-d_sum')[:10]
    context = {'opsExamine':opsExamine}
    # The template to be loaded as per HaOps.
    # All resource paths for HaOps end in .html.

    # Pick out the html file name from the url. And load that template.
    load_template = request.path.split('/')[-1]
    template = loader.get_template('app/' + load_template)
    return HttpResponse(template.render(context, request))



def get_context_data_all(**kwargs):
    kwargs['Ops_jira'] = OpsJira.objects.order_by('num')[:5]
    #kwargs['date_archive'] = Article.objects.archive()
    # kwargs['tag_list'] = Tag.objects.all()
    # visitor_ip = VisitorIP.objects.all()[:5]
    # for visitor in visitor_ip:
    #     ip_split = visitor.ip.split('.')
    #     visitor.ip = '%s.*.*.%s' % (ip_split[0], ip_split[3])
    # kwargs['visitor_ip'] = visitor_ip
    # kwargs['visitor_num'] = cache.get('visitor_num')
    # recent_comment = BlogComment.objects.order_by('-created_time')[:5]
    # for comment in recent_comment:
    #     if len(comment.body) > LENGTH_IN_RIGHT_INDEX:
    #         comment.body = comment.body[:LENGTH_IN_RIGHT_INDEX + 1] + '...'
    # kwargs['recent_comment'] = recent_comment
    # hot_article = Article.objects.filter(
    #     status='p').order_by('-weight', '-created_time')[:5]
    # for article in hot_article:
    #     if len(article.title) > LENGTH_IN_RIGHT_INDEX:
    #         article.title = article.title[:LENGTH_IN_RIGHT_INDEX + 1] + '...'
    # kwargs['hot_article'] = hot_article
    return kwargs


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