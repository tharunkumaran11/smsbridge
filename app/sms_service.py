from datetime import datetime


def send_sms(phone: str, message: str):

    print("=" * 50)
    print("📩 New SMS Request")
    print(f"Time    : {datetime.now()}")
    print(f"Phone   : {phone}")
    print(f"Message : {message}")
    print("=" * 50)

    return {
        "status": "success",
        "phone": phone,
        "message": message,
        "timestamp": str(datetime.now())
    }