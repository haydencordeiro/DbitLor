from typing import Text
from django.shortcuts import render
from .models import *
from .serializers import *
from django.shortcuts import render
from rest_framework import viewsets, mixins, generics
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
import datetime
import time
from rest_framework.parsers import JSONParser
from django.utils import timezone
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404, reverse
from django.http import (HttpResponse, HttpResponseNotFound, Http404,
                         HttpResponseRedirect, HttpResponsePermanentRedirect)
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import auth
import requests
from django.core.mail import send_mail
from rest_framework import status
from django.contrib.auth import authenticate, login
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib import messages
from datetime import datetime, date
from django.core.mail import send_mail
import json
from django.core.serializers.json import DjangoJSONEncoder
import os
from django.views.decorators.cache import cache_control
from django.db.models import Sum
import collections
import json
from datetime import date
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


# add user to group
# from django.contrib.auth.models import Group
# my_group = Group.objects.get(name='my_group_name')
# my_group.user_set.add(your_user)


# check if user exist in group


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None, **kwargs):
        if request.user.groups.filter(name="student").exists():  # is student
            try:
                user = StudentProfile.objects.get(user=request.user)
            except:
                return Response({'error': 'You Dont Have Permission To Access This'}, status=status.HTTP_400_BAD_REQUEST)
            serializer = StudentProfileSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:  # is teacher
            try:
                user = TeacherProfile.objects.get(user=request.user)
            except:
                return Response({'error': 'You Dont Have Permission To Access This'}, status=status.HTTP_400_BAD_REQUEST)
            serializer = TeacherProfileSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)


# Students

@api_view(('POST',))
@ permission_classes([IsAuthenticated])
def ApplyForLor(request):
    if request.user.groups.filter(name="student").exists():

        application = Application(
            student=StudentProfile.objects.filter(
                user=request.user).first(),
            teacher=TeacherProfile.objects.filter(
                user=User.objects.filter(id=request.data['teacherID']).first()).first(),
            status=Status.objects.get(status="pending")

        )
        application.save()
        return Response(ApplicationSerializer(application).data, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'You Dont Have Permission To Access This'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(('GET',))
@ permission_classes([IsAuthenticated])
def ListAllTeachers(request):
    if request.user.groups.filter(name="student").exists():
        teachers = TeacherProfile.objects.all()

        return Response(TeacherProfileSerializer(teachers, many=True).data, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'You Dont Have Permission To Access This'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(('GET',))
@ permission_classes([IsAuthenticated])
def LoggedInUsersApplications(request):
    if request.user.groups.filter(name="student").exists():
        application = Application.objects.filter(student=StudentProfile.objects.filter(
            user=request.user).first()).order_by('-date').order_by('-time')

        return Response(ApplicationSerializer(application, many=True).data, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'You Dont Have Permission To Access This'}, status=status.HTTP_400_BAD_REQUEST)


# Teachers

@api_view(('GET',))
@ permission_classes([IsAuthenticated])
def LoggedInTeachersApplications(request):
    if request.user.groups.filter(name="teacher").exists():
        application = Application.objects.filter(
            teacher=TeacherProfile.objects.filter(user=request.user).first())

        return Response(ApplicationSerializer(application, many=True).data, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'You Dont Have Permission To Access This'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(('POST',))
@ permission_classes([IsAuthenticated])
def LoggedInTeacherEditApplications(request):
    if request.user.groups.filter(name="teacher").exists():
        application = Application.objects.get(id=request.data['appID'])
        application.status = Status.objects.get(status=request.data['status'])
        application.save()

        return Response(ApplicationSerializer(application).data, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'You Dont Have Permission To Access This'}, status=status.HTTP_400_BAD_REQUEST)
