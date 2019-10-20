from django.contrib import admin
from .models import Prescriptions, Info, Details, Tests
# Register your models here.
admin.site.register(Details)
admin.site.register(Info)
admin.site.register(Prescriptions)
admin.site.register(Tests)