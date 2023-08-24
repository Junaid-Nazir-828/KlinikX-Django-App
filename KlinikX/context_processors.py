from datetime import date


def contact_info_context(request):
    current_year = date.today().year
    return {
        # Counter
        'doctor_counter': '32',
        'staff_counter': '121',
        'customer_counter': '6547',
        # footer year
        'year': current_year,
        # Business Details
        'address': 'Esenyurt, İstanbul, Türkiye', 
        'phone_number': '+64210403089', 
        'email': 'info@klinikx.com',  
        'website': 'http://www.klinikx.com',  
        # Social Media Links
        'twitter': 'https://twitter.com/klinikxofficial',
        'facebook': 'https://www.facebook.com/klinikxofficial', 
        'youtube': 'https://www.youtube.com/@KlinikXOfficial',
        'instagram': 'https://www.instagram.com/klinikxofficial/',
        'snapchat': 'https://snapchat.com/add/klinikxofficial',

        
    }

