import os
import django
from django.template.loader import render_to_string

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecommerce.settings")
django.setup()

try:
    html = render_to_string("store/review_order.html", {})
    print("Review Order Template rendered successfully.")
except Exception as e:
    import traceback
    traceback.print_exc()
