from django.shortcuts import render


def index(request):
    names_of_apps = [
        "Inventory",
        "Orders",
        "Authenticate",
    ]
    links_to_apps = ["inventory_list", "order_list", "user_login"]
    if request.user.is_authenticated:
        names_of_apps.append("Logout")
        links_to_apps.append("user_logout")
    apps = zip(names_of_apps, links_to_apps)
    print(names_of_apps)
    return render(
        request,
        "home/homepage.html",
        {"apps": apps},
    )
