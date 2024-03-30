from django.db import models

# Create your models here.
class tasks(models.Model):  
    title=models.CharField(max_length = 50)
    description=models.CharField(max_length=150)
    duedate=models.DateField()
    iscompleted=models.BooleanField(default=False)
    
    # def __int__(self) :
    #     return self.id
    # def __int__(self) :
    #     return self.id
    
    class meta:
        db_table="myapp_tasks"
    
