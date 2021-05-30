from django.shortcuts import render
from django.http import HttpResponse
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


def index(request):
    data = {'title': 'Main page'}
    return render(request, 'main/index.html', data)


def about(request):
    data = {'title': 'About'}
    return render(request, 'main/about.html', data)


first_time = True


def stats(request):
    global first_time
    if first_time:
        cred = credentials.Certificate('credentials.json')
        firebase_admin.initialize_app(cred)
        first_time = False

    db = firestore.client()
    users_ref = db.collection(u'TrashCount')
    docs = users_ref.stream()

    aluminium = []
    glass = []
    plastic = []
    paper = []
    for doc in docs:
        values = doc.to_dict()
        aluminium.append(values['aluminium'])
        glass.append(values['glass'])
        plastic.append(values['plastic'])
        paper.append(values['paper'])

    data = {'title': 'Stats',
            'aluminium': sum(aluminium),
            'glass': sum(glass),
            'plastic': sum(plastic),
            'paper': sum(paper)
            }
    return render(request, 'main/stats.html', data)
