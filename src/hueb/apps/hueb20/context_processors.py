def menu(request):
    menu = []

    menu.append({"name": "Projekt", "link": "/", "disabled": False})

    if request.user.is_authenticated:
        menu.append({"name": "Suche", "link": "/search", "disabled": False})
    else:
        menu.append({"name": "Suche", "link": "#", "disabled": True})

    menu.append({"name": "Katalog", "link": "#", "disabled": True})

    context = {}
    context["menu"] = menu

    return context


def overlay(request, context={}):
    context = {}
    context["overlayOpen"] = False

    return context
