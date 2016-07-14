from django.shortcuts import render_to_response, get_object_or_404
from django.template.loader import render_to_string
from shop.models import Slide, Phone


def search(req, search_str):
    print(search_str)


def general(req):
    args = dict()
    args['slides'] = Slide.objects.all()
    args['new_items'] = Phone.objects.all()[:8]
    return render_to_response("general/index.html", args)


def phones(req):
    args = dict()
    args['items'] = get_items(Phone)
    return render_to_response("phones/index.html", args)


def get_items(type):
    items = type.objects.all()
    return items


def item_phone(req, item='1'):
    args = dict()
    args["item"] = get_object_or_404(Phone, pk=item)
    return render_to_response("item_phone/index.html", args)