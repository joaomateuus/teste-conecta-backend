import requests
from app.exceptions.google_api_exc import GoogleAPIError

class GoogleAPIClient:
    BASE_URL = 'https://people.googleapis.com/v1/people/me'

    def get_user_google_account(self, token: str):
        response = requests.get(
            f'{self.BASE_URL}?personFields=names,emailAddresses',
            headers={"Authorization": f'Bearer {token}'}
        )
        
        if not response.ok:
            raise GoogleAPIError.from_api_response(response)
        
        return response.json()

    def get_user_google_contacts(self, token: str):
        response = requests.get(
            f'{self.BASE_URL}/connections?personFields=names,emailAddresses',
            headers={"Authorization": f'Bearer {token}'}
        )
        
        if not response.ok:
            raise GoogleAPIError.from_api_response(response)
        
        return response.json()