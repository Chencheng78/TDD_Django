from django.shortcuts import render, redirect
from lists.models import Item, List
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from lists.forms import ItemForm
# Create your views here.


def home_page(request):
    return render(request, 'home.html', {'form': ItemForm()})


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    form = ItemForm()
    if request.method == 'POST':
        form = ItemForm(data=request.POST)
        if form.is_valid():
            Item.objects.create(text=request.POST['text'], list=list_)
            return redirect(list_)
    return render(request, 'list.html', {'list': list_, 'form': form})


def new_list(request):
    form = ItemForm(data=request.POST)
    if form.is_valid():
        list_ = List.objects.create()
        Item.objects.create(text=request.POST['text'], list=list_)
        return redirect(list_)
    else:
        return render(request, 'home.html', {"form": form})
    # list_ = List.objects.create()
    # new_item_text = request.POST['text']
    # item = Item.objects.create(text=new_item_text, list=list_)
    # try:
    #     item.full_clean()
    #     item.save()
    # except ValidationError:
    #     list_.delete()
    #     error = "You can't have an empty list item"
    #     return render(request, 'home.html', {'error': error})
    # return redirect(list_)


# def add_item(request, list_id):
#     list_ = List.objects.get(id=list_id)
#     new_item_text = request.POST['item_text']
#     Item.objects.create(text=new_item_text, list=list_)
#     return redirect('/lists/%d/' % list_.id)