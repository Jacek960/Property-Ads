from django.urls import path
from .views import HomePageView, AdByCategoryView, AllAdsView, ad_by_location

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('ogloszenia/cat/<slug:category_slug>/',AdByCategoryView.as_view(), name='all_ads_category'),
    path('ogloszenia/',AllAdsView.as_view(), name='all_ads'),
    path('ogloszenia/loc/<slug:location_slug>/',ad_by_location, name='all_ads_location'),
]