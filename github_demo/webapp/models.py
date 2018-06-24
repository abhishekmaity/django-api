from django.db import models

# Create your models here.

class show_image(models.Model):
    description= models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='static/image',blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'image'

# Method to add thumbnail on django-Admin
def admin_thumbnail(self):
    return '<img src="/%s" width="50" height="50" />' % (self.image)
    
admin_thumbnail.short_description = 'Thumbnail'
admin_thumbnail.allow_tags = True