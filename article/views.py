from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.views.generic.base import TemplateView
from django.utils import timezone
from article.models import Article
from forms import ArticleForm
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
# Create your views here.

def hello(request):
    name = "Mike"
    html = "<html><body> Hi %s, this worked...!!</body></html>" % name
    return HttpResponse(html)

def alu(request):
    name = "Mike"
    html = "<html><body> Hi %s, alu this worked...!!</body></html>" % name
    return HttpResponse(html)

def hello_template(request):
    name = "Mike"
    date = timezone.now()
    t = get_template('hello.html')
    html = t.render(Context({'name':name,'date':date}))
    return HttpResponse(html)

class HelloTemplate(TemplateView):
    
    template_name = 'hello_class.html'
    
    def get_context_data(self, **kwargs):
        context = super(HelloTemplate, self).get_context_data(**kwargs)
        context['name'] = 'Mike'
        context['date'] = timezone.now()
        return context
    
def hello_simple_template(request):
    name = "Mike"
    date = timezone.now()
    return render_to_response('hello.html',{'name':name,'date':date,
                                            'language' : language})

def articles(request):
    language = 'en-in'
    session_language = 'en-in'
    if 'lang' in request.COOKIES:
        language = request.COOKIES['lang']
    
    return render_to_response('articles.html',{'articles':Article.objects.all(),
                                               'language' : language})

def article(request, article_id=1):
    return render_to_response('article.html',
                              { 'article':Article.objects.get(id = article_id) })

def language(request, language='en-in'):
    response = HttpResponse("setting language to %s" % language)
    
    response.set_cookie('lang',language)
    
    return response

def create(request):
    if request.POST:
        form=ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            
            return HttpResponseRedirect('/articles/all/')
    
    form = ArticleForm()
        
    args={}
    args.update(csrf(request))
    
    args['form'] = form
    
    return render_to_response('create_article.html',args)
    
    
