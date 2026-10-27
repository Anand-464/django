from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, response
from django.template.loader import get_template
from django.core.mail import send_mail
from xhtml2pdf import pisa
from io import BytesIO
from django.template.loader import render_to_string
from .models import Certificate
from django.utils.html import strip_tags


def certificate_form(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        course_name = request.POST.get('course_name', '').strip()
        date = request.POST.get('date', '').strip()

        certificate = Certificate.objects.create(
            student_name=name,
            student_email=email,
            course_name=course_name,
            completion_date=date
        )
        
        
        template = get_template('certificate_pdf.html')
        html = template.render({'certificate': certificate})
        buffer = BytesIO()
        pisa_status = pisa.CreatePDF(html, dest=buffer)
        
        if pisa_status.err:
            return HttpResponse('PDF creation error!')
        else:
            response = HttpResponse(buffer.getvalue(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="{}.pdf"'.format(certificate.student_name)

        
        subject = f"Course Completion Certificate for {certificate.student_name}"
        from_email = "user123@gmail.com"
        recipient_list = ["your_mailtrap_inbox@mailtrap.io"]
        html_message = render_to_string('certificate_email.html', {'certificate': certificate})
        plain_message = strip_tags(html_message)
        send_mail(subject, plain_message, from_email, recipient_list,html_message=html_message)
        return response

    return render(request, 'form.html')


  
    
    
    
