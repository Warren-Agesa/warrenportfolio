from django.db import models


class Hero(models.Model):
    name = models.CharField(max_length=100)
    roles = models.CharField(
        max_length=255,
        help_text="Comma separated values e.g Designer, Developer, Freelancer"
    )
    background_image = models.ImageField(
        upload_to='images/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name


class SocialProfile(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField()
    icon_class = models.CharField(
        max_length=100,
        help_text="Example: bi bi-github"
    )

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=50)
    proficiency = models.PositiveSmallIntegerField(default=50, help_text="Proficiency % (0-100)")

    def __str__(self):
        return f"{self.name} ({self.proficiency}%)"

class Hobby(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class About(models.Model):
    name = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='about/', blank=True, null=True)
    short_intro = models.TextField(help_text="A brief 1-2 sentence intro")
    description = models.TextField(help_text="Full detailed description")
    birthday = models.DateField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    cv_file = models.FileField(upload_to='cv/', blank=True, null=True)

    skills = models.ManyToManyField(Skill, blank=True)
    hobbies = models.ManyToManyField(Hobby, blank=True)
    social_profiles = models.ManyToManyField(SocialProfile, blank=True)
    languages = models.ManyToManyField(Language, blank=True)

    def __str__(self):
        return self.name

class Experience(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    is_current = models.BooleanField(default=False, help_text="Check if currently working here")
    description = models.TextField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-order', '-end_date']

    def __str__(self):
        return f"{self.title} at {self.company}"


class Education(models.Model):
    school_name = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    field_of_study = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    is_current = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-order', '-end_date']

    def __str__(self):
        return f"{self.degree} from {self.school_name}"


class Certification(models.Model):
    name = models.CharField(max_length=100)
    issuer = models.CharField(max_length=100)
    issue_date = models.DateField()
    expiry_date = models.DateField(blank=True, null=True)
    credential_url = models.URLField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-order', '-issue_date']

    def __str__(self):
        return f"{self.name} - {self.issuer}"


class PortfolioCategory(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name_plural = "Portfolio Categories"

    def __str__(self):
        return self.name


class PortfolioProject(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    short_description = models.CharField(max_length=255, blank=True, null=True)
    category = models.ForeignKey(PortfolioCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name='projects')
    featured_image = models.ImageField(upload_to='portfolio/')
    project_url = models.URLField(blank=True, null=True, help_text="Link to live project")
    github_url = models.URLField(blank=True, null=True, help_text="Link to GitHub repository")
    skills = models.ManyToManyField(Skill, blank=True)
    created_date = models.DateField(auto_now_add=True)
    order = models.PositiveIntegerField(default=0)
    is_featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['-order', '-created_date']

    def __str__(self):
        return self.title


class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon_class = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Bootstrap icon class, e.g., bi bi-code-slash"
    )
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.subject} - {self.name}"

