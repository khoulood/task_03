from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = { "my_list": [ {"restaurant_name":"albaik","food_type":"spaicy"},
                             {"restaurant_name":"pizza hot","food_type":"margrita"},
                             {"restaurant_name":"steak house","food_type":"spaicy"},
                            ],

               }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = { 
             "my_object": {"restaurant_name":"albaik","food_type":"spaicy"},

    }
    return render(request, 'detail.html', context)
