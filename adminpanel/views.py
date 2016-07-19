from django.shortcuts import render, render_to_response
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
    if category == 'phone':
        args['form'] = PhoneForm
    return render_to_response('new_item/index.html', args)


def add(req, ):
    pass
