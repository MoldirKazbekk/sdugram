from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from telegrambot.sendMessage import sendTelegram
from grid_panel import *
from myProfile.models import *
from .validator import *


# Create your views here.

def apply(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        form = AdApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            if not validate_image(form, request):
                advt = form.save(False)
                advt.advertisement_user = request.user
                advt.save()
                messages.success(request,
                                 f'Your advertisement is successfully uploaded! {advt.advertisement_user.username}')
                return redirect('Home')
    else:
        form = AdApplicationForm(instance=request.user)

    return render(request, 'applyAd/apply_ad.html', {'form': form})
#
#
# def success(request):
#     if request.method == 'GET':
#         Ads = Advt.objects.all()
#         size = len(Ads)
#         Ads = Advt.objects.get(pk=size)
#         profile = Profile.objects.get(user=request.user)
#     return render(request, 'thanks.html', {'ads': Ads})
