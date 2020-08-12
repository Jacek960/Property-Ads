from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Count
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView, UpdateView
from advert.forms import AdvertForm
from advert.models import Category, Location, Advert

pagination_quantity = 10 # Show  adverts per page.

class HomePageView(View):
    def get(self,request):
        categorys = Category.objects.all().order_by('name')
        locations = Location.objects.all().order_by('name')
        category_count = Category.objects.annotate(total_products=Count('advert')).order_by('name')
        location_count = Location.objects.annotate(total_locations=Count('advert')).order_by('name')
        last3_ads = Advert.objects.order_by('-created')[0:3]
        premium3_ads = Advert.objects.filter(premium='True').order_by('-created')[0:3]
        return render(request, 'advert/home_page.html',{
        'categorys':categorys,
        'locations': locations,
        'category_count': category_count,
        'location_count': location_count,
        'last3_ads':last3_ads,
            'premium3_ads':premium3_ads,
        })

class AdByCategoryView(View):
    def get(self,request,category_slug=None):
        category_count = Category.objects.annotate(total_products=Count('advert')).order_by('name')
        location_count = Location.objects.annotate(total_locations=Count('advert')).order_by('name')
        all_advertisement= Advert.objects.all().order_by('-premium',)
        categorys = Category.objects.all().order_by('name')
        locations = Location.objects.all().order_by('name')
        if category_slug:
            category = Category.objects.get(slug=category_slug)
            all_advertisement=all_advertisement.filter(category=category)
            paginator = Paginator(all_advertisement, pagination_quantity)
            page = request.GET.get('page')
            all_advertisement = paginator.get_page(page)

        return render(request, 'advert/adverts_page.html', {'all_advertisement':all_advertisement,
                'category_count': category_count,
                'location_count': location_count,
                  'categorys':categorys,
                'locations':locations,

            })

class AllAdsView(View):
    def get(self,request):
        all_advertisement= Advert.objects.all().order_by('-premium','-created')
        categorys = Category.objects.all().order_by('name')
        locations = Location.objects.all().order_by('name')
        paginator = Paginator(all_advertisement, pagination_quantity)
        page = request.GET.get('page')
        all_advertisement = paginator.get_page(page)
        return render(request, 'advert/adverts_page.html', {'all_advertisement':all_advertisement,
                                                            'categorys':categorys,
                                                            'locations':locations})


class AdsByLocationView(View):
    def get(self,request,location_slug=None):
        location_count = Location.objects.annotate(total_locations=Count('advert')).order_by('name')
        category_count = Category.objects.annotate(total_products=Count('advert')).order_by('name')
        all_advertisement = Advert.objects.all().order_by('-premium',)
        categorys = Category.objects.all().order_by('name')
        locations = Location.objects.all().order_by('-premium','name')
        if location_slug:
            location = Location.objects.get(slug=location_slug)
            all_advertisement=all_advertisement.filter(location=location)
            paginator = Paginator(all_advertisement, pagination_quantity)
            page = request.GET.get('page')
            all_advertisement = paginator.get_page(page)
        return render(request, 'advert/adverts_page.html',{'all_advertisement':all_advertisement,
                                                                       'category_count': category_count,
                                                                       'location_count': location_count,
                                                                       'locations': locations,
                                                                       'categorys':categorys})

class DashbordView(View):
    def get(self,request):
        user_ads = Advert.objects.filter(owner=request.user)
        paginator = Paginator(user_ads, pagination_quantity)
        page = request.GET.get('page')
        all_advertisement = paginator.get_page(page)
        return render (request, 'advert/dashbord.html',{'all_advertisement':all_advertisement})

class AdsDetailsView(View):
    def get(self,request,advert_slug=None):
        advert = Advert.objects.get(slug=advert_slug)
        return render(request,'advert/advert_details.html',{'advert':advert})


class AdvertUpdate(LoginRequiredMixin, UpdateView):
    model = Advert
    form_class = AdvertForm
    template_name = 'advert/add_ad_form.html'
    success_url = '/dashbord/'

    def user_passes_test(self, request):
        if request.user.is_authenticated:
            self.object = self.get_object()
            return self.object.owner == request.user
        return False

    def dispatch(self, request, *args, **kwargs):
        if not self.user_passes_test(request):
            return redirect('home')
        return super(AdvertUpdate, self).dispatch(
            request, *args, **kwargs)


class AdCreateView(LoginRequiredMixin,View):
    def get(self,request):
        form = AdvertForm()
        return render(request, 'advert/add_ad_form.html',
                      {'form': form})
    def post(self,request):
        advertForm = AdvertForm(request.POST, request.FILES)
        if advertForm.is_valid():
            advert = advertForm.save(commit=False)
            advert.owner = request.user
            advert.save()
            advertForm.save_m2m()
        return redirect('dashbord')

class AdDeleteView(LoginRequiredMixin,View):
    def get(self,request,id):
        advertt = Advert.objects.get(pk=id)
        if advertt.owner == request.user:
            advert_del = Advert.objects.get(pk=id)
            return render(request, 'advert/ad_delete.html', {'advert_del': advert_del})
        else:
            return redirect('home')
    def post(self,request,id):
        advertt = Advert.objects.get(pk=id)
        advertt.delete()
        return redirect('dashbord')


class SearchView(View):
    def get(self,request):
        qs= Advert.objects.all()
        categorys=Category.objects.all().order_by('name')
        locations = Location.objects.all().order_by('name')
        category_query= request.GET.get('category')
        location_query= request.GET.get('location')
        price_max_query = request.GET.get('price_max')
        price_min_query = request.GET.get('price_min')
        room_query = request.GET.get('room')

        if category_query is not None:
            qs = qs.filter(category=category_query)

            if location_query is not None:
                qs = qs.filter(location=location_query)

        if price_min_query !='' and price_min_query is not None:
            qs = qs.filter(price__gte=price_min_query)

        if price_max_query !='' and price_max_query is not None:
            qs = qs.filter(price__lte=price_max_query)

        if room_query !='' and room_query is not None:
            qs = qs.filter(no_of_rooms=room_query)


        context = {
            'categorys':categorys,
             'locations':locations,
            "queryset":qs
        }
        return render(request,'advert/search.html',context)



