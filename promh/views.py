from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.urls import reverse
from django.views import generic

from .forms import UserForm
from .forms import WellForm 
from .forms import WellUpdateForm
from .forms import RigForm
from .forms import PlatformForm
from .forms import ProcessComplexForm
from .forms import StockForm

from .models import Rig
from .models import ProcessComplex
from .models import Platform
from .models import Well
from .models import Stock

import datetime

def index(request):
    if not request.user.is_authenticated():
        return render(request, 'promh/login.html')
    else:
        stock = Stock.objects.all()[0]
        return render(request, 'promh/index.html', {
            'stock': stock,
        })

def update_stock(request):
    if not request.user.is_authenticated():
        return render(request, 'promh/login.html')
    else:
        s = get_object_or_404(Stock, pk = 1)
        form = StockForm(request.POST or None, instance = s)
        if form.is_valid():
            stock = form.save(commit=False)
            stock.save()
            context = {
                'stock': stock,
            }
            return render(request, 'promh/index.html', context)
        context = {
            "form": form,
        }
        return render(request, 'promh/update_stock.html', context)

def wells(request):
    if not request.user.is_authenticated():
        return render(request, 'promh/login.html')
    else:
        wells = Well.objects.all()
        query = request.GET.get("q")
        if query:
            wells = wells.filter(
                Q(well_code__icontains = query)
            ).distinct()
            return render(request, 'promh/wells.html', {
                'wells': wells,
            })
        else:
            return render(request, 'promh/wells.html', {
                'wells': wells,
            })

def detail(request, well_id):
    if not request.user.is_authenticated():
        return render(request, 'promh/login.html')
    else:
        well = get_object_or_404(Well, pk = well_id)
        context = {
            'well': well,

        }
        return render(request, 'promh/detail.html', context)

def platform_detail(request, platform_id):
    if not request.user.is_authenticated():
        return render(request, 'promh/login.html')
    else:
        platform = get_object_or_404(Platform, pk = platform_id)
        context = {
            'platform': platform,

        }
        return render(request, 'promh/platform_detail.html', context)

def processcomplex_detail(request, processcomplex_id):
    if not request.user.is_authenticated():
        return render(request, 'promh/login.html')
    else:
        processcomplex = get_object_or_404(ProcessComplex, pk = processcomplex_id)
        context = {
            'processcomplex': processcomplex,

        }
        return render(request, 'promh/processcomplex_detail.html', context)

def rig_detail(request, rig_id):
    if not request.user.is_authenticated():
        return render(request, 'promh/login.html')
    else:
        rig = get_object_or_404(Rig, pk = rig_id)
        context = {
            'rig': rig,

        }
        return render(request, 'promh/rig_detail.html', context)               

def update_well(request, well_id):
    if not request.user.is_authenticated():
        return render(request, 'promh/login.html')
    else:
        w = get_object_or_404(Well, pk = well_id)
        s = get_object_or_404(Stock, pk = 1)
        form = WellUpdateForm(request.POST or None, instance = w)
        if form.is_valid():
            well = form.save(commit=False)
            well.user = request.user
            well.well_code = well.well_code.upper()
            well.pub_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            if well.casing_size_30_status == 2:
                s.casing_size_30 -= well.casing_size_30
            if well.casing_size_20_status == 2:
                s.casing_size_20 -= well.casing_size_20
            if well.casing_size_18_5by8_status == 2:
                s.casing_size_18_5by8 -= well.casing_size_18_5by8        
            if well.casing_size_13_3by8_status == 2:
                s.casing_size_13_3by8 -= well.casing_size_13_3by8
            if well.float_joint_11_3by4_status == 2:
                s.float_joint_11_3by4 -= well.float_joint_11_3by4
            if well.casing_size_9_5by8_status == 2:
                s.casing_size_9_5by8 -= well.casing_size_9_5by8
            if well.prem_casing_9_5by8_status == 2:
                s.prem_casing_9_5by8 -= well.prem_casing_9_5by8
            if well.btc_9_5by8_status == 2:
                s.btc_9_5by8 -= well.btc_9_5by8
            if well.chrome_casing_9_5by8_status == 2:
                s.chrome_casing_9_5by8 -= well.chrome_casing_9_5by8
            if well.float_joint_9_5by8_status == 2:
                s.float_joint_9_5by8 -= well.float_joint_9_5by8
            if well.float_joint_liner_11_3by4_large_status == 2:
                s.float_joint_liner_11_3by4_large -= well.float_joint_liner_11_3by4_large
            if well.liner_size_7_status == 2:
                s.liner_size_7 -= well.liner_size_7
            if well.liner_hanger_7_status == 2:
                s.liner_hanger_7 -= well.liner_hanger_7
            if well.chrome_liner_size_7_status == 2:
                s.chrome_liner_size_7 -= well.chrome_liner_size_7
            if well.chrome_liner_hanger_7_status == 2:
                s.chrome_liner_hanger_7 -= well.chrome_liner_hanger_7
            if well.liner_size_5_status == 2:
                s.liner_size_5 -= well.liner_size_5
            if well.liner_hanger_5_status == 2:
                s.liner_hanger_5 -= well.liner_hanger_5
            if well.float_shoe_size_20_status == 2:
                s.float_shoe_size_20 -= well.float_shoe_size_20
            if well.float_shoe_size_18_5by8_status == 2:
                s.float_shoe_size_18_5by8 -= well.float_shoe_size_18_5by8
            if well.float_shoe_size_13_3by8_status == 2:
                s.float_shoe_size_13_3by8 -= well.float_shoe_size_13_3by8
            if well.float_shoe_size_9_5by8_status == 2:
                s.float_joint_9_5by8 -= well.float_joint_9_5by8
            if well.float_collar_size_13_3by8_status == 2:
                s.float_collar_size_13_3by8 -= well.float_collar_size_13_3by8
            if well.float_collar_size_9_5by8_status == 2:
                s.float_collar_size_9_5by8 -= well.float_collar_size_9_5by8
            if well.btc_pin_prem_box_cross_over_9_5by8_status == 2:
                s.btc_pin_prem_box_cross_over_9_5by8 -= well.btc_pin_prem_box_cross_over_9_5by8
            if well.btc_box_prem_pin_cross_over_9_5by8_status == 2:
                s.btc_box_prem_pin_cross_over_9_5by8 -= well.btc_box_prem_pin_cross_over_9_5by8
            if well.wellhead_a_section_status == 2:
                s.wellhead_a_section -= well.wellhead_a_section
            if well.wellhead_b_section_status == 2:
                s.wellhead_b_section -= well.wellhead_b_section
            if well.wellhead_c_section_status == 2:
                s.wellhead_c_section -= well.wellhead_c_section
            if well.wellhead_xmas_tree_status == 2:
                s.wellhead_xmas_tree -= well.wellhead_xmas_tree        

            s.save()    
            well.save()
            context = {
                'well': well,
            }
            return render(request, 'promh/detail.html', context)
        context = {
            "form": form,
        }
        return render(request, 'promh/update_well.html', context)

