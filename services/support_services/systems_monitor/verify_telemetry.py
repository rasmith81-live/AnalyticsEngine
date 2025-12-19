
import sys
import os

# Add the directory containing 'app' to sys.path
sys.path.append(os.path.join(os.getcwd(), 'services', 'support_services', 'systems_monitor'))

try:
    from app import telemetry
    print("Successfully imported app.telemetry")
    print(f"initialize_telemetry: {getattr(telemetry, 'initialize_telemetry', 'Not Found')}")
except ImportError as e:
    print(f"ImportError: {e}")
except Exception as e:
    print(f"Error: {e}")
