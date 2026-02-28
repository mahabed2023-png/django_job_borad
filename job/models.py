from django.db import models

from django.utils.text import slugify
# Create your models here.


'''
  -django model field :
  -html widget
  -validation
  -db size
'''

JOb_TYPE = (
    ('full time','full time'),
    ('part time','part time')
)

def image_upload(instance,filename):
    imagename , extension = filename.split('.')
    return 'jobs/%s.%s'%(instance.id,extension)


class job(models.Model): #table 
    title = models.CharField(max_length=100) #column
    # location
    job_type = models.CharField(max_length=15,choices=JOb_TYPE)
    description = models.TextField(max_length=1000)
    puplished_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_upload)
    
    slug = models.SlugField(blank=True , null=True)        
    
    def save(self, *args, **kwargs):
        self.slug =slugify(self.title)
        super(job, self).save(*args, **kwargs)
    
    
    
    def __str__(self):
        return self.title
    
class Category(models.Model):
    name = models.CharField(max_length=25)
    
    def __str__(self):
        return self.name