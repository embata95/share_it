from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include, reverse_lazy
from django.views.generic import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", RedirectView.as_view(url=reverse_lazy("expenses:list")), name="home"),
    path("expenses/", include("expenses.urls", namespace="expenses")),
    path("utils/", include("utils.urls", namespace="utils")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
