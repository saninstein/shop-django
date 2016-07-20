from django.shortcuts import render, render_to_response, redirect
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from adminpanel.form import PhoneForm, TabletForm, NotebookForm
from django.http import HttpResponse


def general(req):
    args = dict()
    return render_to_response('admin_general/index.html', args)


def new_item(req, category=''):
    args = dict()
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



