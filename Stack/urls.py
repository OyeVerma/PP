from django.urls import path
from .views import *

urlpatterns = [
    path('', stackIndexView, name='stack-index'),
    path('new/', StackCreateView.as_view(), name='stack-create'),
    path('<slug>/update/', StackUpdateView.as_view(), name='stack-update'),
    # path('<slug>/delete/', stackDelete, name='stack-delete'),
    path('<slug>/', StackDetailView.as_view(), name='stack-detail'),
]

htmxpatterns = [
    path('verify/image-url/', verifyImageUrl, name="stack-verify-image-url"),
    path('verify/title/', verifyTitle, name="stack-verify-title"),
    path('verify/text/', verifyText, name="stack-verify-text"),
    path('search/', stackSearch, name="stack-search"),

    path('<slug>/event/new/', createNewEvent, name="stack-create-new-event"),
    path('<slug>/event/<event_id>/delete/', deleteEvent, name="stack-event-delete"),

    path('<slug>/event/<event_id>/update/', EventUpdate.as_view(), name="stack-event-update")
]

urlpatterns = htmxpatterns + urlpatterns