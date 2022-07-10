from django.urls import path
from .views import *

urlpatterns = [
    path('', studyAppsIndex, name='studyapps-index'),

    path('stacks', topicIndexView, name='stack-index'),
    path('stack/new/', TopicCreateView.as_view(), name='stack-create'),
    path('stack/<slug>/update/', TopicUpdateView.as_view(), name='stack-update'),
    path('stack-by-file/new/', TopicFileCreateView.as_view(), name='stack-file-create'),
    path('stack<slug>/delete/', topicDelete, name='stack-delete'),
    path('stack<slug>/quiz/', TopicQuizView.as_view(), name='stack-quiz'),
    path('stack<slug>/', TopicDetailView.as_view(), name='stack-detail'),
]

htmxpatterns = [
    path('stack/verify/image-url/', verifyImageUrl, name="stack-verify-image-url"),
    path('stack/verify/title/', verifyTitle, name="stack-verify-title"),
    path('stack/verify/text/', verifyText, name="stack-verify-text"),
    path('stack-file/upload/', topicFileUpload, name="stack-file-upload"),
    path('stacksearch/', topicSearch, name="stack-search"),
]

urlpatterns = htmxpatterns + urlpatterns