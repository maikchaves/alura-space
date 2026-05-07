MENU_ITEMS = [
    {
        "url_name": "home",
        "label": "Home",
        "icon": "Home",
    },
    {
        "url_name": "add_image",
        "label": "Nova imagem",
        "icon": "Novas",
    },
    {
        "url_name": "#",
        "label": "Mais vistas",
        "icon": "Mais vistas",
        "disabled": True,
    },
    {
        "url_name": "#",
        "label": "Surpreenda-me",
        "icon": "Surpreenda-me",
        "disabled": True,
    },
]


def menu_items(request):
    return {
        "menu_items": MENU_ITEMS
    }