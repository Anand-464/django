from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm
from .models import Product
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.template.loader import get_template, render_to_string
from xhtml2pdf import pisa
from io import BytesIO
from django.utils.html import strip_tags
from django.core.mail import send_mail



def product_create(request):
    if request.method=='POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductForm()
    return render(request, 'create.html', {'form':form})

def product_read(request):
    product_list=Product.objects.all()
    return render(request,'retrieve.html',{'product_list':product_list})

def product_update(request, id):
    product = Product.objects.get(pk=id)
    if request.method == 'POST':
        form = ProductForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form =ProductForm(instance=product)           
    return render(request, 'update.html', {'form': form})

def product_delete(request,pk):
    product=Product.objects.get(pk=pk)  
    if request.method == 'POST':
        product.delete()
        return redirect('home')
    
    return render(request,'delete.html',{'product':product})

def listing(request):
    product_list = Product.objects.all()
    paginator = Paginator(product_list, 3)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'list.html', {'page_obj': page_obj})

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
    subject = f"New product: {product.name}"
    from_email= "user123@gmail.com"
    recipient_list = ["your_mailtrap_inbox@mailtrap.io"]
    html_message = render_to_string('product_email.html',{'product':product})
    plain_message= strip_tags(html_message)
    send_mail(subject, plain_message, from_email, recipient_list, html_message=html_message)
    return HttpResponse('Email sent successfully')