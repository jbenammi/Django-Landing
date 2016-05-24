from django.shortcuts import render

def index(request):
    context = {
    	'name': 'Jonathan Ben-Ammi',
    	'like': 'Watch Movies',
    	'lang': 'PHP',
    	}
    return render(request, 'home/home_index.html', context)