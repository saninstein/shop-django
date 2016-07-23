from django.shortcuts import render, render_to_response, redirect, RequestContext
from django.http import HttpResponse
from shop.views import get_item
from django.contrib import auth
from django.contrib.auth.decorators import user_passes_test
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from adminpanel.form import PhoneForm, TabletForm, NotebookForm, SlideForm, AccessoriesForm, ForHomeForm, ForMasterForm
from shop.models import Slide, Phone, Tablet, Notebook, Accessories, ForMaster, ForHome


def is_su(user):
    return user.is_superuser


@user_passes_test(is_su, login_url='/adminpanel/login/', redirect_field_name='')
def general(req):
    args = dict()
    return render_to_response('admin_general/index.html', args, context_instance=RequestContext(req))


@user_passes_test(is_su, login_url='/adminpanel/login/', redirect_field_name='')
def new_item(req, category='', inv=''):
    args = dict()
    args.update(csrf(req))
    if inv:
        item = get_item(inv)
        item_inv = item.inv
    else:
        item = None
        item_inv = False
    if req.method == 'POST':
        if category == 'phone':
            args['category'] = 'Смартфон'
            form = PhoneForm(req.POST, req.FILES, instance=item or None)
            if form.is_valid():
                item = form.save(commit=False)
                form.save()
                return redirect(item.get_item())
            if item_inv:
                args['url'] = reverse('new_item', kwargs={'category': 'phone', 'inv': item_inv})
            else:
                args['url'] = reverse('add_item', kwargs={'category': 'phone'})
        elif category == 'notebook':
            args['category'] = 'Ноутбук'
            form = NotebookForm(req.POST, req.FILES, instance=item or None)
            if form.is_valid():
                item = form.save(commit=False)
                form.save()
                return redirect(item.get_item())
            if item_inv:
                args['url'] = reverse('new_item', kwargs={'category': 'notebook', 'inv': item_inv})
            else:
                args['url'] = reverse('add_item', kwargs={'category': 'notebook'})
        elif category == 'tablet':
            args['category'] = 'Планшет'
            form = TabletForm(req.POST, req.FILES, instance=item or None)
            if form.is_valid():
                item = form.save(commit=False)
                form.save()
                return redirect(item.get_item())
            if item_inv:
                args['url'] = reverse('new_item', kwargs={'category': 'tablet', 'inv': item_inv})
            else:
                args['url'] = reverse('add_item', kwargs={'category': 'tablet'})
        elif category == 'accessories':
            args['category'] = 'Аксессуар/Комплектующие'
            form = AccessoriesForm(req.POST, req.FILES, instance=item or None)
            if form.is_valid():
                item = form.save(commit=False)
                form.save()
                return redirect(item.get_item())
            if item_inv:
                args['url'] = reverse('new_item', kwargs={'category': 'accessories', 'inv': item_inv})
            else:
                args['url'] = reverse('add_item', kwargs={'category': 'accessories'})
        elif category == 'appliances':
            args['category'] = 'Бытовая Техника'
            form = ForHomeForm(req.POST, req.FILES, instance=item or None)
            if form.is_valid():
                item = form.save(commit=False)
                form.save()
                return redirect(item.get_item())
            if item_inv:
                args['url'] = reverse('new_item', kwargs={'category': 'appliances', 'inv': item_inv})
            else:
                args['url'] = reverse('add_item', kwargs={'category': 'appliances'})
        elif category == 'master-tools':
            args['category'] = 'Для Мастера'
            form = ForMasterForm(req.POST, req.FILES, instance=item or None)
            if form.is_valid():
                item = form.save(commit=False)
                form.save()
                return redirect(item.get_item())
            if item_inv:
                args['url'] = reverse('new_item', kwargs={'category': 'master-tools', 'inv': item_inv})
            else:
                args['url'] = reverse('add_item', kwargs={'category': 'master-tools'})
        args['form'] = form
        return render_to_response('new_item/index.html', args, context_instance=RequestContext(req))
    else:
        if item:
            catg = item.link_category_id
        else:
            catg = False
        if category == 'phone' or catg == 1:
            args['category'] = 'Смартфон'
            args['form'] = PhoneForm(instance=item or None)
            if item_inv:
                args['url'] = reverse('new_item', kwargs={'category': 'phone', 'inv': item_inv})
            else:
                args['url'] = reverse('add_item', kwargs={'category': 'phone'})
        elif category == 'notebook' or catg == 3:
            args['category'] = 'Ноутбук'
            args['form'] = NotebookForm(instance=item or None)
            if item_inv:
                args['url'] = reverse('new_item', kwargs={'category': 'notebook', 'inv': item_inv})
            else:
                args['url'] = reverse('add_item', kwargs={'category': 'notebook'})
        elif category == 'tablet' or catg == 2:
            args['form'] = TabletForm(instance=item or None)
            args['category'] = 'Планшет'
            if item_inv:
                args['url'] = reverse('new_item', kwargs={'category': 'tablet', 'inv': item_inv})
            else:
                args['url'] = reverse('add_item', kwargs={'category': 'tablet'})
        elif category == 'accessories' or catg in [4, 5, 6]:
            args['form'] = AccessoriesForm(instance=item or None)
            args['category'] = 'Аксессуар/Комплектующие'
            if item_inv:
                args['url'] = reverse('new_item', kwargs={'category': 'accessories', 'inv': item_inv})
            else:
                args['url'] = reverse('add_item', kwargs={'category': 'accessories'})
        elif category == 'master-tools' or catg in [7, 8, 9]:
            args['form'] = ForMasterForm(instance=item or None)
            args['category'] = 'Для Мастера'
            if item_inv:
                args['url'] = reverse('new_item', kwargs={'category': 'master-tools', 'inv': item_inv})
            else:
                args['url'] = reverse('add_item', kwargs={'category': 'master-tools'})
        elif category == 'appliances' or catg in [10, 11, 12, 13]:
            args['form'] = ForHomeForm(instance=item or None)
            args['category'] = 'Бытовая Техника'
            if item_inv:
                args['url'] = reverse('new_item', kwargs={'category': 'appliances', 'inv': item_inv})
            else:
                args['url'] = reverse('add_item', kwargs={'category': 'appliances'})
    return render_to_response('new_item/index.html', args, context_instance=RequestContext(req))


