from django.shortcuts import render
from .models import Menu, Item


def create_data(request):
    breakfast = Menu(101, 'Breakfast')
    item1 = Item(901, 'Poori', 50)
    item2 = Item(902, 'Idly', 40)
    item3 = Item(903, 'Sambhar', 40)
    item4 = Item(904, 'chatnee', 40)
    item5 = Item(905, 'samousa', 40)
    item6 = Item(905, 'vada', 40)
    breakfast.save()
    item1.save()
    item2.save()
    item3.save()
    item4.save()
    item5.save()
    item6.save()
    return render(request, 'home.html')


def display_menu(request):
    records = Menu.objects.all()
    return render(request, 'display.html', {'records': records})


def delete_menu(request):
    return render(request, 'delete.html')


def remove_menu_with_item(request):
    menu_name = request.POST['t1']
    Menu.objects.get(name=menu_name).delete()
    return render(request, 'home.html')

# Create your views here.
