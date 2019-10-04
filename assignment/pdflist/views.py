from django.shortcuts import render
from pdflist.models import PdfFile

def pdfListView(request):
	pdflist = PdfFile.objects.all()
	return render(request, 'pdflist.html', {'pdflist' : pdflist})
