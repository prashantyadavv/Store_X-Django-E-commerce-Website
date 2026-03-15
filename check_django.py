import os
import django
import sys

# Add the project directory to sys.path
sys.path.append(os.getcwd())

try:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecommerce.settings")
    django.setup()
    print("DJANGO_STATUS: OK")
except Exception as e:
    print(f"DJANGO_STATUS: ERROR")
    print(f"ERROR_MSG: {str(e)}")
    import traceback
    traceback.print_exc()
