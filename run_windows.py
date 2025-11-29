#!/usr/bin/env python
"""Windows-compatible SearXNG launcher"""
import os
import sys

# Add searxng directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Set environment variables for development
os.environ['SEARXNG_DEBUG'] = '1'
os.environ['SEARXNG_PORT'] = '8888'
os.environ['SEARXNG_BIND_ADDRESS'] = '127.0.0.1'

# Mock the pwd module which is Unix-only
class PwdMock:
    def getpwuid(self, uid):
        class PwEntry:
            pw_name = 'windows_user'
        return PwEntry()

sys.modules['pwd'] = PwdMock()

print("="*60)
print("Starting SearXNG for Windows...")
print("="*60)

# Now import and run the Flask app
try:
    from searx import webapp
    
    print(f"SearXNG will be available at: http://127.0.0.1:8888")
    print("Press Ctrl+C to stop")
    print("="*60)
    
    # Run the Flask development server
    webapp.app.run(
        host='127.0.0.1',
        port=8888,
        debug=True,
        use_reloader=False  # Disable reloader on Windows to avoid issues
    )
    
except KeyboardInterrupt:
    print("\n\nShutting down SearXNG...")
    sys.exit(0)
except Exception as e:
    print(f"Error starting SearXNG: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
