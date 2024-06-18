from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

#pour montrer la page des enseignants
def enseignants(request):
  template = loader.get_template('enseignants.html')
  return HttpResponse(template.render())
