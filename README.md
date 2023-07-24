# PollingApplication
<br> This is a Web Based Application built using Django Framework(Python) using Visual Studio IDE.
<br> This application is deployed in Render Web Server and PostgresSQL database is used.

# Instruction to use:
<br> After Clonning the application please follow following instructions:
<br> 1. In mysite/settings.py:
<br> Uncomment the default DATABASE and comment out the created DATABASE.
<br>
<br> 2.Open the folder in cmd and run : "env/scripts/activate" to activate virtual enviornment
<br> 3.Run "python manage.py runserver"
<br>
<br> 4. To access admin Previleges:
<br> Run "python manage.py createsuperuser"
<br> Enter the details asked and login through 'Admin' panel.
<br>
# Features:
<br> 1.Proper Authentication(Login/Logout)
<br> 2.Create Sessions to create a Question form for others to answer as a poll.
<br> 3.One user can answer only once thus maintaining the integrity of Polls.\
<br> 4.All the forms are SqlInjection protected.
<br> 5.Users can answer and see questions using session ids.
<br> 6.Results can be seen using the session ids.
<br> 7.A session remains active until the user is logged in.Once the user is logged out, the session can only be accessed for 
<br> answering not for adding questions.

# Features to come (V2.0):
<br> 1.Accessing old sessions and edit from where you left.
<br> 2.Dynamically see the poll results 
