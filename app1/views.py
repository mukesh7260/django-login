from django.shortcuts import render,redirect
from . forms import CustomerForm
from . models import Customer
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='signin_url')
def add_view(request):
    form=CustomerForm()
    if request.method=='POST':
        form=CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
            
    template_name='app1/add.html'
    context={'form':form}
    return render(request,template_name,context)

@login_required(login_url='signin_url')
def show_view(request):
    obj=Customer.objects.all()
    template_name='app1/show.html'
    context={'data':obj}
    return render(request,template_name,context)

def update_view(request,pk): 
   obj=Customer.objects.get(id=pk)
   form=CustomerForm(instance=obj)
   if request.method=='POST':
       form=CustomerForm(request.POST,instance=obj)
       if form.is_valid():
            form.save()
            return redirect('show_url')
   template_name='app1/add.html'
   context={'form':form}
   return render(request,template_name,context)
   
def delete_view(request,pk):
    obj=Customer.objects.get(id=pk)
    if request.method=='POST':
        obj.delete()
        return redirect('show_url')
    template_name='app1/delete.html'
    context={'data':obj}
    return render(request,template_name,context)
  