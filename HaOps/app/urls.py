from django.conf.urls import url
from app.views import *
#from . import views

urlpatterns = [
    # Matches any html file - to be used for gentella
    # Avoid using your .html in your resources.
    # Or create a separate django app.
    # url(r'^.*\.html', views.gentella_html, name='gentella'),

    #新增评论
    url(r'^add/$', ReviewCreate.as_view(), name="review-add"),

    url(r'^create/$',PostView.as_view()),

    url(r'^.*\.html',HaOpsView.as_view(),),

    # 主页
    url(r'^$', IndexView.as_view()),



]