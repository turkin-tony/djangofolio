#-*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from models import Project
# Create your views here.

def view_project(request, project_slug):
    args={}
    args.update(csrf(request))
    project = Project.objects.get(project_slug=project_slug)
    args['project'] = project
    return render_to_response('project.html', args)
