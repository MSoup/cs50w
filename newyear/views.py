from django.shortcuts import render
from datetime import datetime

# Create your views here.
def index(request):
    newyear = False
    now = datetime.now()
    month = now.month
    day = now.day

    if month == 1 and day == 1:
        newyear = True

    return render(request, "newyear/index.html", {
        "newyear": newyear
    })