def create_well(request):
    if not request.user.is_authenticated():
        return render(request, 'promh/login.html')
    else:
        form = WellForm(request.POST or None)
        if form.is_valid():
            well = form.save(commit=False)
            well.user = request.user
            well.well_code = well.well_code.upper()
            well.pub_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            well.save()
            context = {
                'well': well,
            }
            return render(request, 'promh/detail.html', context)
        context = {
            "form": form,
        }
        return render(request, 'promh/create_well.html', context)

def create_rig(request):
    if not request.user.is_authenticated():
        return render(request, 'promh/login.html')
    else:
        form = RigForm(request.POST or None)
        if form.is_valid():
            rig = form.save(commit=False)
            rig.user = request.user
            rig.rig_name = rig.rig_name.upper()
            rig.pub_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            rig.save()
            context = {
                'rig': rig,
            }
            return render(request, 'promh/success.html', context)
        context = {
            "form": form,
        }
        return render(request, 'promh/create_rig.html', context)

def create_processcomplex(request):
    if not request.user.is_authenticated():
        return render(request, 'promh/login.html')
    else:
        form = ProcessComplexForm(request.POST or None)
        if form.is_valid():
            processcomplex = form.save(commit=False)
            processcomplex.user = request.user
            processcomplex.process_complex_code = processcomplex.process_complex_code.upper()
            processcomplex.pub_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            processcomplex.save()
            context = {
                'processcomplex': processcomplex,
            }
            return render(request, 'promh/success.html', context)
        context = {
            "form": form,
        }
        return render(request, 'promh/create_processcomplex.html', context)

def create_platform(request):
    if not request.user.is_authenticated():
        return render(request, 'promh/login.html')
    else:
        form = PlatformForm(request.POST or None)
        if form.is_valid():
            platform = form.save(commit=False)
            platform.user = request.user
            platform.platform_code = platform.platform_code.upper()
            platform.pub_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            platform.save()
            context = {
                'platform': platform,
            }
            return render(request, 'promh/success.html', context)
        context = {
            "form": form,
        }
        return render(request, 'promh/create_platform.html', context)                                                      

def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                #wells = Well.objects.filter(user=request.user)
                wells = Well.objects.all()
                return render(request, 'promh/index.html', {'wells': wells})
    context = {
        "form": form,
    }
    return render(request, 'promh/register.html', context)

def delete_well(request, well_id):
    well = Well.objects.get(pk=well_id)
    well.delete()
    wells = Well.objects.all()
    return render(request, 'promh/index.html', {'wells': wells})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                stock = Stock.objects.all()
                return render(request, 'promh/index.html', {'stock': stock})
            else:
                return render(request, 'promh/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'promh/login.html', {'error_message': 'Invalid login'})
    return render(request, 'promh/login.html')

def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        'form': form,
    }
    return render(request, 'promh/login.html', context)   	