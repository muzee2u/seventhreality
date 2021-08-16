import json

from django.shortcuts import render
from RD_Projects.models import *
from django.http import HttpResponse, JsonResponse
import json

from django.core import serializers

# Create your views here.
def project_domains(request):
    domains = Project.objects.all()
    dict_obj = {'domains': domains}
    return render(request, 'RD_Projects/projects-Domain.html', dict_obj)


def projects_all(request):
    domains = productDomain.objects.all()
    projects = Project.objects.all()
    dict_obj = {'domains': domains, 'projects': projects}
    return render(request, 'RD_Projects/projects-all.html', dict_obj)


# def project_single(request, id):
#     project = Project.objects.filter(id=id)
#     print(project)
#     dict_obj = {'project': project}
#     return render(request, 'RD_Projects/project-single.html', dict_obj)

def project_single(request, id):
    project = Project.objects.filter(id=id)
    print(project)
    dict_obj = {'project': project}
    return HttpResponse("Success")


def service_single(request, id):
    project = Project.objects.filter(id=id)
    print(project)
    dict_obj = {'project': project}
    return HttpResponse("Success")


def services(request):
    domains = serviceDomain.objects.all()
    services = Service.objects.all()
    dict_obj = {'domains': domains, 'services': services}
    return render(request, 'RD_Projects/services.html', dict_obj)


# def service_single(request, id):
#     service = Service.objects.filter(id=id)
#     dict_obj = {'service': service}
#     return render(request, 'RD_Projects/service-single.html', dict_obj)


def get_project_detail(request):
    id = request.GET['id']
    project = Project.objects.filter(id=id)
    tmpJson = serializers.serialize("json",project)
    tmpObj = json.loads(tmpJson)

    return HttpResponse(json.dumps(tmpObj))


def get_service_detail(request):
    id = request.GET['id']
    service = Service.objects.filter(id=id)
    tmpJson = serializers.serialize("json",service)
    tmpObj = json.loads(tmpJson)

    return HttpResponse(json.dumps(tmpObj))
