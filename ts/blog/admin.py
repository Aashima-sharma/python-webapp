from django.contrib import admin

# Register your models here.
from .models import Blogpost, signup, Contact

admin.site.register(Blogpost)
admin.site.register(signup)
admin.site.register(Contact)