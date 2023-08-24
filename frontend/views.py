from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from django.contrib import messages
from django.shortcuts import redirect
from .models import Testimonial
from django.http import JsonResponse
import openai
# Create your views here.

def index(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'frontend/index/index.html', {'testimonials': testimonials})
                            # template_name              # context

def about(request):
    return render(request, 'frontend/about/about.html')

# < -- Start Services Views -- >
def services(request):
    return render(request, 'frontend/services/services.html')

def hair_transplant(request):
    return render(request, 'frontend/services/hair_transplant/hair_transplant.html')

def dental(request):
    return render(request, 'frontend/services/dental/dental.html')

def cosmetic(request):
    return render(request, 'frontend/services/cosmetic/cosmetic.html')

def plastic(request):
    return render(request, 'frontend/services/plastic/plastic.html')

def eye_surgery(request):
    return render(request, 'frontend/services/eye_surgery/eye_surgery.html')

def art(request):
    return render(request, 'frontend/services/art/art.html')


# < -- End Services Views -- >
def gallery(request):
    return render(request, 'frontend/gallery/gallery.html')

def gallery_hair_transplant(request):
    return render(request, 'frontend/gallery/gallery_hair_transplant.html')

def gallery_dental(request):
    return render(request, 'frontend/gallery/gallery_dental.html')

def gallery_eye_surgery(request):
    return render(request, 'frontend/gallery/gallery_eye_surgery.html')

def gallery_ivf(request):
    return render(request, 'frontend/gallery/gallery_ivf.html')

def gallery_plastic(request):
    return render(request, 'frontend/gallery/gallery_plastic.html')

def gallery(request):
    return render(request, 'frontend/gallery/gallery.html')

def gallery_cosmetic(request):
    return render(request, 'frontend/gallery/gallery_cosmetic.html')

def faq(request):
    return

def terms_and_conditions(request):
    return render(request, 'frontend/terms_and_conditions/terms_and_conditions.html')

def privacy(request):
    return render(request, 'frontend/privacy/privacy.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                form.save()

                # Send email
                subject = form.cleaned_data['subject']
                message = 'A new contact form has been submitted.\n\n' \
                          f'First Name: {form.cleaned_data["first_name"]}\n' \
                          f'Last Name: {form.cleaned_data["last_name"]}\n' \
                          f'Email: {form.cleaned_data["email"]}\n' \
                          f'Phone Number: {form.cleaned_data["phone_number"]}\n' \
                          f'Subject: {form.cleaned_data["subject"]}\n' \
                          f'Message: {form.cleaned_data["message"]}'

                recipient_list = [settings.DEFAULT_FROM_EMAIL]
                send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)

                messages.success(request, 'Message sent successfully!')
                return redirect('index')  # Assuming the URL name for the homepage is 'index'
            except Exception as e:
                print(f"Error saving form data: {e}")
                messages.error(request, 'An error occurred while saving the form data.')
    else:
        form = ContactForm()

    # Print form errors to the console
    if form.errors:
        print(form.errors)

    return render(request, 'frontend/contact/contact.html', {'form': form})

# openai.api_key = settings.OPENAI_API_KEY

# def chatbot(message):
#     prompt = f"User: {message}\nChatbot:"
        
#     if "timing" in message:
#         prompt += "\nOur clinic is open from 9 AM to 5 PM, Monday to Friday."
#     elif "address" in message:
#         prompt += "\nOur clinic is located at 123 Main Street, City, Country."
#     elif "appointment" in message:
#         prompt += "\nTo book an appointment, you can call our clinic at 123-456-7890."
#     else:
#         prompt += "\nI'm sorry, I'm not sure how to help with that question."
    
#     response = openai.Completion.create(
#             engine="text-davinci-003",
#             prompt=prompt,
#             max_tokens=50
#     )

#     answer = response.choice[0].text.strip()
#     return answer

# def chatbot(request):
#     if request.method == 'POST':
#         message = request.POST.get('message')
#         response = ask_openai(message)
#         return JsonResponse({'message':message,'response':response})

#     return render(request, 'frontend/chatbot/chatbot.html')