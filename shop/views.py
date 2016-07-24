from django.shortcuts import render_to_response, get_object_or_404, redirect, RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.db.models import Q, Max, Min
from shop.models import Slide, Phone, Tablet, Notebook, Items, ForHome, ForMaster, Category, Accessories, Share


def get_item(item_inv):
    if item_inv.isdigit:
        l = [list(x.objects.filter(inv=item_inv)) for x in (Phone, Tablet, Notebook, Accessories, ForMaster, ForHome, Share)]
        item = list()
        for x in l:
            item += x
        if item:
            return item[0]
        return False
    return False


def item(req, item=''):
    args = dict(item=get_item(item))
    if args['item']:
        shares = Share.objects.filter(gen_item__exact=args['item'].inv).only('sec_item', 'discount').values()
        if shares:
            args['shares'] = list()
            for obj in shares:
                args['shares'].append(dict(sec_item=get_item(str(obj['sec_item'])), discount=obj['discount'],
                                      inv=obj['inv']))
        return render_to_response('item_phone/index.html', args, context_instance=RequestContext(req))
    else:
        return redirect('general')


def tablet_filter(req, filter_str=""):
    if filter_str == "":
        args = dict()
        args["items"] = Tablet.objects.all()
        return render_to_response("filter_items/index.html", args, context_instance=RequestContext(req))
    filter_str = filter_str.split('-')
    filter_str.sort()
    filters = {
        "d1": lambda: (Q(diagonal__gte=6) & Q(diagonal__lte=7.7)),
        "d2": lambda: (Q(diagonal__gte=7.85) & Q(diagonal__lte=9.5)),
        "d3": lambda: (Q(diagonal__gte=9.6) & Q(diagonal__lte=10.1)),
        "d4": lambda: Q(diagonal__gt=10.1),

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
    q = Q()
    for f in q_l:
        q.add(f, Q.AND)
    args = dict()
    args["items"] = Tablet.objects.filter(q)
    return render_to_response("filter_items/index.html", args, context_instance=RequestContext(req))


def note_filter(req, filter_str=""):
    if filter_str == "":
        args = dict()
        args["items"] = Notebook.objects.all()
        return render_to_response("filter_items/index.html", args, context_instance=RequestContext(req))
    filter_str = filter_str.split('-')
    filter_str.sort()
    filters = {
        "d1": lambda: (Q(diagonal__gte=9) & Q(diagonal__lte=12.5)),
        "d2": lambda: Q(diagonal=13),
        "d3": lambda: (Q(diagonal__gte=14) & Q(diagonal__lte=15.6)),
        "d4": lambda: (Q(diagonal__gte=16) & Q(diagonal__lte=17)),

        "r1": lambda: Q(resolution__iexact="1900x1080"),
        "r2": lambda: Q(resolution__iexact="1366x768"),
        "r3": lambda: Q(resolution__iexact="1600x900"),

        "n1": lambda: Q(count_core__exact=1),
        "n2": lambda: Q(count_core__exact=2),
        "n3": lambda: Q(count_core__exact=4),
        "n4": lambda: Q(count_core__exact=8),
        "n5": lambda: Q(count_core__gt=8),

        "m1": lambda: Q(ram__lt=4096),
        "m2": lambda: (Q(ram__gte=4096) & Q(ram__lte=6144)),
        "m3": lambda: (Q(ram__gte=8192) & Q(ram__lte=10240)),
        "m4": lambda: Q(ram__gte=12288),

        "c1": lambda: Q(gpu__icontains='amd'),
        "c2": lambda: Q(gpu__icontains='nvidia'),

        "w1": lambda: Q(core_other__icontains='amd'),
        "w2": lambda: Q(core_other__icontains='intel'),

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
    q_objs_w = Q()
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
            elif f[0] == 'w':
                q_objs_w.add(filters[f](), Q.OR)
    q_l = [q_objs_d, q_objs_r, q_objs_n, q_objs_m, q_objs_c, q_objs_f, q_objs_p, q_objs_w]
    q = Q()
    for f in q_l:
        q.add(f, Q.AND)
    args = dict()
    args["items"] = Notebook.objects.filter(q)
    return render_to_response("filter_items/index.html", args, context_instance=RequestContext(req))


def phone_filter(req, filter_str=""):
    if filter_str == "":
        args = dict()
        args["items"] = Phone.objects.all()
        return render_to_response("filter_items/index.html", args, context_instance=RequestContext(req))
    filter_str = filter_str.split('-')
    filter_str.sort()
    filters = {
        "d1": lambda: (Q(diagonal__gte=6) & Q(diagonal__lte=7.7)),
        "d2": lambda: (Q(diagonal__gte=7.85) & Q(diagonal__lte=9.5)),
        "d3": lambda: (Q(diagonal__gte=9.6) & Q(diagonal__lte=10.1)),
        "d4": lambda: Q(diagonal__gt=10.1),

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
    q = Q()
    for f in q_l:
        q.add(f, Q.AND)
    args = dict()
    args["items"] = Phone.objects.filter(q)
    return render_to_response("filter_items/index.html", args, context_instance=RequestContext(req))



def search(req, search_str=""):
    args = dict()
    args['phones'] = Phone.objects.filter(name__icontains=search_str).only('name', 'inv')
    args['tablets'] = Tablet.objects.filter(name__icontains=search_str).only('name', 'inv')
    args['note'] = Notebook.objects.filter(name__icontains=search_str).only('name', 'inv')
    args['acs'] = Accessories.objects.filter(name__icontains=search_str).only('name', 'inv')
    args['home'] = ForHome.objects.filter(name__icontains=search_str).only('name', 'inv')
    args['master'] = ForMaster.objects.filter(name__icontains=search_str).only('name', 'inv')
    return render_to_response("search/index.html", args, context_instance=RequestContext(req))


def all_search(req, search_str=""):
    args = dict()
    l = [list(x.objects.filter(name__icontains=search_str)) for x in (Phone, Tablet, Notebook, Accessories, ForMaster, ForHome, Accessories)]
    res = list()
    for x in l:
        res += x
    del l
    args["items"] = res
    args["search_str"] = search_str
    return render_to_response("items/index.html", args, context_instance=RequestContext(req))


def other_category(req, category='', subcategory=''):
    args = dict()
    if category:
        if category == 'appliances':
            if subcategory:
                try:
                    args['items'] = ForHome.objects.filter(link_category_id=subcategory)
                    args['category'] = Category.objects.get(pk=subcategory)
                except (ForHome.DoesNotExist, Category.DoesNotExist):
                    args['items'] = ForHome.objects.all()
                    args['category'] = 'Бытовая техника'
            else:
                args['items'] = ForHome.objects.all()
                args['category'] = 'Бытовая техника'
            args['cat'] = 'appliances'
            args['subcategory'] = Category.objects.filter(variant=3)
        elif category == 'master-tools':
            if subcategory:
                try:
                    args['items'] = ForMaster.objects.filter(link_category_id=subcategory)
                    args['category'] = Category.objects.get(pk=subcategory)
                except (ForMaster.DoesNotExist, Category.DoesNotExist):
                    args['items'] = ForMaster.objects.all()
                    args['category'] = 'Всё для мастера'
            else:
                args['items'] = ForMaster.objects.all()
                args['category'] = 'Всё для мастера'
            args['subcategory'] = Category.objects.filter(variant=2)
            args['cat'] = 'master-tools'
        elif category == 'accessories':
            if subcategory:
                try:
                    args['items'] = Accessories.objects.filter(link_category_id=subcategory)
                    args['category'] = Category.objects.get(pk=subcategory)
                except (ForMaster.DoesNotExist, Category.DoesNotExist):
                    args['items'] = ForMaster.objects.all()
                    args['category'] = 'Акссесуары и Комплектующие'
            else:
                args['items'] = Accessories.objects.all()
                args['category'] = 'Акссесуары и Комплектующие'
            args['subcategory'] = Category.objects.filter(variant=1)
            args['cat'] = 'accessories'
        return render_to_response('items/index.html', args, context_instance=RequestContext(req))
    else:
        return redirect('general')


def phones_search(req, search_str=""):
    args = dict()
    args['items'] = Phone.objects.filter(name__icontains=search_str)
    return render_to_response("phones/index.html", args, context_instance=RequestContext(req))


def general(req):
    args = dict()
    args['slides'] = Slide.objects.all()
    l = [list(x.objects.order_by('-date')[:4]) for x in (Phone, Tablet, Notebook)]
    news = list()
    for x in l:
        news += x
    del l
    news.sort(key=lambda i: i.date, reverse=True)
    args['new_items'] = news
    del news
    l = [list(x.objects.order_by('-likes')[:4]) for x in (Phone, Tablet, Notebook)]
    populars = list()
    for x in l:
        populars += x
    populars.sort(key=lambda i: i.likes, reverse=True)
    args["pop_items"] = populars
    return render_to_response('general/index.html', args, context_instance=RequestContext(req))


def phones(req):
    args = dict()
    a = Phone.objects.aggregate(Max('price'), Min('price'))
    args['items'] = Phone.objects.all()
    try:
        args['price_max'] = int(a['price__max'])
        args['price_min'] = int(a['price__min'])
    except TypeError:
        args['price_max'] = 0
        args['price_min'] = 0
    return render_to_response("phones/index.html", args, context_instance=RequestContext(req))


def tablets(req):
    args = dict()
    a = Tablet.objects.aggregate(Max('price'), Min('price'))
    args['items'] = Tablet.objects.all()
    try:
        args['price_max'] = int(a['price__max'])
        args['price_min'] = int(a['price__min'])
    except TypeError:
        args['price_max'] = 0
        args['price_min'] = 0
    return render_to_response("tablets/index.html", args, context_instance=RequestContext(req))


def notes(req):
    args = dict()
    a = Notebook.objects.aggregate(Max('price'), Min('price'))
    args['items'] = Notebook.objects.all()
    try:
        args['price_max'] = int(a['price__max'])
        args['price_min'] = int(a['price__min'])
    except TypeError:
        args['price_max'] = 0
        args['price_min'] = 0
    return render_to_response("notes/index.html", args, context_instance=RequestContext(req))


def item_phone(req, item='1'):
    args = dict()
    args["item"] = get_object_or_404(Phone, pk=item)
    return render_to_response("item_phone/index.html", args, context_instance=RequestContext(req))


def like(req, item=''):
    if 'like' not in req.session:
        item = get_item(item)
        item.likes += 1
        item.save()
        req.session.set_expiry(100)
        req.session['like'] = True
        return HttpResponse(True)
    return HttpResponse(False)


@csrf_exempt
def add_basket(req):
    if req.method == 'POST':
        new_item = int(req.POST['item'])
        item_count = int(req.POST['count'])
        print(new_item, item_count)
        if not ('basket' in req.session):
            req.session['basket'] = ()
            req.session['item_count'] = ()
        if new_item not in req.session['basket']:
            req.session['basket'] += (new_item,)
            req.session['item_count'] += (item_count,)
        else:
            pos = req.session['basket'].index(new_item)
            a = req.session['item_count']
            a = list(a)
            a[pos] = item_count
            req.session['item_count'] = tuple(a)
        print(req.session['basket'])
        print(req.session['item_count'])
    return HttpResponse()
