from django.urls import path
from . import views
urlpatterns = [
    path('edit_musician/<int:id>', views.edit_details , name = 'edit_details'),
]