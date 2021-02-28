from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='homepage'),
    path('searchformpage', views.saerchformview, name='searchformpage'),
    path('Flipkartsearchresults', views.Flipkartsearchresults, name='Flipkartsearchresults'),
    path('ebaysearchresults', views.ebaysearchresults, name='ebaysearchresults'),
    path('amazonproductresults', views.amazonproductresults, name='amazonproductresults'),
    path('olxpriceresuls', views.olxpriceresuls, name='olxpriceresuls'),

]

