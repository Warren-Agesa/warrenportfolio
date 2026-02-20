from django.contrib import admin
from .models import Hero, SocialProfile, About, Skill, Language, Hobby, Experience, Education, Certification, PortfolioCategory, PortfolioProject, Service, ContactMessage


@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(SocialProfile)
class SocialProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    
    def has_add_permission(self, request):
        # Only allow adding if no About instance exists
        return not About.objects.exists()

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'proficiency')

@admin.register(Hobby)
class HobbyAdmin(admin.ModelAdmin):
    list_display = ('name',)   


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'start_date', 'is_current')
    list_filter = ('is_current',)


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'school_name', 'start_date', 'is_current')
    list_filter = ('is_current',)


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ('name', 'issuer', 'issue_date')


@admin.register(PortfolioCategory)
class PortfolioCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')


@admin.register(PortfolioProject)
class PortfolioProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_featured', 'created_date')
    list_filter = ('category', 'is_featured')
    filter_horizontal = ('skills',)
    readonly_fields = ('created_date',)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    ordering = ('order',)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at', 'is_read')
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('created_at', 'name', 'email', 'subject', 'message')
    
    def has_add_permission(self, request):
        return False



   



