from django.shortcuts import render, redirect
from .forms import QuotationForm
from django.contrib import messages
from .models import ContactInfo, Quotation

def home(request):
    contact_info = ContactInfo.objects.first()
    
    if request.method == 'POST':
        print('1.Done')
        form = QuotationForm(request.POST)
        
        if form.is_valid():
            # Access cleaned form data
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            mobile = form.cleaned_data['mobile']
            address = form.cleaned_data['address']
            home_appliance = form.cleaned_data['home_appliance']
            home_appliance_maker = form.cleaned_data['home_appliance_maker']
            home_appliance_model_number = form.cleaned_data['home_appliance_model_number']
            home_appliance_problem = form.cleaned_data['home_appliance_problem']
            
            # Create and save Quotation instance
            quotation = Quotation(
                first_name=first_name,
                last_name=last_name,
                email=email,
                mobile=mobile,
                address=address,
                home_appliance=home_appliance,
                home_appliance_maker=home_appliance_maker,
                home_appliance_model_number=home_appliance_model_number,
                home_appliance_problem=home_appliance_problem
            )
            quotation.save()
            
            messages.success(request, 'Form submitted successfully.')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the errors.')
    else:
        form = QuotationForm()
    
    return render(request, 'base.html', {'form': form, 'contact_info': contact_info})
