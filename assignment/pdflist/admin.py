import re
from django.contrib import admin
from django.contrib import messages
from django.db import transaction

from pdflist.models import PdfFile


class PdfFileAdmin(admin.ModelAdmin):
	def save_model(self, request, obj, form, change): # Calculate the item slug from the filename
		try:
			with transaction.atomic(): # Needed in order to avoid problems if the database operation fails (TransactionManagementError)
				obj.item_slug = re.sub('[^0-9a-zA-Z]', '-', obj.file_name) # Every non alphanumeric characters will be replaced with "-"
				super().save_model(request, obj, form, change)
		except Exception as e:
			self.message_user(request, e, level=messages.ERROR) # If anything goes wrong I print the error in the admin panel
admin.site.register(PdfFile, PdfFileAdmin)