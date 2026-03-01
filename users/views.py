from django.core.mail import send_mail
from django.http import HttpResponse

def send_test_email(request):
    send_mail(
        'Test Email from StepHero',
        'This is a test email sent from your StepHero project.',
        'carl.claw.me@gmail.com',
        ['armin.letz@gmail.com'],
        fail_silently=False,
    )
    return HttpResponse('Test email sent!')