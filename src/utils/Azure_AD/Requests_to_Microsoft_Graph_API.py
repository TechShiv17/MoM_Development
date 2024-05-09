import logging
import requests
from azure.identity import DefaultAzureCredential

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def fetch_meetings():
    # Authenticate with Azure using your credentials
    credential = DefaultAzureCredential()

    # Acquire an access token for authentication
    access_token = credential.get_token("https://graph.microsoft.com/.default").token

    if access_token:
        # API endpoint for fetching all meetings
        url = "https://graph.microsoft.com/v1.0/users/kumaririshika1020@outlook.com/events"
        # Request headers
        headers = {
            "Authorization": f"Bearer {access_token}",
        }

        # Make GET request
        response = requests.get(url, headers=headers)

        # Handle response
        if response.ok:  # Check if the response status code indicates success (200-299)
            meetings = response.json().get("value", [])
            for meeting in meetings:
                meeting_id = meeting.get("id")
                subject = meeting.get("subject")
                # email = meeting.get("email")
                start_time = meeting.get("start", {}).get("dateTime")
                end_time = meeting.get("end", {}).get("dateTime")
                print("Meeting ID:", meeting_id)
                print("Subject:", subject)
                print("Start Time:", start_time)
                print("End Time:", end_time)
                # print("Email :",email)
        else:
            if response.status_code == 401:
                logger.error("Unauthorized: Access token is expired or invalid.")
            else:
                logger.error("Error: %s - %s", response.status_code, response.text)
    else:
        logger.error("Access token not acquired. Unable to fetch meetings.")

# Call the function to fetch meetings
fetch_meetings()