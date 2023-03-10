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
   Vacancy =models.IntegerField(default=1) # متاح كام مكان للناس تقدم ع الوظيفه
    
   salary = models.DecimalField(default=0.0 ,max_digits=6 ,decimal_places=2)
   
   category = models.ForeignKey('Category',on_delete=models.CASCADE)      # inside qoutes ''      because the class is after it not before     if before so no ''
   #        category  ---> One To One relasionship
   #? if we    ----->  make migrations      -----> will appear an error     because we must first make migrations for Category   to then  Can make the relasion.
   #? if that error appears to you   make COMMENT  for -->>  category = models.ForeignKey('Category',on_delete=models.CASCADE)   ,   And Delete  the file of it inside the folder migrations.
   
   
   experience =models.DecimalField(default=0.0 ,max_digits=6 ,decimal_places=2)
    
    
   def __str__(self):
       return self.title
  
     
class Category(models.Model):
   name= models.CharField(max_length=25)

   def __str__(self):
      return self.name