from azure.identity import DefaultAzureCredential
from azure.graphrbac import GraphRbacManagementClient

from azure_authentication import acquire_token
from Requests_to_Microsoft_Graph_API import fetch_meetings

def authenticate_with_azure():
    # Use DefaultAzureCredential for authentication
    credential = DefaultAzureCredential()

    try:
        # Create a GraphRbacManagementClient
        graph_client = GraphRbacManagementClient(credential, "f8cdef31-a31e-4b4a-93e4-5f571e91255a")

        # Register your application
        app_registration = graph_client.applications.create(
            {
                "displayName": "Email_Extraction",
                "signInAudience": "AzureADandPersonalMicrosoftAccount",
                "requiredResourceAccess": [
                    {
                        "resourceAppId": "00000003-0000-0000-c000-000000000000",  # Microsoft Graph API
                        "resourceAccess": [
                            {
                                "id": "e1fe6dd8-ba31-4d61-89e7-88639da4683d",  # User.Read permission
                                "type": "Scope"
                            }
                        ]
                    }
                ],
                "web": {
                    "redirectUris": ["http://localhost/callback"]  # Redirect URI
                }
            }
        )
    except Exception as e:
        print(f"Error while authenticating with Azure: {e}")

def main():
    try:
        authenticate_with_azure()
        # Acquire an access token for authentication
        access_token = acquire_token()  # Assuming this function exists and returns the access token
        # Make requests to fetch details of attendees
        attendee_details = fetch_meetings()

        # Process attendee details (e.g., print them)
        for attendee in attendee_details:
            print("Attendee:", attendee)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
