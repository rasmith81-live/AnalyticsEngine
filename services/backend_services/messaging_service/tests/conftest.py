import sys
import os

# Add the service root directory to sys.path
# This assumes the structure is:
# services/
#   backend_services/
#     messaging_service/
#       app/
#       tests/
#
# We want to add 'services/backend_services/messaging_service' to sys.path
# so that 'import app' works.

current_dir = os.path.dirname(os.path.abspath(__file__))
service_root = os.path.abspath(os.path.join(current_dir, ".."))

if service_root not in sys.path:
    sys.path.insert(0, service_root)
