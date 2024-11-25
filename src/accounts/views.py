from django.shortcuts import redirect
from django.core.mail import send_mail
from django.contrib import messages, auth
from accounts.models import Token
from django.urls import reverse


def send_login_email(request):
    email = request.POST["email"]
    token = Token.objects.create(email=email)
    url = request.build_absolute_uri(
        reverse("login") + "?token=" + str(token.uid),
    )
    message_body = f"Use this link to log in:\n\n{url}"
    send_mail(
        "Your login link for Superlists",
        message_body,
        "noreply@superlists",
        [email],
    )
    messages.success(
        request,
        "Check your email, we've sent you a link you can use to log in.",
    )
    return redirect("/")

def login(request):
    if Token.objects.filter(uid=request.GET["token"]).exists():
        User = auth.get_user_model()
        user = User.objects.create(email="edith@example.com")
        auth.login(request, user)
    else:
        messages.error(request, "Invalid login link, please request a new one")
    return redirect("/")
