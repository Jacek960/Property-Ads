from django.db.models import Count
from django.shortcuts import render
from django.views import View
# Create your views here.
from advert.models import Category, Location, Advert


class HomePageView(View):
    def get(self,request):
        categorys = Category.objects.all().order_by('name')
        locations = Location.objects.all().order_by('name')
        category_count = Category.objects.annotate(total_products=Count('advert')).order_by('name')
        location_count = Location.objects.annotate(total_locations=Count('advert')).order_by('name')
        last3_ads = Advert.objects.order_by('-created')[0:3]
        return render(request, 'advert/home_page.html',{
        'categorys':categorys,
        'locations': locations,
        'category_count': category_count,
        'location_count': location_count,
        'last3_ads':last3_ads,
        })

class AdByCategoryView(View):
    def get(self,request,category_slug=None):
        category_count = Category.objects.annotate(total_products=Count('advert')).order_by('name')
        location_count = Location.objects.annotate(total_locations=Count('advert')).order_by('name')
        all_advertisement= Advert.objects.all()
        categorys = Category.objects.all().order_by('name')
        locations = Location.objects.all().order_by('name')
        if category_slug:
            category = Category.objects.get(slug=category_slug)
            all_advertisement=all_advertisement.filter(category=category)

        return render(request, 'advert/adverts_page.html', {'all_advertisement':all_advertisement,
                'category_count': category_count,
                'location_count': location_count,
                  'categorys':categorys,
                'locations':locations,

            })

class AllAdsView(View):
    def get(self,request):
        all_advertisement= Advert.objects.all()
        return render(request, 'advert/adverts_page.html', {'all_advertisement':all_advertisement,})


class AdsByLocationView(View):
    def get(self,request,location_slug=None):
        location_count = Location.objects.annotate(total_locations=Count('advert')).order_by('name')
        category_count = Category.objects.annotate(total_products=Count('advert')).order_by('name')
        all_advertisement = Advert.objects.all()
        categorys = Category.objects.all().order_by('name')
        locations = Location.objects.all().order_by('name')
        if location_slug:
            location = Location.objects.get(slug=location_slug)
            all_advertisement=all_advertisement.filter(location=location)
        return render(request, 'advert/adverts_page.html',{'all_advertisement':all_advertisement,
                                                                       'category_count': category_count,
                                                                       'location_count': location_count,
                                                                       'locations': locations,
                                                                       'categorys':categorys})

class DashbordView(View):
    def get(self,request):
        user_ads = Advert.objects.filter(owner=request.user)
        return render (request, 'advert/dashbord.html',{'user_ads':user_ads})

class AdsDetailsView(View):
    def get(self,request,advert_slug=None):
        advert = Advert.objects.get(slug=advert_slug)
        return render(request,'advert/advert_details.html',{'advert':advert})