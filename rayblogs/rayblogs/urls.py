from django.contrib import admin
from django.urls import path 
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home,name="home"),
    path("signin/",views.signin,name="signin"),
    path("login/",views.login,name="signin"),
    path("blog/",views.blog,name="blog"),
    path("blog/<slug:link>",views.Dblog,name="Dblog"),
    path("search/",views.search,name="search"),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
