from django.http.response import HttpResponse 
from django.template import loader, Context

from .models import Tag

def homepage(request):
    tag_list = Tag.objects.all()
    template = loader.get_template('organizer/tag_list.html')
    context = Context({'tag_list': tag_list})
    output = template.render(context)
    return HttpResponse(output)

# Create your views here.
        
