from django.shortcuts import render
from .models import *
# from django. import MultiValueDictKeyError
from django.utils.datastructures import MultiValueDictKeyError
from django.views.decorators.csrf import csrf_protect
from mysql.connector import cursor
from django.db import connection
from django.http import Http404 #for error

from .serializer import MymodelSerializer   #import the model serializer
from rest_framework import viewsets,status  #status - for show the http error status
from rest_framework.views import APIView    #for api view of the drf
from rest_framework.response import Response    #for give responce in http view 
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view


# Create your views here.

def homeo(request):
    return render(request,'home.html')

#Class Based view

#create data through api
class createclass(APIView):
    def post(self,request,**args):  #for post the data ,**args when unknown number of arguments as here are the fields
        serializer = MymodelSerializer(data=request.data)   #go to model serialzer and then request the fields from that and create the data 
        
        if serializer.is_valid(): #check if valid data or fields
            serializer.save()   # save it to database
            return Response(serializer.data,status=status.HTTP_201_CREATED) #return the http response to the user.
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST) #same
    
    
# @api_view(['GET'])
#read the data of given id -GET method
class readclass(APIView):
    def get(self,request,task_id):  # get method to read data
        #this can also be done
        # instance = tasks.objects.get(id=task_id)
        # serializer = MymodelSerializer(instance)
        # return Response(data=instance,status=status.HTTP_200_OK)
    
        try:    #better to use try and except
            task = tasks.objects.get(pk=task_id)   #get the  data of pk(primary Key) as task_id, 
            serializer = MymodelSerializer(task)    #serialize the fetched data 
            return Response(serializer.data)        #Response- for http response view. 

        except tasks.DoesNotExist:      #if the given id's data not found then
            return Response({"detail": "Task not found"}, status=status.HTTP_404_NOT_FOUND)     #http error message

class getall(APIView):
    def get(self,request):
        task = tasks.objects.all()
        serializer = MymodelSerializer(task,many=True)
        return Response(serializer.data)  
        
#Patch or update the data    
class updateclass(APIView):
    def patch(self,request,task_id,**args): #petch method to update the perticular task_id
        try:
            t = tasks.objects.get(pk=task_id)   #get the task_id data to update
            serializer = MymodelSerializer(instance=t, data=request.data, partial=True) #instance - which object to be updatede
                                                                                        #data=request.data - provides the new data
                                                                                        #partial=True - means not all the fileds in the model are requred to update
            if serializer.is_valid():
                serializer.save()   #if valid then save the object
                return Response("Tasks updated successfully",status=status.HTTP_201_CREATED)    #response the success http 
        except tasks.DoesNotExist:
            raise Http404("Task does not exist")   #if not got the data then http errror message.
        
# Delete the data 
class deleteclass(APIView):
    def delete(self,request,task_id):   #delete the given task_id data
        try:
            t = tasks.objects.get(pk=task_id).delete()      #get the data of the task_id and delete()
            return Response(f"Task is deleted successfully",status=status.HTTP_200_OK)      #Response- for http response of success message
        except tasks.DoesNotExist:
            raise Http404("Task does not exist")
        
        
        
        
# CREATE for HTML view
 
# @csrf_protect
# def home(request):
#     if request.method == 'POST':
#         title = request.POST['title']
#         description=request.POST['description']
#         duedate=request.POST['duedate']
#         try:
#             is_completed = request.POST['iscompleted']
#         except MultiValueDictKeyError:
#             is_completed = False
#         # is_completed=request.POST['is_completed']
#         # if is_completed == 'on':
#         #     is_completed = True
#         # else:
#         #     is_completed = False
#         task = tasks.objects.create(title=title,description=description,duedate=duedate,iscompleted=is_completed)
#         task.save()
#         return redirect('/')
#     return render(request,'index.html')



#READ for html view

# def show(request, task_id):
#     # Retrieve the task using the task_id
#     try:
#         task = tasks.objects.get(id=task_id)
#     except tasks.DoesNotExist:
#         # Handle the case where the task doesn't exist (you can raise a 404 or redirect)
#         # For example, you can use Django's Http404 exception
#         raise Http404("Task does not exist")

#     # Pass the task details to the template or handle them as needed
#     context = {'task': task}
#     return render(request, 'view.html', context)







