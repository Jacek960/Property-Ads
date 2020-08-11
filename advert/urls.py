from django.urls import path
from .views import HomePageView, AdByCategoryView, AllAdsView, AdsByLocationView, DashbordView, AdsDetailsView, AdCreateView, AdvertUpdate,AdDeleteView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('ogloszenia/cat/<slug:category_slug>/',AdByCategoryView.as_view(), name='all_ads_category'),
    path('ogloszenia/',AllAdsView.as_view(), name='all_ads'),
    path('ogloszenia/loc/<slug:location_slug>/',AdsByLocationView.as_view(), name='all_ads_location'),
    path('dashbord/', DashbordView.as_view(), name='dashbord'),
    path('ogloszenia/<slug:advert_slug>/',AdsDetailsView.as_view(), name='ads_details'),
    path('dodaj-ogloszenie/',AdCreateView.as_view(), name='ads_create'),
    path('zmien-ogloszenie/<int:pk>/',AdvertUpdate.as_view(), name='edit_ad'),
    path('usun-ogloszenie/<int:id>/',AdDeleteView.as_view(), name='delete_ad'),
]