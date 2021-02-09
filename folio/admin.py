from django.contrib import admin
from models import Project, ProjectTags, ProjectGallery

# Register your models here.

class ProjectTagsInLines(admin.StackedInline):
    model = ProjectTags
    extra = 0

class ProjectGalleryInLines(admin.StackedInline):
    model = ProjectGallery
    extra = 0

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectTagsInLines, ProjectGalleryInLines]
    prepopulated_fields = {'project_slug': ('project_name',)}

admin.site.register(Project, ProjectAdmin)
