# Gen AI Project

## Description
This project is built using Python's FastAPI framework. It includes endpoints for language translation and a PDF-based retrieval-augmented generation (RAG) model for a chatbot.

## Setup Instructions

### Prerequisites
- Ensure you have Python v3.13 installed on your system.

### Steps

1. **Install Python v3.13**

   Download and install Python v3.13 from the official [Python website](https://www.python.org/downloads/).

2. **Create a Virtual Environment**

   Open your terminal and navigate to the project directory. Run the following command to create a virtual environment:

   ```python3 -m venv venv```

### Activate the Virtual Environment
#### On Windows:
```.\venv\Scripts\activate```

#### On macOS and Linux:
```source venv/bin/activate```

### Install Required Packages With the virtual environment activated, install the necessary packages using the requirements.txt file:
```pip install -r requirements.txt```

### Run the Application Start the FastAPI application using Uvicorn:
```uvicorn app.main:app --reload```

This will start the server, and you can access the API documentation at http://127.0.0.1:8000/docs.

### Additional Information
Ensure that all environment variables and configurations are set up as required by the project.
For any issues or contributions, please refer to the project's issue tracker or contact the maintainers.
