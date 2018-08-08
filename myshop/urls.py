
from django.contrib import admin
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from shop import views
from shop import views as core_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^information.html/', views.information_veiw.as_view()),
    url(r'^payment/', include(('payment.urls','payment'), namespace='payment')),
    url(r'^orders/', include(('orders.urls','orders'), namespace='orders')),
    url(r'^paypal/',include('paypal.standard.ipn.urls')),
    url(r'^cart/', include(('cart.urls', 'cart'), namespace='cart')),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^', include(('shop.urls', 'shop'), namespace='shop')),
    url(r'^', core_views.shop, name='shop'),



]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
