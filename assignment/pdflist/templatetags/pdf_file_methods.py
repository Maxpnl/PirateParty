from django import template

register = template.Library()

@register.filter
def getDownloadUrl(pdf):
	return pdf.getDownloadUrl()

@register.filter
def getViewUrl(pdf):
	return pdf.getViewUrl()