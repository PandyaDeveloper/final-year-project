from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def sendmail(subject,template,to,context):
    n = subject
    t = to
    template_str = 'blog/'+ template+'.html'
    html_message = render_to_string(template_str, {'data': context})
    plain_message =strip_tags(html_message)
    from_email = 'darshitpandya18@gmail.com'
    send_mail(n, plain_message, from_email, [t], html_message=html_message)