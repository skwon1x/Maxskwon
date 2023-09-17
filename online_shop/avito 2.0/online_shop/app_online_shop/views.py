from django.shortcuts import render, redirect
# Подключаем объект для выполнения HTTP-запроса
from django.http import HttpResponse
from .models import OnlineShop
# from .forms import AdvertisementForm
from .forms import AdvertisementModelForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy


# Функция, отображающая index.html
def index(request):
    query = request.GET.get('query')
    if query:
        online_shops = OnlineShop.objects.filter(title=query)
    else:
        online_shops = OnlineShop.objects.all()
    context = {'online_shops': online_shops}
    return render(request, 'app_advertisement/index.html', context)

# Функция, отображающая top-sellers.html
def top_sellers(request):
    return render(request, 'app_advertisement/top-sellers.html')

@login_required(login_url=reverse_lazy('login'))
def advertisment_post(request):
    # Проверка на пост запрос
    if request.method == 'POST':
        ## Получение формы через класс унаследованный от Form
        # form = AdvertisementForm(request.POST, request.FILES)
        ## Получение формы через класс унаследованный от ModelForm
        form = AdvertisementModelForm(request.POST, request.FILES)
        if form.is_valid():
            # advertisement = OnlineShop(**form.cleaned_data)
            advertisement = form.save(commit=False)
            advertisement.user = request.user
            advertisement.save()
            url = reverse('main-page')
            return redirect(url)
    else:
        ## Отображение формы через класс унаследованный от Form
        # form = AdvertisementForm()
        ## Отображение формы через класс унаследованный от ModelForm
        form = AdvertisementModelForm()
    context = {'form':form}
    return render(request, 'app_advertisement/advertisement-post.html', context)

def advertisment(request):
    return render(request, 'app_advertisement/advertisement.html')
