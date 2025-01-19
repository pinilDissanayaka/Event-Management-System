from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('create/', views.create_event, name='create_event'),
    path('event/<int:id>', views.update_event, name='update_event'),
    path("view/<int:id>", views.view_event, name='view_event'),
    path("register/<int:id>", views.register_to_event, name="register_to_event"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)