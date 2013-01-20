from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Q

from gel_view.models import Gel

def index(request):
	gels=Gel.objects.all().order_by('gelref__number')
	out=list_gels(request,gels)
	return out

def search(request):
	s=request.GET.__getitem__('s')
	f=request.GET.__getitem__('f')

	search=Gel.objects.filter(Q(gelref__colour_description__icontains=s) | Q(gelref__description__icontains=s)).order_by('gelref__number')

	if f=='cut':
		search=search.exclude(quantity_cut=0)
	elif f=='sheet':
		search=search.exclude(quantity_sheet=0)

	out=list_gels(request,search)
	return out

def list_gels(request,gels):
	form={}
	if 's' in request.GET:
		form['s']=request.GET['s']
		form['f']=request.GET['f']
	else:
		form['s']=""
		form['f']=""

	return render(request, 'gel_view/index.html', {'gels':gels, 'formdata':form})

