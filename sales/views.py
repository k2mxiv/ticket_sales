from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import datetime
from .models import Product
from .models import Sales
from .forms import ProductForm
from .forms import SalesForm
from django.db.models import Q
from addons.log_fetch import accountingAnd


# Create your views here.

def index(request) :
    page = request.GET.get('page', 1)
    kw = request.GET.get('kw', '')
    getSel = request.GET.get('selp', '')
    if kw :
        product_list = Product.objects.order_by('pcode')
        if getSel == 'pname' :
            product_list = product_list.filter(
            Q(pname__icontains = kw)
        )
        elif getSel == 'pcode' : 
            product_list = product_list.filter(
            Q(pcode__icontains = kw)
        )
    else : 
        product_list = Product.objects.order_by('pcode')
    paginator = Paginator(product_list, 10)
    page_obj = paginator.get_page(page)
    context  = {'product_list' : page_obj, 'page' : page, 'kw' : kw, 'getSel' : getSel} 
    return render(request, 'sales/product_list.html', context)

def detail(request, product_id) :
    product = get_object_or_404(Product, pk = product_id)
    context = {'product' : product}
    return render(request, 'sales/product_detail.html', context)

@login_required(login_url = 'common:login')
def product_create(request) :   
    if request.method == 'POST' :
        #if request.FILES : 
        #    image = Image.open(request.FILES['img_file'])
        #    img_wid, img_hei = image.size
        #    img_ratio = float(img_wid) / float(img_hei)
        #    img_reRatio = int(img_ratio * 200)
        #    image = image.resize((img_reRatio, 200))
        #    
        form = ProductForm(request.POST, request.FILES)       
        if form.is_valid() :           
            products = form.save(commit=False)
            products.create_date = datetime.now()
            products.author = request.user
            products.save()
            return redirect('sales:index')
    else : 
        form = ProductForm()
    context = {'form' : form}    
    return render(request, 'sales/product_form.html', context)

@login_required(login_url = 'common:login')
def product_modify(request, product_id) : 
    product = get_object_or_404(Product, pk = product_id)
    if request.user != product.author : 
        messages.error(request, '수정 권한이 없습니다.')
        return redirect('sales:detail', product_id = product.id)
    
    if request.method == "POST" :
        form = ProductForm(request.POST, request.FILES, instance = product)
        if form.is_valid() : 
            product = form.save(commit = False)
            product.author = request.user
            product.save()
            return redirect('sales:detail', product_id = product.id)
    else : 
        form = ProductForm(instance = product)
    context = {'form' : form}
    return render(request, 'sales/product_form.html', context)

@login_required(login_url = 'common:login')
def product_delete(request, product_id) : 
    product = get_object_or_404(Product, pk = product_id)
    if request.user != product.author : 
        messages.error(request, '삭제 권한이 없습니다.')
        return redirect('sales:detail', product_id = product.id)
    product.delete()
    return redirect('sales:index')

@login_required(login_url = 'common:login')
def sales_create(request, product_id) :
    pform = get_object_or_404(Product, pk = product_id)
    form = SalesForm()
    sales = form.save(commit = False)
    sales.scode = pform.pcode
    sales.sdate = datetime.now()
    sales.qty = request.GET.get('tNumber', 0)
    #print('GET.get', request.GET.get('tNumber'))
    #print('GET', request.GET)
    #print('request', request)
    #print('price', pform.unitprice)
    #print(int(request.GET.get('tNumber', 0)) * int(pform.unitprice))
    sales.amt = int(request.GET.get('tNumber', 0)) * int(pform.unitprice)
    sales.save()
    return redirect('sales:detail', product_id)

def full_history(request) :
    table = accountingAnd.account('All')
    context = {'table' : table}
    return render(request, 'sales/sales_full_list.html', context)

def delete_history(request) :
    table = accountingAnd.account('Del')
    context = {'table' : table}
    return render(request, 'sales/sales_delete_list.html', context)

def live_history(request) :
    table = accountingAnd.account('Liv')
    context = {'table' : table}
    return render(request, 'sales/sales_live_list.html', context)

def img_dir(request, img_str = '') :
    print("!@#!@$!#%", request)
    print(img_str)
    context = {'img_str' : img_str}
    return render(request, 'img_print.html', context)

