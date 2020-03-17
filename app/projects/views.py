# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from projects.models import Project


def project_index(request):
	#a view to select all projects
    projects = Project.objects.all()
    return render(request, 'project_index.html', {'projects': projects})

def project_detail(request, pk):
	#view for the details of a project
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)
