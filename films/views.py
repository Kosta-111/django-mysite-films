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
    list = '<ul>'
    for i in films:
        list += f'''
            <li>{i['name']} ({i['genre']}) - {i['author']['firstName']} {i['author']['lastName']}</li>
            '''
    list += "</ul>"

    return HttpResponse("<h1>Films Catalog!</h1>" + list)

# GET: details/id
def details(request, id):
    # create HTML response text
    info = '<div>'
    
    for i in films:
        if (i['id'] == id):
            film = i
            break

    info += f'''
            <p>{film['name']}</p>
            <p>{film['genre']}</p>
            <p>{film['author']['firstName']} {i['author']['lastName']}</p>
        '''
    info += "</div>"

    return HttpResponse("<h1>Film Details!</h1>" + info)
