from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from customer.models import User
from customer.views.tokens import account_activation_token

