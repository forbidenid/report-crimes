from django.shortcuts import render
from . forms import ComplainForm
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from . models import Complaint
from django.views.generic import CreateView, FormView, ListView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from . serializers import ComplaintSerializer
from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response


class RegisterComplaint(SuccessMessageMixin, CreateView):
    form_class = ComplainForm
    template_name = 'complaints/new_complaint.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.seen_by = None
        form.save()

        messages.success(self.request,
                         'Your complaint was registered successfully, one of our correspondents would soon get back to you')

        return HttpResponseRedirect(reverse('accounts:dashboard'))


class ListComplaints(ListView):
    model = Complaint
    template_name = 'complaints/all_complaints.html'


class DetailComplaints(DetailView):
    model = Complaint
    template_name = 'complaints/complaints_detail.html'

    def update_seen_by(self):
        self.object.seen_by = self.request.user
        print(str(self.object))




class ComplaintView(viewsets.ModelViewSet):
    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer

    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        return Response("ok")


class ComplaintList(generics.ListAPIView):
    serializer_class = ComplaintSerializer


    def get_queryset(self):
        user = self.request.user
        return Complaint.objects.filter(created_by=user)
