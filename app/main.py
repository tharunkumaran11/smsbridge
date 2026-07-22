from fastapi import FastAPI

from app.models import SMSRequest

from app.sms_service import send_sms

app = FastAPI(
    title="SMSBridge API",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "project":"SMSBridge"
    }

@app.get("/health")
def health():
    return {
        "status":"Running"
    }

@app.post("/send-sms")
def send_sms_api(request: SMSRequest):

    return send_sms(
        request.phone,
        request.message
    )