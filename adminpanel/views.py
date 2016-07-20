from django.shortcuts import render, render_to_response, redirect
from django.contrib import auth
from django.contrib.auth.decorators import user_passes_test, permission_required
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from adminpanel.form import PhoneForm, TabletForm, NotebookForm
from django.http import HttpResponse


def is_su(user):
    return user.is_superuser


@user_passes_test(is_su, login_url='/adminpanel/login/', redirect_field_name='')
def general(req):
    args = dict()
    args['user'] = req.user
    return render_to_response('admin_general/index.html', args)


@user_passes_test(is_su, login_url='/adminpanel/login/', redirect_field_name='')
def new_item(req, category=''):
    args = dict()
    args['user'] = req.user
    args.update(csrf(req))
    if req.method == 'POST':
        if category == 'phone':
            form = PhoneForm(req.POST, req.FILES)
            if form.is_valid():
                item = form.save(commit=False)
                form.save()
                return redirect(item.get_item())
            args['url'] = reverse('new_item', kwargs={'category': 'phone'})
        elif category == 'notebook':
            form = NotebookForm(req.POST, req.FILES)
            if form.is_valid():
                item = form.save(commit=False)
                form.save()
                return redirect(item.get_item())
            args['url'] = reverse('new_item', kwargs={'category': 'notebook'})
        elif category == 'tablet':
            form = TabletForm(req.POST, req.FILES)
            if form.is_valid():
                item = form.save(commit=False)
                form.save()
                return redirect(item.get_item())
            args['url'] = reverse('new_item', kwargs={'category': 'tablet'})
        args['form'] = form
        return render_to_response('new_item/index.html', args)
    else:
        if category == 'phone':
            args['form'] = PhoneForm()
            args['url'] = reverse('new_item', kwargs={'category': 'phone'})
        elif category == 'notebook':
            args['form'] = NotebookForm()
            args['url'] = reverse('new_item', kwargs={'category': 'notebook'})
        elif category == 'tablet':
            args['form'] = TabletForm()
            args['url'] = reverse('new_item', kwargs={'category': 'tablet'})

    return render_to_response('new_item/index.html', args)


def login(req):
    args = {}
    args.update(csrf(req))
    args['user'] = req.user
    if req.POST:
        username = req.POST.get('username', '')
        password = req.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(req, user)
            return redirect('/adminpanel/')
        else:
            args['login_error'] = "Пользователь не найден"
            return render_to_response('login/index.html', args)
    else:
        return render_to_response('login/index.html', args)


def logout(req):
    auth.logout(req)
    return redirect('/')
