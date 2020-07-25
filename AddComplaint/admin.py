from django.contrib import admin

from AddComplaint import models

admin.site.register([
    models.Complaint
])