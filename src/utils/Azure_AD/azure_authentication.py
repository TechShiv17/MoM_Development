import os
from msal import ConfidentialClientApplication

def acquire_token():
    # Load environment variables or use a configuration file
    client_id = os.getenv("AZURE_CLIENT_ID")
    # Please uncomment the next line, that is commented to avoid repositories rule violation.
    client_secret = os.getenv("AZURE_CLIENT_SECRET_VALUE")
    authority = "https://login.microsoftonline.com/tenant-id"

    # Create a ConfidentialClientApplication
    app = ConfidentialClientApplication(
        client_id,
        authority=authority,
        client_credential=client_secret
    )

    # Get access token
    result = app.acquire_token_silent(scopes=["https://graph.microsoft.com/.default"], account=None)
    if not result:
        result = app.acquire_token_for_client(scopes=["https://graph.microsoft.com/.default"])

    return result.get("access_token")
