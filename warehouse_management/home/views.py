from django.shortcuts import render


def index(request):
    names_of_apps = [
        "Inventory",
        "Orders",
        "Authenticate",
    ]
    links_to_apps = ["inventory_list", "order_list", "user_login"]
    apps = zip(names_of_apps, links_to_apps)
    print(names_of_apps)
    return render(
        request,
        "home/homepage.html",
        {"apps": apps},
    )
