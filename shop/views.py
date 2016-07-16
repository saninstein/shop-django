from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from django.template.loader import render_to_string
from shop.models import Slide, Phone


def phone_filter(req, filter_str=""):
    return HttpResponse(filter_str)


def search(req, search_str=""):
    args = dict()
    args["phones"] = Phone.objects.filter(name__icontains=search_str)
    return render_to_response("search/index.html", args)


def all_search(req, search_str=""):
    args = dict()
    args["items"] = Phone.objects.filter(name__icontains=search_str)
    args["search_str"] = search_str
    return render_to_response("items/index.html", args)


def phones_search(req, search_str=""):
    args = dict()
    args['items'] = Phone.objects.filter(name__icontains=search_str)
    return render_to_response("phones/index.html", args)


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