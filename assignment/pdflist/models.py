import re
import os
from django.conf import settings
from django.db import models

class PdfFile(models.Model):
	file_name = models.CharField( max_length = 254 )
	name_displayed = models.CharField( max_length = 100 ) # The name to display in the item list
	item_slug = models.CharField( max_length = 254, blank=True, unique=True) # The slug used in the url to view the pdf

	def getLocation(self):
		return os.path.join(settings.PDF_DIR, self.file_name)
	def getDownloadUrl(self):
		return "/pdf/download/{}".format(self.item_slug)
	def getViewUrl(self):
		return "/pdf/view/{}".format(self.item_slug)

	def __str__(self): # Display the "fancy name" in the admin page
		return self.name_displayed
