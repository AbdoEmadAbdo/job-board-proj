from django.db import models

'''
Django model field :
   -html widget
   -validation
   -db size
'''

JOB_TYPE = (
   ('full time','full time'),
   ('part time','part time'),                                                                                                           
)

class Job(models.Model):
    title = models.CharField(max_length=100)  # column
    #location = models.CharField(max_length=50)
    
    job_type = models.CharField(max_length=15 ,choices=JOB_TYPE)    #full time or half time
    description = models.TextField(max_length=1000)
    
    published_at =models.DateTimeField(auto_now=True)
    Vacancy =models.IntegerField(default=1)
    
    salary = models.DecimalField(default=0.0 ,max_digits=6 ,decimal_places=2)
    #category =models.CharField(max_length=100)
    
    experience =models.DecimalField(default=0.0 ,max_digits=6 ,decimal_places=2)
    
    
    def __str__(self):
        return self.title