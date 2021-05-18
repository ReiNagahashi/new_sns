from django.contrib import admin
from .models import Problem,ProblemLike

class ProblemLikeAdmin(admin.TabularInline):
    model = ProblemLike
class ProblemAdmin(admin.ModelAdmin):
    inlines = [ProblemLikeAdmin]
    list_display = ['__str__','author']
    search_fields = ['title','user__email']
    class Meta:
        model=Problem

admin.site.register(Problem,ProblemAdmin)
