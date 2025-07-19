from django.urls import path
from CRUD_app import views

urlpatterns = [
    path('',views.studentdata),
    path('edit/<uid>',views.editstudent),
    path('delete/<uid>',views.deletestudent),
    path('search/',views.search_box,name='search_box'),
    path('search/<str:name>/',views.search_box)
    
]