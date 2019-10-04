import re
from django.db import models

class PdfFile(models.Model):
	file_name = models.CharField( max_length = 254 )
	name_displayed = models.CharField( max_length = 100 ) # The name to display in the item list
	item_slug = models.CharField( max_length = 254, blank=True, unique=True) # The slug used in the url to view the pdf

	def __str__(self): # Display the "fancy name" in the admin page
		return self.name_displayed
