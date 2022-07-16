from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
# Create your views here.
from django.views import View

from .forms import *
from django.template.loader import render_to_string
from .models import *
from django.utils.text import slugify

def stackIndexView(request):
        return render(request, 'stack/stack-index.html', {
            'title':'stacks',
            'stacks':Stack.objects.all().order_by('?')
        })

class StackCreateView(View):
    def get(self, request):
        return render(request, 'stack/stack-create.html', {
            'title':f'New Stack',
            'form':StackForm,
            
        })
    
    def post(self, request):
        form = StackForm(request.POST)
        if form.is_valid():
            t = form.save()
            return redirect('stack-detail', t.slug)
        else:
            return render(request, 'stack/stack-create.html', {
                'title':f'New stack',
                'form':form,
            })

class StackUpdateView(View):
    def get(self, request, slug):
        stack = Stack.objects.get(slug=slug)
        return render(request, 'stack/stack-update.html', {
            'title':f'Update {stack.title.title()}',
            'form':StackForm(instance=stack),
        })
    
    def post(self, request, slug):
        stack = Stack.objects.get(slug=slug)
        form = StackForm(request.POST, instance=stack)
        if form.is_valid():
            t = form.save()
            return redirect('stack-detail', slugify(t.title))
        else:
            return render(request, 'stack/stack-update.html', {
                'title':f'Update {stack.title.title()}',
                'form':form,
            })


class StackDetailView(View):

    def get(self, request, slug):
        stack = Stack.objects.get(slug=slug)
        return render(request, 'stack/stack-detail.html', {
            'title':stack.title,
            'stack':stack,
            'eventform':EventForm
        })

class StackFileCreateView(View):
    def get(self, request):
        return render(request, 'stack/stack-file-create.html', {
            'title':'New stack By Txt File',
            'form':StackFileForm
        })

class StackQuizView(View):
    def get(self, request, slug):
        stack = Stack.objects.get(slug=slug)
        stackquiz = stackAPI(stack_obj=stack).quiz()
        return render(request, 'stack/stack-quiz.html', {
            'title':stack.title,
            'stack':stack,
            'stackquiz':stackquiz
        })

def createNewEvent(request, slug):
    stack = Stack.objects.get(slug=slug)
    eventform = EventForm(request.POST)

    if eventform.is_valid():
        event = eventform.save(commit=False)
        event.order = len(stack.events.all()) + 1
        event.user = request.user
        event.save()
        stack.events.add(event)
        stack.save()
        return HttpResponse(render_to_string('stack/partials/stack-detail-body.html', {
            'stack':stack,
        }))

def deleteEvent(request, slug, event_id):
    stack = Stack.objects.get(slug=slug)
    event = Event.objects.get(pk=event_id)
    if request.user == event.user:
        event.delete()
        return HttpResponse(render_to_string('stack/partials/stack-detail-body.html', {
            'stack':stack,
        }))

def verifyTitle(request):
    title = request.GET.get('title')
    stack = Stack.objects.filter(slug=slugify(title))
    
    try:
        validate_title(title)
    except Exception as e:
        return HttpResponse(e)
        

    if len(stack):
        return HttpResponse('stack with this Title already exists.')
    else:
        return HttpResponse('')

def stackSearch(request):
    q = request.GET.get('q')
    if q[0] == '/': q = q[1:]
    if not len(q):
        return HttpResponse('')
    stacks = Stack.objects.filter(slug__icontains=q)
    if not len(stacks):
        return HttpResponse('')
    return HttpResponse(render_to_string('stack/partials/search-results.html', {
        'stackSearchResults':stacks,
        'q':q,
    }, request))

def verifyText(request):
    text = request.GET.get('text')
    text = text.strip()
    if len(text):
        return HttpResponse('')
    else:
        return HttpResponse('Text should not be empty'.title())

@user_passes_test(lambda u: u.is_superuser)
def stackDelete(request, slug):
    stack = Stack.objects.get(slug=slug)
    stack.delete()
    return redirect('stack-index')

def verifyImageUrl(request):
    url = request.GET.get('image_url')
    if 'http' not in url:
        return HttpResponse('Invalid Image URL')
    elif url=='':
        return HttpResponse('')
    else:
        return HttpResponse('')

class EventUpdate(View):
    def get(self, request, slug, event_id):
        stack = Stack.objects.get(slug=slug)
        event = Event.objects.get(pk=event_id)
        eventform  =EventForm(instance=event)

        print(eventform)
        return HttpResponse(render_to_string('stack/partials/event-update.html', {
            'eventform':eventform,
            'stack':stack
        }))