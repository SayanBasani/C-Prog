'''
###  How to create a Django project from cmd  ###

step 1 :-active the variable envirment.Then move back to the folder.
step 2 :-type pip install 
step 3 :- once instalation is complet then check the the django is working by the below command .
            "django-admin
step 4 :- How to cheat, a Django project from eMD Step activate the rentual enribamenst then more book to the main folder.
Step-5 :- once the proje is completed . Move to the main django file using command 
            cd Project_Name

Step 6 :-Check this project is working of not by below commend 
            Python manage.Py runserver

Ster-7 To creat a New app in Project use the below comment
           django admin App_Name

Step-8 :- Once app is crreted  open
step 9 :- Create "url.py" inside your created application
step 10 :- inside the u r l dot pie ride the below code
            From Django.Urls import path
            From.import views
            urlpatterns=[
                path('home/',views.home),
            ]
Step 11 :- to make any logic or statement inside views.py file - make your logic or write your statement inside function .
Step 12 :- Inside url.py Of mean project include the app url
            from django.contrib import admin
            from django.urls import path,include
            urlpatterns = [
                path(' ',include('regform.urls'))
step 13 :- To use HTML and CSS code make a folder template inside your django folder where your main project app manage.py present.
            Also include the folder name (template) inside template section of select setting.py DTRS:[templet_name]

'''