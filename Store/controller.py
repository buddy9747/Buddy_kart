from django.urls import path,include
from .import views
from Buddy_kart import settings
from django.conf.urls.static import static

app_name="Store"
urlpatterns = [
    path('', views.fun, name="home"),
    path('<slug:menu>', views.fun1, name="detail"),
    path('user/signin/', views.loginpage, name="login"),
    path('user/addprod/', views.AddCatlog.as_view(), name="addprod"),
    #path('user/upprod/<int:pk>',views.UpdateCatlog.as_view(),name="upprod"),
    path('user/upprod/<int:pk>',views.Detail.as_view(),name="upprod"),
#path('user/delprod/<int:pk>',views.DeleteCatlog.as_view(),name="delprod"),
]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)