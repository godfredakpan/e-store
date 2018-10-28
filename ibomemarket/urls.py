"""ibomemarket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin


from contact import views as contact_views
from profiles import views as profiles_views
from checkout import views as checkout_views
from dashboard import views as dashboard_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', profiles_views.home, name='home'),
    url(r'^about/$', profiles_views.about, name='about'),
    url(r'^profile/$', profiles_views.userProfile, name='profile'),
    url(r'^contact/$', contact_views.contact, name='contact'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^account/signup', profiles_views.signup, name='signup'),
    url(r'^account/login', profiles_views.login, name='login'),
    url(r'^checkout', checkout_views.checkout, name='checkout'),
    url(r'^dashboard', dashboard_views.dashboard, name='dashboard'),
    url(r'^user', dashboard_views.user, name='user'),
    url(r'^paystack/', include(('paystack.urls', 'paystack'), namespace='paystack')),
    url(r'^cart/', include(('cart.urls', 'cart'),  namespace='cart')),
    url(r'^paystack/', include(('paystack.urls', 'paystack'), namespace='paystack')),
    url(r'^orders/', include(('orders.urls', 'orders'), namespace='orders')),
    url(r'^payment/', include(('payment.urls', 'payment'), namespace='payment')),
    url(r'^paypal/', include('paypal.standard.ipn.urls')),
    url(r'^shop/', include(('shop.urls','shop'), namespace='shop')),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)