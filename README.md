# AgriAgent AI 🌾🚜

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.3-green?logo=flask&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple?logo=bootstrap&logoColor=white)
![OpenRouter API](https://img.shields.io/badge/OpenRouter-API-orange)
![SERP API](https://img.shields.io/badge/SERP-API-red)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 🌟 Overview

**AgriAgent AI** is an autonomous **multi-agent advisory system** for farmers.  
It provides **personalized insights** into government schemes, crop insurance, loans, and sustainability incentives based on the farmer's profile.  

With structured farm inputs and a **knowledge base of 100+ crops and schemes**, it delivers actionable recommendations through reports and an interactive **RAG-based chatbot**.  

---

## 🤖 Agents & Their Roles

- **Profiling Agent 📝** – Collects and processes farm and farmer details.  
- **Subsidy Agent 💰** – Identifies eligible government schemes and subsidies.  
- **Insurance Agent 🛡️** – Evaluates and recommends crop insurance options.  
- **Financial Agent 💳** – Suggests suitable loans and financial support programs.  
- **Sustainability Agent 🌱** – Recommends sustainable practices & carbon credit opportunities.  
- **Climate Agent 🌦️** – Assesses climate-related risks for specific crops and regions.  
- **Master Agent 🏆** – Aggregates all outputs and generates comprehensive advisory reports.  

---

## ⚡ Key Features

- **Farmer Profile Collection** – Captures farm size, location, crop type, soil type, irrigation method, and income category.  
- **Personalized Advisory Reports** – Generates **PDF reports** 📄 with tailored recommendations on subsidies, insurance, loans, and sustainability practices.  
- **RAG-Powered Chatbot** 🤖 – Provides instant answers to farmer queries using Retrieval-Augmented Generation.  
- **LLM Integration** – Leverages **OpenRouter API** 🔑 for intelligent reasoning and response generation.  
- **Real-time Policy Updates** – Uses **SERP API** 🌐 to fetch current government schemes and market information.  
- **Comprehensive Knowledge Base** 📚 – Contains data on 100+ crops, subsidy schemes, insurance policies, and agricultural best practices.  
- **User-Friendly Interface** – Built with **HTML, CSS, and Bootstrap** 🖥️ for an intuitive web experience.  
- **Cloud-Ready Architecture** ☁️ – Environment variable-based configuration for secure API key management.  

---

## 🛠️ Technology Stack

| Component | Technology |
|-----------|------------|
| **Backend** | Flask (Python) 🐍 |
| **Frontend** | HTML, CSS, Bootstrap 5 🖌️ |
| **Multi-Agent System** | Python-based autonomous agents 🤖 |
| **LLM & RAG** | OpenRouter API (for LLM) + SERP API (for real-time data) 🌐 |
| **Knowledge Base** | Structured text files with crop & subsidy data 📚 |
| **Report Generation** | Custom PDF generation service 📝 |
| **Deployment** | Cloud-ready with environment variable configuration ☁️ |

---

## 🚀 Installation & Setup

### Prerequisites
- Python 3.10 or higher
- OpenRouter API key
- SERP API key

### Step-by-Step Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/AgriAgentAI.git
   cd AgriAgentAI
Create a virtual environment

bash
python -m venv venv
Activate the virtual environment

Windows:

bash
venv\Scripts\activate
macOS/Linux:

bash
source venv/bin/activate
Install dependencies

bash
pip install -r requirements.txt
Set up environment variables

Windows (Command Prompt):

bash
set OPENROUTER_API_KEY=your_openrouter_api_key
set SERP_API_KEY=your_serp_api_key
Windows (PowerShell):

bash
$env:OPENROUTER_API_KEY="your_openrouter_api_key"
$env:SERP_API_KEY="your_serp_api_key"
macOS/Linux:

bash
export OPENROUTER_API_KEY="your_openrouter_api_key"
export SERP_API_KEY="your_serp_api_key"
Run the application

bash
python app.py
Access the web interface

Open your browser and visit: http://localhost:5000 🌐

📋 How It Works
Farmer Registration – Farmer enters details (land size, location, crops, soil type, etc.)

Profile Analysis – Profiling Agent processes the information

Multi-Agent Processing – Specialized agents analyze different aspects:

Subsidy Agent checks eligible government schemes

Insurance Agent evaluates crop insurance options

Financial Agent identifies loan opportunities

Sustainability Agent recommends eco-friendly practices

Climate Agent assesses weather-related risks

Report Generation – Master Agent compiles all insights into a comprehensive PDF report

Interactive Q&A – Farmers can ask follow-up questions to the RAG-powered chatbot

🗂️ Sample Output
Advisory Report Contents
After submitting your profile, AgriAgent AI generates a comprehensive advisory report (available as PDF) that includes:

Section	Description
📝 Farmer Summary	Personalized overview of your farm profile
💰 Eligible Subsidies	Detailed list of government schemes you can apply for, with eligibility criteria and application process
🛡️ Insurance Recommendations	Crop insurance options tailored to your location and crop type, with premium estimates
💳 Financial Assistance	Suitable loan schemes, interest rates, and financial support programs
🌱 Sustainability Plan	Actionable steps for sustainable farming and potential carbon credit earnings
🌦️ Climate Risk Assessment	Analysis of climate-related risks and mitigation strategies
Chatbot Interaction Examples
"How do I apply for the PMFBY scheme in my state?"

"What are the best drought-resistant crops for my region?"

"Tell me more about the Kisan Credit Card loan benefits."

"What sustainable practices can help me earn carbon credits?"

📁 Project Struct
