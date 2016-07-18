from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.http import HttpResponse
from django.db.models import Q, Max, Min
from shop.models import Slide, Phone, Tablet, Notebook, Items

def get_item(item_inv):
    q = Items.objects.get(pk=1)
    a = [q.phone_set, q.tablet_set, q.notebook_set]
    for i in a:
        try:
            item = i.get(inv=item_inv)
        except (Phone.DoesNotExist, Tablet.DoesNotExist, Notebook.DoesNotExist):
            return None
        else:
            return item


def item(req, item=''):
    args = dict(item=get_item(item))
    if args['item']:
        return render_to_response('item_phone/index.html', args)
    else:
        return redirect('general')


def phone_filter(req, filter_str=""):
    if filter_str == "":
        args = dict()
        args["items"] = get_items(Phone)
        return render_to_response("filter_items/index.html", args)
    filter_str = filter_str.split('-')
    filter_str.sort()
    print(filter_str)
    filters = {
        "d1": lambda: Q(diagonal__lte=4),
        "d2": lambda: (Q(diagonal__gte=4.1) & Q(diagonal__lt=4.5)),
        "d3": lambda: (Q(diagonal__gte=4.5) & Q(diagonal__lte=5)),
        "d4": lambda: (Q(diagonal__gte=5.1) & Q(diagonal__lte=5.5)),
        "d5": lambda: (Q(diagonal__gte=5.55) & Q(diagonal__lte=6)),
        "d6": lambda: Q(diagonal__gte=6),

        "r1": lambda: Q(resolution__iexact="2560х1440"),
        "r2": lambda: Q(resolution__iexact="1920x1080"),
        "r3": lambda: Q(resolution__iexact="800х400"),
        "r4": lambda: Q(resolution__iexact="1280x720"),
        "r5": lambda: Q(resolution__iexact="1136x640"),
        "r6": lambda: Q(resolution__iexact="960x540"),
        "r7": lambda: Q(resolution__iexact="854х480"),
        "r8": lambda: Q(resolution__iexact="3840x2160"),

        "n1": lambda: Q(count_core__exact=1),
        "n2": lambda: Q(count_core__exact=2),
        "n3": lambda: Q(count_core__exact=4),
        "n4": lambda: Q(count_core__exact=8),
        "n5": lambda: Q(count_core__gt=8),

        "m1": lambda: Q(ram__lt=1024),
        "m2": lambda: (Q(ram__gte=1024) & Q(ram__lt=2048)),
        "m3": lambda: Q(ram__exact=2048),
        "m4": lambda: Q(ram__exact=3072),
        "m5": lambda: Q(ram__exact=4096),
        "m6": lambda: Q(ram__gt=4096),

        "c1": lambda: Q(camera__lte=2),
        "c2": lambda: (Q(camera__gt=2) & Q(camera__lte=7)),
        "c3": lambda: (Q(camera__gte=8) & Q(camera__lte=12)),
        "c4": lambda: Q(camera__gte=13),

        "f1": lambda: Q(availability__exact="is"),
        "f2": lambda: Q(availability__exact="c"),

        "p": lambda min_p, max_p: (Q(price__gte=min_p) & Q(price__lte=max_p)),
    }

    q_objs_d = Q()
    q_objs_r = Q()
    q_objs_n = Q()
    q_objs_m = Q()
    q_objs_c = Q()
    q_objs_f = Q()
    q_objs_p = Q()
    filters_keys = list(filters.keys())

    for f in filter_str:
        if f[0] == 'p':
            s = f[1:]
            s = s.split('p')
            q_objs_p.add(filters['p'](int(s[0]), int(s[1]) + 1), Q.OR)
        if f in filters_keys:
            if f[0] == 'd':
                q_objs_d.add(filters[f](), Q.OR)
            elif f[0] == 'r':
                q_objs_r.add(filters[f](), Q.OR)
            elif f[0] == 'n':
                q_objs_n.add(filters[f](), Q.OR)
            elif f[0] == 'm':
                q_objs_m.add(filters[f](), Q.OR)
            elif f[0] == 'c':
                q_objs_c.add(filters[f](), Q.OR)
            elif f[0] == 'f':
                q_objs_f.add(filters[f](), Q.OR)
    q_l = [q_objs_d, q_objs_r, q_objs_n, q_objs_m, q_objs_c, q_objs_f, q_objs_p]
    print(q_l)
    q = Q()
    for f in q_l:
        q.add(f, Q.AND)
    args = dict()
    print(q)
    print(Phone.objects.filter(q).query)
    args["items"] = Phone.objects.filter(q)
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
    a = Phone.objects.aggregate(Max('price'), Min('price'))
    args['items'] = get_items(Phone)
    try:
        args['price_max'] = int(a['price__max'])
        args['price_min'] = int(a['price__min'])
    except TypeError:
        args['price_max'] = 0
        args['price_min'] = 0
    return render_to_response("phones/index.html", args)


def get_items(type):
    items = type.objects.all()
    return items


def item_phone(req, item='1'):
    args = dict()
    args["item"] = get_object_or_404(Phone, pk=item)
    return render_to_response("item_phone/index.html", args)


def like(req, item=''):
    if 'liked' not in req.session:
        item = get_item(item)
        item.likes += 1
        item.save()
        req.session.set_expiry(60)
        req.session['liked'] = True
        return HttpResponse(True)
    return HttpResponse(False)
