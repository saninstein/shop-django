from django.shortcuts import render, render_to_response, redirect
from django.core.context_processors import csrf
from adminpanel.form import PhoneForm
from django.http import HttpResponse


def general(req):
    args = dict()
    args['gen'] = 'HELLO'
    return render_to_response('admin_general/index.html', args)


def new_item(req, category=''):
    args = dict()
    args.update(csrf(req))
    if req.method == 'POST':
        if category == 'phone':
            form = PhoneForm(req.POST, req.FILES)
            if form.is_valid():
                form.save()
                return redirect('general')
            else:
                args['form'] = form
                return render_to_response('new_item/index.html', args)
    else:
        if category == 'phone':
            args['form'] = PhoneForm()
            args['category'] = 'phone'
    return render_to_response('new_item/index.html', args)



