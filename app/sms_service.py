import logging
import requests

from app.config import GATEWAY_URL, GATEWAY_TOKEN, TIMEOUT
from app.database import save_sms


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


def send_sms(phone, message):

    payload = {
        "to": phone,
        "message": message
    }

    headers = {
        "Authorization": GATEWAY_TOKEN
    }

    logger.info(f"Sending SMS to {phone}")

    try:

        response = requests.post(
            GATEWAY_URL,
            json=payload,
            headers=headers,
            timeout=TIMEOUT
        )

        if response.status_code == 200:

            logger.info("SMS sent successfully")

            save_sms(
                phone,
                message,
                "SUCCESS"
            )

            return {
                "status": "success",
                "message": "SMS sent successfully.",
                "phone": phone
            }

        logger.warning(f"Gateway returned {response.status_code}")

        save_sms(
            phone,
            message,
            "FAILED"
        )

        return {
            "status": "failed",
            "gateway_status": response.status_code,
            "gateway_response": response.text
        }

    except Exception as e:

        logger.error(str(e))

        save_sms(
            phone,
            message,
            "ERROR"
        )

        return {
            "status": "error",
            "message": str(e)
        }