# AI Real Estate Lead Qualification Agent

This project implements **Task A (Mandatory)** of the Full Stack Developer Assignment.

## Overview
An AI-powered voice/chat assistant built using **Vapi** to qualify real estate leads
based on predefined business rules.

## Flow
1. Lead is contacted via voice/chat
2. Property requirements are collected
3. Property availability is checked
4. Lead is marked **Qualified** or **Not Qualified**
5. Final structured JSON is sent to backend via webhook

## Tech Stack
- Vapi (Voice AI)
- Python
- FastAPI
- JSON-based persistence

## Backend
The FastAPI backend exposes a webhook endpoint to receive structured output
from Vapi and store it for further processing.

## How to Run Backend
```bash
pip install fastapi uvicorn
uvicorn webhook:app --reload
```


## Curl request to add data: 
```
curl --location 'http://127.0.0.1:8000/vapi-webhook' \
--header 'Content-Type: application/json' \
--data '{
    "analysis": {
        "output": {
            "contact_name": "Shruti",
            "location": "Noida",
            "property_type": "Residential",
            "topology_or_subtype": "2BHK",
            "budget": "80 Lakhs",
            "sales_consent": "Yes",
            "property_count": 12,
            "decision": "Qualified",
            "reason": "Properties available and consent given"
        }
    }
}'