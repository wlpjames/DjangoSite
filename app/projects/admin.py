# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from projects.models import Project

class ProjectsAdmin(admin.ModelAdmin):
	pass

admin.site.register(Project, ProjectsAdmin)