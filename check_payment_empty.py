import os
import django
from django.test import RequestFactory
from django.contrib.sessions.middleware import SessionMiddleware

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecommerce.settings")
django.setup()

from store.views import payment

try:
    factory = RequestFactory()
    request = factory.get('/payment/')
    
    middleware = SessionMiddleware(lambda r: None)
    middleware.process_request(request)
    request.session.save()
    
    request.session['cart'] = {}
    
    response = payment(request)
    print("Response Status Code:", response.status_code)

except Exception as e:
    import traceback
    traceback.print_exc()
