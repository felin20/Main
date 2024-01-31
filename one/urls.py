from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns=[
    path('home',views.home,name='home'),
    path('home1',views.home1,name='home1'),
    path('search',views.search,name='search'),
    path('welcome',views.welcome,name='welcome'),
    path('ulogin',views.ulogin,name='ulogin'),
    path('movlist',views.movlist,name='movlist'),
    

    path('det/<str:Moviename>',views.mdetail,name='det'),
    
    
    path('register',views.register,name='reg'),
    path('register1',views.register1,name='reg1'),
    path('login',views.loginuser,name='login'),
    path('login1',views.loginuser1,name='login1'),
    path('logout',views.logoutuser,name='logout'),
    path('home',views.home),
    path('adrev',views.adrev,name='adrev'),
    path('adcrev',views.adcrev,name='adcrev'),
    path('editto/<int:id>',views.editto,name='editto'),
    path('editto1/<int:id>',views.editto1,name='editto1'),
    
  
    path('todelete/<int:id>',views.todelete,name='todelete'),
    path('todelete1/<int:id>',views.todelete1,name='todelete1'),
    
    path('myreviews/<str:Username>',views.myreview,name='myrev'),
    path('mycritics/<str:Criticname>',views.mycritic,name='mycri'),
    
    

    path('crev/<str:cmov>',views.crev,name='cr')
    
    
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)