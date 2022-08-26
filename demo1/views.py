from django.shortcuts import render
from django.http import HttpResponse
def helloPage(request):
	return render(request, "demoPage.html")

