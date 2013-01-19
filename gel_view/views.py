from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse

from gel_view.models import Gel

def index(request):
	gels=Gel.objects.all().order_by('gelref__number')
	title="GelView"
	return render(request, 'gel_view/index.html', {'gels':gels, 'title':title})

