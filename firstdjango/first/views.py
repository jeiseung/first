from django.shortcuts import render


# Create your views here.
def home(request):
    context = {'name': '이제승',
               'name2':'홍길동',
               'name3':'아무게', }

    return render(request, "first/home.html", context)
