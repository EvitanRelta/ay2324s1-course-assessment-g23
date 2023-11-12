import os
from dotenv import load_dotenv
import uvicorn

if __name__ == "__main__":
    # Load environment variables from .env file
    base_dir = os.path.dirname(os.path.abspath(__file__))
    load_dotenv(os.path.join(base_dir, '../../../../backend.conf'))
    load_dotenv(os.path.join(base_dir, '../../../../.env'))

    # Start Uvicorn server
    uvicorn.run("main:app", host="0.0.0.0", port=8001)
