from django.shortcuts import render
from django.http import HttpResponse

from .models import Form_Response, Team

# Create your views here.

def page_submit(request):
    return render(request, "recruit_app/page_form.html")

def submit(request):
    data = request.POST
    teams = {"Aero":1, "Baja":2, "FSAE":4, "EFSAE":8}
    
    try:
        program_resp = data['program'] if data['program'] != "other" else data['other']
        resp = Form_Response( \
            first_name = data['first_name'], \
            last_name = data['last_name'], \
            email = data['email'], \
            program = program_resp, \
            year = int(data['year']))
        resp.save()


        t = Team.objects
        interests_resp = sum([int(x) for x in data.getlist('interests')])

        for team in teams:
            if(interests_resp & teams[team]):
                resp.interests.add(t.filter(team_name=team)[0])

    except KeyError:
        return HttpResponse("Strange error encountered. (KeyError)")

    return render(request, "recruit_app/page_submitted.html")
