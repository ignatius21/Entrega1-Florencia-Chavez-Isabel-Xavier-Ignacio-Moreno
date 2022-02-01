from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,authenticate
from django.shortcuts import redirect,render


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['username']
            contrasena = form.cleaned_data['password']
            user = authenticate(username=usuario,password=contrasena)
            if  user is not None:
                login(request,user)
                return redirect('inicio')
            else:
                return render(request,'login.html',{'form': form,'error':'Usuario o contraseña no validos'})

        else:
            return render(request,'login.html',{'form': form})    
    else:
        form = AuthenticationForm()
        return render(request,'login.html',{'form': form})    
