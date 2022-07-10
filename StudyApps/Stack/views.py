from django.http import HttpResponse
from django.shortcuts import render, resolve_url, redirect
from .utilities import TopicAPI
from django.contrib.auth.decorators import user_passes_test
# Create your views here.
from django.views import generic

from django.views import View

###########
def studyAppsIndex(request):
    return render(request, 'studym/studyapps-index.html', {
        'title':'Study Apps',
        'apps':''
    })
###########

class ListStudyMView(generic.ListView):
    template_name = ""
    
    def get_queryset(self):
        pass

def topicIndexView(request):
        return render(request, 'studym/topic-index.html', {
            'title':'Topics',
            'topics':Topic.objects.all().order_by('?')
        })

from .forms import *
class TopicCreateView(View):
    def get(self, request):
        return render(request, 'studym/topic-create.html', {
            'title':f'New Topic',
            'form':TopicForm(initial={'image_url':''}),
            
        })
    
    def post(self, request):
        form = TopicForm(request.POST)
        if form.is_valid():
            t = form.save()
            return redirect('topic-detail', t.slug)
        else:
            return render(request, 'studym/topic-create.html', {
                'title':f'New Topic',
                'form':form,
            })

class TopicUpdateView(View):
    def get(self, request, slug):
        topic = Topic.objects.get(slug=slug)
        return render(request, 'studym/topic-update.html', {
            'title':f'Update {topic.title.title()}',
            'form':TopicForm(instance=topic),
        })
    
    def post(self, request, slug):
        topic = Topic.objects.get(slug=slug)
        form = TopicForm(request.POST, instance=topic)
        if form.is_valid():
            t = form.save()
            return redirect('topic-detail', slugify(t.title))
        else:
            return render(request, 'studym/topic-update.html', {
                'title':f'Update {topic.title.title()}',
                'form':form,
            })


class TopicDetailView(View):

    def get(self, request, slug):
        topic = Topic.objects.get(slug=slug)
        return render(request, 'studym/topic-detail.html', {
            'title':topic.title,
            'topic':topic
        })

class TopicFileCreateView(View):
    def get(self, request):
        return render(request, 'studym/topic-file-create.html', {
            'title':'New Topic By Txt File',
            'form':TopicFileForm
        })

class TopicQuizView(View):
    def get(self, request, slug):
        topic = Topic.objects.get(slug=slug)
        topicquiz = TopicAPI(topic_obj=topic).quiz()
        return render(request, 'studym/topic-quiz.html', {
            'title':topic.title,
            'topic':topic,
            'topicquiz':topicquiz
        })


def verifyTitle(request):
    title = request.GET.get('title')
    page = request.GET.get('page', 0)
    topic = Topic.objects.filter(slug=slugify(title))
    
    try:
        validate_title(title)
    except Exception as e:
        return HttpResponse(e)
        

    if len(topic):
        return HttpResponse('Topic with this Title already exists.')
    else:
        return HttpResponse('')

def topicSearch(request):
    q = request.GET.get('q')
    if not len(q):
        return HttpResponse('')
    topics = Topic.objects.filter(slug__icontains=q)
    if not len(topics):
        return HttpResponse('')
    return HttpResponse(render_to_string('studym/search-results.html', {
        'topicSearchResults':topics,
        'q':q,
    }, request))

def verifyText(request):
    text = request.GET.get('text')
    text = text.strip()
    if len(text):
        return HttpResponse('')
    else:
        return HttpResponse('Text should not be empty'.title())
# from django.template import RequestContext
from django.template.loader import render_to_string
from .utilities import TopicAPI
def topicFileUpload(request):
    file = request.FILES.get('file')
    topic = TopicAPI().fromFile(file)
    return HttpResponse(render_to_string('studym/topic-update.html', {
        'form':TopicForm(initial={'title':topic['title'], 'text':topic['text'], 'image_url':''}),
        'toPostUrl':resolve_url('topic-create')
    }, request=request))

@user_passes_test(lambda u: u.is_superuser)
def topicDelete(request, slug):
    topic = Topic.objects.get(slug=slug)
    topic.delete()
    return redirect('topic-index')

from django.core.validators import URLValidator
def verifyImageUrl(request):
    url = request.GET.get('image_url')
    if 'http' not in url:
        return HttpResponse('Invalid Image URL')
    elif url=='':
        return HttpResponse('')
    else:
        return HttpResponse('')

        