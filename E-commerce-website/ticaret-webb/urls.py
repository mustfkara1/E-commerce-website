from django.urls import path
from . import views

# http://127.0.0.1:8000/
# http://127.0.0.1:8000/home
# http://127.0.0.1:8000/erkek
# http://127.0.0.1:8000/erkek/3
# http://127.0.0.1:8000/kadın
# http://127.0.0.1:8000/cocuk

urlpatterns =[
    path("", views.home, name="home"),
    path("home", views.home),
    path("erkek", views.erkek,name="erkek"),
    path("erkek/<int:id>", views._details,name="erkek"),
    path("kadın", views.kadın,name="kadın"),
    path("kadın/<int:id>", views._details,name="kadın"),
    path("cocuk", views.cocuk,name="cocuk"),
    path("cocuk/<int:id>", views._details,name="cocuk"),
    path("ev&yaşam", views.evyasam,name="evyasam"),
    path("ev&yaşam/<int:id>", views._details,name="evyasam"),
    path("tekneloji", views.tekneloji,name="tekneloji"),
    path("tekneloji/<int:id>", views._details,name="details"),
]