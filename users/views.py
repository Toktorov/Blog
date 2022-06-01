from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from django.contrib.auth import login, authenticate

