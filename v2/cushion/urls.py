from django.contrib import admin
from django.urls import path, include
from cushion_shop import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('shop/', include('cushion_shop.urls')),
    path('cart/', include('cushion_cart.urls')),
    path('search/', include('cushion_search.urls')),
    path('order/', include('cushion_order.urls')),

    path('account/create', views.signupView, name='signup'),
    path('account/login', views.signinView, name='signin'),
    path('account/logout/', views.signoutView, name='signout')
]
