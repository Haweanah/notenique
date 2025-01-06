from dotenv import load_dotenv
import os
from notenique import create_app

# Load environment variables from .env file
load_dotenv()

# Create the Flask application instance
app = create_app()

# Run the application
if __name__ == '__main__':
    # Debug mode is controlled by the DEBUG environment variable
    debug_mode = os.getenv('DEBUG', 'False').lower() in ['true', '1', 't', 'yes']
    app.run(debug=debug_mode)
