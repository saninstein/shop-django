from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.db.models import Q
from django.template.loader import render_to_string
from shop.models import Slide, Phone


def phone_filter(req, filter_str=""):
    if filter_str == "":
        return redirect(reverse("phones"))

    filter_str = filter_str.split('-')
    print(filter_str)
    filters = {
        "d1": lambda: Q(diagonal__lte=4),
        "d2": lambda: (Q(diagonal__gte=4.1) & Q(diagonal__lt=4.5)),
        "d3": lambda: (Q(diagonal__gte=4.5) & Q(diagonal__lte=5)),
        "d4": lambda: (Q(diagonal__gte=5.1) & Q(diagonal__lte=5.5)),
        "d5": lambda: (Q(diagonal__gte=5.55) & Q(diagonal__lte=6)),
        "d6": lambda: Q(diagonal__gte=6)
    }

    q_objs = None
    filters_keys = list(filters.keys())
    for f in filter_str:
        if f in filters_keys:
            if q_objs == None:
                q_objs = filters[f]()
            else:
                q_objs.add(filters[f](), Q.OR)

    args = dict()
    args["items"] = Phone.objects.filter(q_objs)
    return render_to_response("filter_items/index.html", args)


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