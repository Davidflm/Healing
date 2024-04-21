from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages

# Create your views here.
def registry(request):
  if request.method == 'GET':
    return render(request, 'registry.html')
  elif request.method == 'POST':
    username = request.POST.get('username')
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    confirmar_senha = request.POST.get('confirmar_senha')
    
    if senha != confirmar_senha:
      messages.add_message(request, constants.ERROR, 'Senha e confirmar Senha devem possuir valores iguais')
      return redirect('/users/register')
    
    users = User.objects.filter(username=username)
    
    if users.exists():
      messages.add_message(request, constants.ERROR, 'Já existe um usuário com esse login em nossa base de dados!')
      return redirect('/users/register')
    
    if len(senha) < 6:
      messages.add_message(request,constants.ERROR, "A senha deve possuir 6 ou mais digitos!")
      return redirect('/users/register')
    
    user = User.objects.create_user(
      username=username,
      email=email,
      password=senha,
    )
    
    return redirect('/users/login')