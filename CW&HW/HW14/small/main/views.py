from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, response
from django.template.loader import get_template
from django.core.mail import send_mail
from xhtml2pdf import pisa
from io import BytesIO
from django.template.loader import render_to_string
from .models import Product
from django.utils.html import strip_tags
from .forms import ProductForm


def add_product(request):
    if request.method=='POST':
            form = ProductForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')
    else:
        form = ProductForm()
    return render(request, 'create.html', {'form':form})


def product_read(request):
    product_list= Product.objects.all()
    return render(request,'read.html',{'product_list': product_list})


def generate_pdf(request,pk):
    product = get_object_or_404(Product, pk=pk)
    
    template = get_template('product_pdf.html')
    html = template.render({'product': product})
    
    buffer = BytesIO()
    pisa_status = pisa.CreatePDF(html, dest=buffer)
    
    if pisa_status.err:
        return HttpResponse('PDF creation error!')
    else:
        response = HttpResponse(buffer.getvalue(),content_type = 'application/pdf')
        response['Content-Disposition']= 'attachment; fileame="{}.pdf"'.format(product.name)
        return response
    
def send_product_email(request, pk):
    product = Product.objects.get(pk=pk)
    subject = f"Product information: {product.name}"
    from_email= "user123@gmail.com"
    recipient_list = ["your_mailtrap_inbox@mailtrap.io"]
    html_message = render_to_string('product_email.html',{'product':product})
    plain_message= strip_tags(html_message)
    send_mail(subject, plain_message, from_email, recipient_list, html_message=html_message)
    return HttpResponse('Email sent successfully')