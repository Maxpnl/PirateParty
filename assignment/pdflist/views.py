from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.http import HttpResponse

from pdflist.models import PdfFile


def pdfListView(request): # The homepage, it gets all the PdfFiles and passes it to the template which will loop trough and print their details
	pdflist = PdfFile.objects.all()
	return render(request, 'pdflist.html', {'pdflist' : pdflist})

def pdfDownload(request, slug): 
	# Handle the file download (obviously everyone who has access to the admin credentials should be trusted,
	# otherwise this would lead to a security issue due to the lack of controls on sequences like "../" or "/"
	# and so on inside the file_name field, the security here depends on the context of this implementation)

	pdf = get_object_or_404(PdfFile, item_slug=slug)
	with open(pdf.getLocation(), 'rb') as file:

		response = HttpResponse(content_type='application/pdf')
		response['Content-Disposition'] = 'attachment; filename="{}"'.format(pdf.file_name) 
		response.write(file.read())

		return response

def pdfView(request, slug): # Used to render the js viewer with the pdf file
	pdf = get_object_or_404(PdfFile, item_slug=slug)

	return render(request, 'pdfview.html', {'pdf': pdf})