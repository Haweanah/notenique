# notenique/run.py
from dotenv import load_dotenv
import os
from notenique import create_app

# Load environment variables from .env file (for development)
load_dotenv()

# Create the Flask application instance
app = create_app()



# Run the application (for development, use the Flask built-in server)
if __name__ == '__main__':
    app.run(debug=False)  # Set debug=False in production
