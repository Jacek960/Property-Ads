from django.urls import path
from .views import HomePageView, AdByCategoryView, AllAdsView, AdsByLocationView, DashbordView,AdsDetailsView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('ogloszenia/cat/<slug:category_slug>/',AdByCategoryView.as_view(), name='all_ads_category'),
    path('ogloszenia/',AllAdsView.as_view(), name='all_ads'),
    path('ogloszenia/loc/<slug:location_slug>/',AdsByLocationView.as_view(), name='all_ads_location'),
    path('dashbord/', DashbordView.as_view(), name='dashbord'),
    path('ogloszenia/<slug:advert_slug>/',AdsDetailsView.as_view(), name='ads_details'),
]