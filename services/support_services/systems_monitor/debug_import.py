
import sys
import os

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

print(f"CWD: {os.getcwd()}")
print(f"sys.path: {sys.path}")

try:
    import app
    print(f"Imported app from: {app.__file__}")
    import app.telemetry
    print(f"Imported app.telemetry from: {app.telemetry.__file__}")
    print(f"Attributes in app.telemetry: {dir(app.telemetry)}")
    
    if 'initialize_telemetry' in dir(app.telemetry):
        print("initialize_telemetry is present.")
    else:
        print("initialize_telemetry is MISSING.")
        
except ImportError as e:
    print(f"ImportError: {e}")
except Exception as e:
    print(f"Error: {e}")
