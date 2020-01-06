from django.shortcuts import render,redirect
from contact.forms import MessageForm
from django.views.generic import TemplateView

# Create your views here.
class Contact(TemplateView):
    template_name='contact.html'

    def get(self,request):
        form = MessageForm()
        return render(request, self.template_name,{'form':form})

    def post(self,request):
        form= MessageForm(request.POST)
        if form.is_valid():
            form.save()
            form= MessageForm()
            return render(request,template_name='success.html')
        args={
            'form':form,

        }
        return render(request,self.template_name,args)
        

    