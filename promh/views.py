from django.contrib.auth import authenticate, login, logout
from .forms import UserForm, WellForm, CasingForm, LinerForm, DrainholeLinerForm, WellheadForm
from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.urls import reverse
from django.views import generic


from .models import Rig, ProcessComplex, Platform, Well, Casing, Liner, DrainholeLiner, Wellhead

def index(request):
    if not request.user.is_authenticated():
        return render(request, 'promh/login.html')
    else:
        wells = Well.objects.all()
        query = request.GET.get("q")
        if query:
            wells = wells.filter(
                Q(well_code__icontains = query)
            ).distinct()
            return render(request, 'promh/index.html', { 'wells': wells })
        else:
            return render(request, 'promh/index.html', { 'wells': wells })

def detail(request, well_id):
    if not request.user.is_authenticated():
        return render(request, 'promh/login.html')
    else:
        well = get_object_or_404(Well, pk = well_id)
        casing = well.casing_set.all()
        liner = well.liner_set.all()
        drainholeliner = well.drainholeliner_set.all()
        wellhead = well.wellhead_set.all()
        context = {
            'well': well,
            'casing': casing,
            'liner': liner,
            'drainholeliner': drainholeliner,
            'wellhead': wellhead,

        }
        return render(request, 'promh/detail.html', context)

def create_well(request):
    if not request.user.is_authenticated():
        return render(request, 'promh/login.html')
    else:
        form = WellForm(request.POST or None)
        if form.is_valid():
            well = form.save(commit=False)
            well.user = request.user
            well.well_code = well.well_code.upper()
            well.save()
            context = {
                'well': well,
                'casing': well.casing_set.all(),
                'liner': well.liner_set.all(),
                'drainholeliner': well.drainholeliner_set.all(),
                'wellhead': well.wellhead_set.all(),
            }
            return render(request, 'promh/detail.html', context)
        context = {
            "form": form,
        }
        return render(request, 'promh/create_well.html', context)

def create_casing(request, well_id):
    if not request.user.is_authenticated():
        return render(request, 'promh/login.html')
    else:
        form = CasingForm(request.POST or None)
        if form.is_valid():
            casing = form.save(commit=False)
            casing.user = request.user
            w = get_object_or_404(Well, pk = well_id)
            casing.well = w
            casing.save()
            context = {
                'casing': casing,
                'well': w,
                'liner': w.liner_set.all(),
                'drainholeliner': w.drainholeliner_set.all(),
                'wellhead': w.wellhead_set.all(),
            }
            return render(request, 'promh/detail.html', context)
        ww = get_object_or_404(Well, pk = well_id)     
        context = {
            "well": ww,
            "form": form,
        }
        return render(request, 'promh/create_casing.html', context)

def create_liner(request, well_id):
    if not request.user.is_authenticated():
        return render(request, 'promh/login.html')
    else:
        form = LinerForm(request.POST or None)
        if form.is_valid():
            liner = form.save(commit=False)
            liner.user = request.user
            w = get_object_or_404(Well, pk = well_id)
            liner.well = w
            liner.save()
            context = {
                'liner': liner,
                'well': w,
                'casing': w.casing_set.all(),
                'drainholeliner': w.drainholeliner_set.all(),
                'wellhead': w.wellhead_set.all(),
            }
            return render(request, 'promh/detail.html', context)
        ww = get_object_or_404(Well, pk = well_id)    
        context = {
            "well": ww,
            "form": form,
        }
        return render(request, 'promh/create_liner.html', context)

def create_drainholeliner(request, well_id):
    if not request.user.is_authenticated():
        return render(request, 'promh/login.html')
    else:
        form = DrainholeLinerForm(request.POST or None)
        if form.is_valid():
            drainholeliner = form.save(commit=False)
            drainholeliner.user = request.user
            w = get_object_or_404(Well, pk = well_id)
            drainholeliner.well = w
            drainholeliner.save()
            context = {
                'drainholeliner': drainholeliner,
                'well': w,
                'casing': w.casing_set.all(),
                'liner': w.liner_set.all(),
                'wellhead': w.wellhead_set.all(),
            }
            return render(request, 'promh/detail.html', context)
        ww = get_object_or_404(Well, pk = well_id)    
        context = {
            "well": ww,
            "form": form,
        }
        return render(request, 'promh/create_drainholeliner.html', context)

def create_wellhead(request, well_id):
    if not request.user.is_authenticated():
        return render(request, 'promh/login.html')
    else:
        form = WellheadForm(request.POST or None)
        if form.is_valid():
            wellhead = form.save(commit=False)
            wellhead.user = request.user
            w = get_object_or_404(Well, pk = well_id)
            wellhead.well = w
            wellhead.save()
            context = {
                'wellhead': wellhead,
                'well': w,
                'casing': w.casing_set.all(),
                'liner': w.liner_set.all(),
                'drainholeliner': w.drainholeliner_set.all(),
            }
            return render(request, 'promh/detail.html', context)
        ww = get_object_or_404(Well, pk = well_id)    
        context = {
            "well": ww,
            "form": form,
        }
        return render(request, 'promh/create_wellhead.html', context)                                     

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

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                wells = Well.objects.all()
                return render(request, 'promh/index.html', {'wells': wells})
            else:
                return render(request, 'promh/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'promh/login.html', {'error_message': 'Invalid login'})
    return render(request, 'promh/login.html')

def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'promh/login.html', context)   	