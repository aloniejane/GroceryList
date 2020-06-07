from django.shortcuts import render, redirect
from List.models import UserList


# Create your views here.
def home(request):
    items = UserList.objects.all()
    if request.POST:
        itm = request.POST["itm"]
        return render(request, "Main.html", {"items": items, "itm1": itm})
    else:
        return render(request, "Main.html",{"items":items})


def add_list(request):
    cur_item=request.POST["item"]
    if request.POST["quantity"]:
        cur_quan=request.POST["quantity"]
    else:
        cur_quan=1
    UserList.objects.create(item=cur_item,quantity=cur_quan)
    return redirect(home)

def delete(request,id):
    UserList.objects.get(id=id).delete()
    return redirect(home)

def save_state(request,id):
    if request.method == 'POST':
        user = UserList.objects.get(id=id)
        if user.check==False:
            user.check =True
        else:
            user.check =False
        user.save()
    return redirect(home)









