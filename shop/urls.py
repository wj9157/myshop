from django.conf.urls import url
from . import views
from django.contrib import admin
from shop import views as core_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^snacks/admin/', admin.site.urls),
    url(r'^hot-food/admin/', admin.site.urls),
    url(r'^drinks/admin/', admin.site.urls),
    url(r'^help/admin/', admin.site.urls),
    url(r'^gluten-free/admin/', admin.site.urls),
    url(r'^vegetarian/admin/', admin.site.urls),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^$', views.product_list, name='product_list'),
    url(r'^(?P<category_slug>[-\w]+)/$',
        views.product_list,
        name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
        views.product_detail,
        name='product_detail'),

]