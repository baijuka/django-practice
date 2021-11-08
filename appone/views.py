from django.shortcuts import render

# Create your views here.

fruits = [
    { 'id':'1',
      'name':'Banana',
      'price':1.50,
      'origin':'Brazil'
    },
    {
        'id':'2',
        'name':'Pineapple',
        'price':2.00,
        'origin': 'Costorica'
    },
    {
        'id':'3',
        'name':'Orange',
        'price':1.25,
        'origin':'Spain'
    },
     {
        'id':'4',
        'name':'Melon',
        'price':3.25,
        'origin':'India'
    }
]

def home(request):
    return render(request,'appone/home.html')

def about(request):
    context = {'item': fruits}
    return render(request,'appone/about.html', context)

def detail(request, pk):
    detailobject = None
    for i in fruits:
        if i['id'] == str(pk):
            detailobject = i
    return render(request, 'appone/detail.html', {'item':detailobject})

