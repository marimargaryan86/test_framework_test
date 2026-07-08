import json
import requests
import allure
from src.config import Config


class BaseClient:
    """The Parent Class containing shared setup, HTTP shortcuts, and auto-logging."""

    def __init__(self):
        self.base_url = Config.BASE_URL
        self.headers = {"Content-Type": "application/json"}

    def _log_to_allure(self, response: requests.Response):
        """Formats and attaches the HTTP request and response details to the Allure report."""
        try:
            # Format request body neatly if it's JSON
            req_body = response.request.body
            if req_body and isinstance(req_body, bytes):
                req_body = req_body.decode('utf-8')
                try:
                    req_body = json.dumps(json.loads(req_body), indent=2)
                except ValueError:
                    pass  # Keep as plain text if it's not valid JSON

            # Format response body neatly if it's JSON
            try:
                res_body = json.dumps(response.json(), indent=2)
            except ValueError:
                res_body = response.text

            # Create a structured text representation of the API call
            log_content = (
                f"=== HTTP REQUEST ===\n"
                f"URL: {response.request.method} {response.url}\n"
                f"Headers: {json.dumps(dict(response.request.headers), indent=2)}\n"
                f"Body:\n{req_body or 'None'}\n\n"
                f"=== HTTP RESPONSE ===\n"
                f"Status Code: {response.status_code}\n"
                f"Body:\n{res_body}\n"
            )

            # This line attaches the log string as a text file attachment inside the current Allure test step
            allure.attach(
                log_content,
                name=f"API Exchange: {response.request.method} {response.request.path_url}",
                attachment_type=allure.attachment_type.TEXT
            )
        except Exception as e:
            # Prevent logging failures from crashing the actual tests
            allure.attach(f"Failed to log API exchange: {str(e)}", name="Logging Error",
                          attachment_type=allure.attachment_type.TEXT)

    def _get(self, endpoint: str):
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url, headers=self.headers)
        self._log_to_allure(response)  # 🆕 Intercept and log automatically
        return response

    def _post(self, endpoint: str, payload: dict):
        url = f"{self.base_url}{endpoint}"
        response = requests.post(url, json=payload, headers=self.headers)
        self._log_to_allure(response)  # 🆕 Intercept and log automatically
        return response