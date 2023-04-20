from django.db import models

from django.utils.text import slugify
from django.contrib.auth.models import User


'''
 ? django model field : 
    - html widget
    - validation 
    - db size 
'''

JOB_TYPE = (                     # **
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)

#?  For media folder
#                the photo
def image_upload(instance,filename): ###
    imagename , extension = filename.split(".")
    return "jobs/%s.%s"%(instance.id,extension)


class Job(models.Model):  # table 
    owner = models.ForeignKey(User, related_name='job_owner', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)  # column
    # location                                  # **
    job_type = models.CharField(max_length=15 , choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    Vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1) 
             
#                        ?  on_delete=models.CASCADE  -->  if delete the category delete the jobs too.         (, ,related_name='job_category'  -->  for get all jobs in category ).
    category = models.ForeignKey('Category',on_delete=models.CASCADE) # 1 to many relation --> 1 category have many jobs , 1 job have 1 category. 
#                        *     'Category'  --> in '' because Category is not defined yet.   python is Interpreter read the code from top to bottom.

#!   if error ecoured when "Migrating" after the Relation  ---->  1) delete the migration_file.   2) comment the relation  and "Migrate firstlly" the tabel which you need to relate with.

    image = models.ImageField(upload_to=image_upload)  ###?   fro media folder that user upload in

    slug = models.SlugField(blank=True, null=True)


    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)
        super(Job,self).save(*args, **kwargs)


    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name



class Apply(models.Model):
    job = models.ForeignKey(Job, related_name='apply_job', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    webiste = models.URLField()
    cv = models.FileField(upload_to='apply/')
    cover_letter = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name