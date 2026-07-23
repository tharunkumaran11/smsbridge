from fastapi import Depends, FastAPI

from app.models import SMSRequest
from app.sms_service import send_sms
from app.database import create_tables, get_sms_history
from app.security import verify_api_key
from prometheus_fastapi_instrumentator import Instrumentator

create_tables()

app = FastAPI(
    title="SMSBridge API",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "project": "SMSBridge Version 2"
    }

@app.get("/health")
def health():
    return {
        "status": "Running"
    }

@app.post("/send-sms")
def send_sms_api(
    request: SMSRequest,
    api_key: str = Depends(verify_api_key)
):
    return send_sms(
        request.phone,
        request.message
    )

@app.get("/sms-history")
def sms_history(
    api_key: str = Depends(verify_api_key)
):
    return get_sms_history()

Instrumentator().instrument(app).expose(app)