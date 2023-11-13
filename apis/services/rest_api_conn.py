# import lib for rest api
import json
import requests


def _get_data(api_url, access_token, last_timestamp):
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    response = requests.get(api_url, headers=headers)
    if response.status_code == 401:
        # Refresh the token if it has expired
        access_token = refresh_token()
        headers["Authorization"] = f"Bearer {access_token}"
        response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        raise Exception(
            f"Failed to get data from API. Response: {response.text}")


def refresh_token():
    refresh_token =  # retrieve refresh token from storage
    data = {
        "refresh_token": refresh_token,
        "grant_type": "refresh_token"
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    response = requests.post(
        "https://auth.example.com/refresh", data=data, headers=headers)
    if response.status_code == 200:
        # Save the new access token and refresh token
        response_json = json.loads(response.text)
        access_token = response_json["access_token"]
        refresh_token = response_json["refresh_token"]
        # save the new access token and refresh token to storage
        return access_token
    else:
        raise Exception(f"Failed to refresh token. Response: {response.text}")
