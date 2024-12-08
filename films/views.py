from django.http import HttpResponse
from django.shortcuts import render, redirect
from films.forms import FilmCreate
from films.models import Film

# Create your views here.
""" films = [
  {
    "id": 1,
    "name": "Saw 2",
    "genre": "Horror",
    "year": 2005,
    "author": {
      "firstName": "Darren",
      "lastName": "Lynn",
      "country": "USA",
    },
    "website": "saw2.org",
    "budget": 10000000,
  },
  {
    "id": 2,
    "name": "Terminator",
    "genre": "Action",
    "year": 1984,
    "author": {
      "firstName": "James",
      "lastName": "Cameron",
      "country": "USA",
    },
    "website": "terminator.org",
    "budget": 20000000,
  },
  {
    "id": 3,
    "name": "Avatar",
    "genre": "Fantastic",
    "year": 2009,
    "author": {
      "firstName": "James",
      "lastName": "Cameron",
      "country": "USA",
    },
    "website": "avatar.org",
    "budget": 50000000,
  }
]
 """

def index(request):
    films = Film.objects.all
    return render(request, "index.html", {'films': films})


def upload(request):
    form = FilmCreate()
    if request.method == 'POST':
      form = FilmCreate(request.POST)
      if form.is_valid():
        form.save()
        return redirect('index')
      else:
        return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
      return render(request, "create_form.html", {'form': form})


def delete(request, id):
    film_id = int(id)
    try:
      film = Film.objects.get(id = film_id)
    except Film.DoesNotExist:
      return redirect('index')
    film.delete()

    return redirect('index')


def details(request, id):
    film_id = int(id)
    try:
      film = Film.objects.get(id = film_id)
    except Film.DoesNotExist:
      return redirect('index')
            
    return render(request, 'details.html', { 'film': film })
