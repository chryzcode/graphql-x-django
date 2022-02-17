from django.contrib import admin
from .models import ExtendedUser
from django.apps import apps
# Register your models here.

admin.site.register(ExtendedUser)
 

app = apps.get_app_config('graphql_auth')

for model_name, model in app.models.items():
    admin.site.register(model)