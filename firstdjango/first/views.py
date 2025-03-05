from django.shortcuts import render


# Create your views here.
def home(request):
    context = {"name": "떡볶이",
               "hobby": "고추장",
               "interest": "계란",
                 }

    return render(request, "first/home.html", context)
