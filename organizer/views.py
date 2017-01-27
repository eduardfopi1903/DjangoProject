from django.http import HttpResponse 
from .models import Tag

def homepage(request):
	tag_list = Tag.objects.all()
	output = "<html>\n"
	output += "<head>\n"
	output += " <title>"
	output += "Don't do This!</title>\n"
	output += "</head> \n"
	output += "<body>\n"
	output += " <ul>\n"
	for tag in tag_list:
		output += " <li>"
		output += tag.name.title() 
		output += "</li>\n"
	output += " </ul>\n"
	output += "</body>\n"
	output += "</html>\n"
	return HttpResponse(output)

# Create your views here.
