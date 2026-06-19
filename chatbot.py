import re

from predict import predict_email
from url_predict import predict_url

from gemini_service import (
    generate_response
)


def is_url(text):

    pattern = r"(http[s]?://|www\.)"

    return bool(
        re.search(
            pattern,
            text
        )
    )


def chat(message):

    if is_url(message):

        result = predict_url(
            message
        )

        prompt = f"""
You are a cybersecurity assistant.

User URL:
{message}

Analysis:
{result}

Explain:
- Is it dangerous?
- Why?
- Give advice.

Answer only in English.
"""

        return {
            "mode": "url",
            "analysis": result,
            "chat_reply":
            generate_response(
                prompt
            )
        }

    else:

        result = predict_email(
            message
        )

        prompt = f"""
You are a cybersecurity assistant.

Email:
{message}

Model Result:
{result}

Explain:
- Spam or Safe
- Threat
- Advice

Answer only in English.
"""

        return {
            "mode": "email",
            "analysis": result,
            "chat_reply":
            generate_response(
                prompt
            )
        }