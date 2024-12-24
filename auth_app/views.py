from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.
def sign_up_view(request):
    form=UserCreationForm()
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin_url')
    template_name='auth_app/signup.html'
    context={'form':form}
    return render(request,template_name,context)
    # return render(request ,template_name='auth_app/signup.html',context={'form':form})

def sign_in_view(request):
    if request.method=='POST':
        u=request.POST.get('un')   # un : - username 
        p=request.POST.get('pw')    # pw : - password
        user=authenticate(username=u,password=p)
        if user is not None:
            login(request,user)
            return redirect ('show_url')
        else:
        # If authentication fails, show an error message
            messages.error(request, "Invalid username or password.")
    
        #print(user)
        #print(u,'----->',p)
    template_name='auth_app/signin.html'
    context={}
    return render(request,template_name,context)

def sign_out_view(request):
    logout(request)
    return redirect('signup_url')



# def register(request):
#     pass