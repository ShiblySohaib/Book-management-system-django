from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage, name='homepage'),
    path("add_book/",views.add_book, name="add_book"),
    path('delete/<int:id>',views.delete_book, name='delete_book'),
    path('update/<int:id>',views.update_book, name='update_book'),
]
