from django.shortcuts import render, redirect
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.db import IntegrityError
from django.contrib import messages
from Gen_AI_App.models import *
import openai

# Create your views here.
class HomeView(View):
    def get(self, request):
        return render(request, "home.html")

class SignupView(View):
    def get(self, request):
        return render(request, "signup2.html", {'form': None})

    def post(self, request):
        uname=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')

        uname = uname.lower()

        if not uname.strip() or not email.strip() or not password.strip():
            messages.error(request, 'Please fill out all the required fields.')
            return redirect('signup')

        try:
            user = User.objects.create_user(username=uname, email=email, password=password)
            user.save()
            messages.success(request, 'You have successfully signed up!')
            return redirect('login')
        except IntegrityError:
            messages.error(request, 'Username or email already exists. Please choose a different one.')
            return render(request, "signup2.html")

class LoginView(View):
    def get(self, request):
        return render(request, "login.html")

    


@method_decorator(login_required, name='dispatch')
class ChatBot(View):
    def get(self,request):
        data=chat_history.objects.all()
        username = request.user.username
        return render(request,"chat.html",{"data":data, "username": username})
    
    def post(self, request):
        username = request.user.username
        api_key = "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"
        openai.api_key = api_key

        def chat_with_gpt(prompt):
            response = openai.Completion.create(
                engine='text-davinci-003',
                prompt=prompt,
                max_tokens=2000,
                temperature=0.7,
                n=1,
            )
            model_reply = response.choices[0].text.strip()
            return model_reply
        
        que= request.POST.get("user-input")
        print(que)

        input = f"Answer me this question on the bases of Indian constitution:'{que}'"
        bot_response = chat_with_gpt(input)

        print(bot_response)

        data=chat_history.objects.all()
        chat_history(ques=que,ans=bot_response).save()

        return render(request,"chat.html",{"ans":bot_response,"data":data,"que":que, "username": username})
        # return JsonResponse({"ans": bot_response})


class LogoutView(View):
    def get(self, request):
        return redirect('home')

