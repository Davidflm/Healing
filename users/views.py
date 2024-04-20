from django.shortcuts import render, redirect
from django.http import HttpResponse

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
      print('Erro 2')
      return redirect('/users/register')
    
    if len.senha < 6:
      print('Erro 3')
      return redirect('/users/register')
    
    return HttpResponse(f"{username} ---{email}----{senha}----{confirmar_senha}")