#-*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect, HttpResponse
from django.core.context_processors import csrf
from folio.models import Project

def home(request):
    args={}
    args.update(csrf(request))
    projects = Project.objects.all()
    args['projects'] = projects
    return render_to_response('index.html', args)
