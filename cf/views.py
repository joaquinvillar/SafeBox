from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import generic
from rest_framework import generics

from cf.forms import KeyForm, SafeBoxForm
from cf.serializers import SafeBoxSerializer, KeySerializer
from .models import SafeBox, Key
from django.http import HttpResponse
from wsgiref.util import FileWrapper
# Create your views here.


class Index(generic.View):
    model = SafeBox
    template_name = 'cf/index.html'
    context_object_name = 'list'

    @method_decorator(login_required)
    def get(self, request):
        data = []
        s_box = SafeBox.objects.all()
        for box in s_box:
            boxes = {}
            boxes['id'] = box.id
            boxes['name'] = box.name
            keys = Key.objects.filter(safe_box=box.id)

            ke = []
            for key in keys:
                k = {}
                if key.document:
                    k[key.description] = key.document.url
                else:
                    k[key.description] = 'No tiene imagen'
                ke.append(k)
            boxes['key'] = ke
            data.append(boxes)
        sal = {}
        form = KeyForm()
        sal['data'] = data
        sal['form'] = form
        return render(request, self.template_name, sal)


def download(request):

    data = request.body
    post_text = request.POST.get('item')
    file = Key.objects.get(document=data)
    # response = HttpResponse(FileWrapper(file.document, content_type='application/zip')
    # response['Content-Disposition'] = 'attachment; filename=myfile.zip'
    return None


class SafeBoxList(generics.ListCreateAPIView):
    queryset = SafeBox.objects.all()
    serializer_class = SafeBoxSerializer


class SafeBoxDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SafeBox.objects.all()
    serializer_class = SafeBoxSerializer


class KeyList(generics.ListCreateAPIView):
    queryset = Key.objects.all()
    serializer_class = KeySerializer


class KeyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Key.objects.all()
    serializer_class = KeySerializer


def model_form_upload(request):
    if request.method == 'POST':
        form = KeyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cf:index')
    else:
        form = KeyForm()
    return render(request, 'cf/index.html', {
        'form': form
    })


def safe_box_form(request):
    if request.method == 'POST':
        form = SafeBoxForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cf:index')
    else:
        form = SafeBoxForm()
    return render(request, 'cf/new_safe_box.html', {
        'form': form
    })