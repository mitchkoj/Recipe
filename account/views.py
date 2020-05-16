from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.conf import settings
# from django.views.generic import CreateView

from .models import CustomUser
from .forms import CustomUserCreationForm
from .tokens import account_activation_token

from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

# ____ EMAIL SETUP ___#
from django.core.mail import send_mail



def gate_keeper(request):
    """
        method to verify user status.
    """
    user = request.user
    lock = dict()

    if user.is_authenticated:
        lock['email_confirmed'] = user.email_confirmed
    else:
        return redirect("home")

    lock_keys = {
        'email_confirmed': "reconfirm_email",
    }

    lock_key = get_false_key(lock)
    return redirect(lock_keys.get(lock_key, "home"))


def process_user_creation(request, is_creator=False):
    """
        method to process user form and add new user
    """
    form = CustomUserCreationForm(request.POST)
    if form.is_valid():
        user = form.save(commit=False)
        user.is_active = True

        if is_creator:
            user.is_creator = True

        user.save()
        breakingpoint(f"{user.pk}")
    else:
        # breakpoint('FORM NOT VALID')
        return render(request, "registration/signup.html", {'form': form,
                               'TEMPLATE_TITLE': 'signup',
                               'FORM_BUTTON_NAME': 'signup'})
    return user


def account_signup(request):
    """
        method to handle request for account signup
    """
    if request.method == 'POST':
        # breakpoint('POSTING')
        user = process_user_creation(request)

        # uid = force_text(urlsafe_base64_encode(force_bytes(user.pk)))
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = account_activation_token.make_token(user)

        # send email verification
        send_email_verification(request, user, uid, token)
        return render(request, 'registration/notification.html',
                                {
                                'TEMPLATE_TITLE': 'confirm email',
                                'notification': 'Please confirm your email address to complete your registration'
                                })
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html',
                  {'form': form,
                   'TEMPLATE_TITLE': 'signup',
                   'FORM_BUTTON_NAME': 'signup'})


def send_email_verification(request, user, uid, token):
    """
        method to process and send email verification
    """
    current_site = get_current_site(request)
    subject = 'Activate Your Recipe.FoodInc Account'
    message = render_to_string('registration/account_activation_email.html', {
        'user': user,
        'domain': current_site.domain,
        'url_path': CustomUser.get_absolute_url(uid, token),
    })

    SENDER_EMAIL = "info.mitchkoj@gmail.com"
    RECEIVER_EMAIL_LIST = [user.email]

    try:
        print(f"\n\n sending email \n\n")
        print(f"\n\n {user.email} \n\n")
        send_mail(subject, message, SENDER_EMAIL, RECEIVER_EMAIL_LIST)
    except Exception as e:
        breakingpoint(e)


@login_required
def reconfirm_email(request):
    """
    upon login, if user email not confirmed, render confirm_email.html.
    send another confirmation email.
    :param request:
    :return:
    """
    user = request.user
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = account_activation_token.make_token(user)

    # send email verification
    send_email_verification(request, user, uid, token)
    return render(request, 'registration/notification.html',
                            {
                            'TEMPLATE_TITLE': 'confirm email',
                            'notification': 'Please confirm your email address to complete your account setup'
                            })


def activate_user(request, uidb64, token):
    """
        method to verify and confirm user email
    """
    try:
        breakingpoint('Preparing uid, user, and token')
        breakingpoint(f'uidb64: {uidb64}')
        uid = force_text(urlsafe_base64_decode(uidb64))
        breakingpoint(f'uid: {uid}')
        user = CustomUser.objects.get(pk=uid)
        _values_ = f"uid: {uid} | user: {user} | token: {token}"
        breakingpoint(_values_)
    except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        # user.is_active = True
        user.email_confirmed = True
        user.save()

        login(request, user)

        return redirect('gate_keeper')
    else:
        return render(request, 'registration/notification.html',
                                {
                                'TEMPLATE_TITLE': 'invalid activation',
                                'notification': 'The confirmation link was invalid It may have expired or been used'
                                })


def get_false_key(dict_obj):
    """
    get the dictionary key with a "False" boolean value
    :param dict_obj:
    :return:
    """
    for key, value in dict_obj.items():
        if not value:
            return key
    return 1


def breakingpoint(message):
    print(f'\n-------------- BREAKPOINT MARK --------------\n')
    print(f'{message}')
    print(f'\n-------------- END BREAKPOINT MARK ----------------\n')
