from django.contrib import admin
from news.models import Reporter, Article

app_models = [Reporter, Article]

admin.site.register(app_models)
