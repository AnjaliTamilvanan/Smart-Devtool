# Smart DevTool

Smart DevTool is an AI-powered tool that simplifies API integration by automatically extracting API details from documentation and generating ready-to-use code.

---

## Problem Statement

Developers spend a lot of time reading API documentation, identifying endpoints, handling authentication, and writing repetitive code. This slows down development and creates unnecessary complexity.

---

## Solution

Smart DevTool automates this process by:
- Extracting API details from documentation  
- Identifying endpoints and parameters  
- Detecting authentication requirements  
- Generating ready-to-use API code instantly  

---

## Features

- Extract API endpoints from documentation  
- AI-based parsing of API structure  
- Generate sample API URLs  
- Auto-generate working Python code  
- Detect authentication requirements  
- Provide SDK suggestions  
- Copy-to-clipboard support  
- Clean and interactive UI  

---

## Tech Stack

**Frontend**
- React.js  
- CSS  

**Backend**
- FastAPI (Python)  
- OpenAI API  

**Libraries**
- requests  
- python-dotenv  

---

## How It Works

1. User enters API documentation URL and use case  
2. Backend scrapes API content  
3. AI extracts structured data  
4. System selects the best endpoint  
5. Generates API URL and code  
6. Displays results in UI  

---

## Setup Instructions

### 1. Clone Repository
```bash
git clone https://github.com/AnjaliTamilvanan/Smart-Devtool.git
cd Smart-Devtool

2. Backend Setup
cd api-devtool/backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

Create .env file:

OPENAI_API_KEY=your_api_key_here

Run backend:

uvicorn main:app --reload

3. Frontend Setup
cd ../frontend
npm install
npm run dev
4. Access Application
http://localhost:5173


Usage
Enter API documentation URL
Provide a use case
Click "Analyze API"
View:
API details
Endpoints
Sample URL
Generated code
Copy and use the code


Prerequisites
Python 3.8+
Node.js
OpenAI API Key


Conclusion

Smart DevTool reduces the effort required to understand API documentation and generate integration code. It helps developers save time and focus on building applications instead of manually reading documentation.