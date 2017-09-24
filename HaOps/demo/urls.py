from django.conf.urls import url
from demo.views import *

urlpatterns = [
    # Matches any html file - to be used for gentella
    # Avoid using your .html in your resources.
    # Or create a separate django app.
    # url(r'^.*\.html', views.gentella_html, name='gentella'),

    url(r'^', IndexView.as_view()),
]