@user_passes_test(is_su, login_url='/adminpanel/login/', redirect_field_name='')
def slide_edit(req, num=''):
    args = dict()
    args.update(csrf(req))
    slides = ['1', '2', '3', '4']
    if num in slides:
        try:
            slide = Slide.objects.get(pk=num)
        except Slide.DoesNotExist:
            return redirect('general')
        if req.method == 'POST':
            form = SlideForm(req.POST, req.FILES, instance=slide)
            if form.is_valid():
                form.save()
                return redirect('/')
            else:
                args['category'] = 'Слайд ' + str(slide.id)
                args['form'] = form
                args['url'] = reverse('slide_edit', kwargs={'num': num})
                return render_to_response('new_item/index.html', args, context_instance=RequestContext(req))
        else:
            args['category'] = 'Слайд ' + str(slide.id)
            args['form'] = SlideForm(instance=slide)
            args['url'] = reverse('slide_edit', kwargs={'num': num})
            return render_to_response('new_item/index.html', args, context_instance=RequestContext(req))
    else:
        return redirect('general')


@user_passes_test(is_su, login_url='/adminpanel/login/', redirect_field_name='')
def show_items(req, category=''):
    args = dict()
    args.update(csrf(req))
    if category == 'phone':
        args['items'] = Phone.objects.all()
    elif category == 'tablet':
        args['items'] = Tablet.objects.all()
    elif category == 'notebook':
        args['items'] = Notebook.objects.all()
    elif category == 'accessories':
        args['items'] = Accessories.objects.all()
    elif category == 'appliances':
        args['items'] = ForHome.objects.all()
    elif category == 'master-tools':
        args['items'] = ForMaster.objects.all()
    else:
        return redirect('admingeneral')

    if not args['items']:
        return redirect('admingeneral')
    else:
        args['category'] = args['items'][0].link_category.name
    return render_to_response('show_all/index.html', args, context_instance=RequestContext(req))


@user_passes_test(is_su, login_url='/adminpanel/login/', redirect_field_name='')
def delete_item(req):
    if req.method == 'POST':
        item = get_item(req.POST['item'])
        item.delete()
    return HttpResponse()


def login(req):
    args = dict()
    args.update(csrf(req))
    if req.POST:
        username = req.POST.get('username', '')
        password = req.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(req, user)
            return redirect('/adminpanel/')
        else:
            args['login_error'] = "Пользователь не найден"
            return render_to_response('login/index.html', args, context_instance=RequestContext(req))
    else:
        return render_to_response('login/index.html', args, context_instance=RequestContext(req))


def logout(req):
    auth.logout(req)
    return redirect('/')
