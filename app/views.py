from django.shortcuts import render,redirect,HttpResponse
from django.core.mail import send_mail
from app.forms import ContactForm, RegisterForm,EmployeeForm
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
@login_required
def home(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Employee created Successfully..") 
    form = EmployeeForm()
    return render(request,"home.html",{"employee_form":form})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message']}
            message = "\n".join(body.values())
            send_mail(subject,message,'psarthaki348@gmail.com',['sarthaki228@gmail.com','sarthaki22345@gmail.com'])
            messages.success(request, "Message Sent..")
            return redirect("contact")
        messages.error(request,"ERROR:Message not Sent")
    form = ContactForm()
    return render(request, "contact.html", {'form': form})

def register_request(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # print("valid User")
            user = form.save()
            login(request,user)
            messages.success(request, "User Registration Successfully Done..!!")
            return redirect("home")
        messages.error(request,"Unsuccessful Registration..Please Try Later..")
        # print("Invalid User")
    form = RegisterForm()
    return render(request, "register.html",context={"register_form":form})

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username = username,password = password)
            if user is not None:
                login(request,user)
                messages.info(request,f"You are logged in as {username}")
                return redirect("home")
            else:
                # return HttpResponse("Credentials are Incorrect")
                messages.error(request, "Invalid Credentials..!")
        else:
            # return HttpResponse("Credentials are Incorrect")
            messages.error(request,"Invalid username and password..")
    form = AuthenticationForm()
    return render(request,"login.html",{"login_form":form})

def logout_user(request):
    logout(request)
    messages.info(request,"You have Succcssfully log out..!!")
    return redirect("login_user")

#----------------------------------------------------------------------------------------

def index(request):
    return HttpResponse("Hello world..welcome to Index page...")