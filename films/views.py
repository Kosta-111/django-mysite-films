from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
films = [
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

def home(request):
    # create HTML response text
    return render(request, 'home.html', { 'films': films })

# GET: details/id
def details(request, id):
    # create HTML response text  
    for i in films:
        if (i['id'] == id):
            film = i
            break
            
    return render(request, 'details.html', { 'film': film })
