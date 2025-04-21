import requests
import os


def get_user_events(user_name: str):
    """Fetches events for a given user from the GitHub API."""
    url = f"https://api.github.com/users/{user_name}/events"
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        raise EnvironmentError("GITHUB_TOKEN is not set")
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"Bearer {token}",
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        latest_events = response.json()
        if latest_events:
            for event in latest_events:
                print(event["type"])
                print(event["repo"]["name"])
                print(event["payload"])
                print("=" * 20)
            return latest_events

        else:
            return None
    else:
        raise Exception(
            f"Error fetching events: {response.status_code} - {response.text}"
        )
