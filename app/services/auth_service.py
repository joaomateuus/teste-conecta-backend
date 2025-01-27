
from app.clients.google_api_client import GoogleAPIClient
from app.repositories.user_repository import UserRepository
from app.model import models
from app import utils

class AuthService:
    def __init__(self):
        self.google_api_client = GoogleAPIClient()
        self.user_repository = UserRepository()
    
    def get_user_and_check_if_its_registered(self, token: str):
        google_user = self.google_api_client.get_user_google_account(token)
        print(google_user)
        user = self.user_repository.get_user_by_google_resource_name(google_user['resourceName'])
        if not user:
            user = models.User(
                google_resource_name=google_user['resourceName'],
                name=google_user['names'][0]['givenName'],
                display_name=google_user['names'][0]['displayName'],
                token=token
            )
            self.user_repository.save_user(user)
        
        self.user_repository.update_user_token(user, token)
        return user
    
    def get_user_contacts_organized_by_domain(self, resource_name: str):
        user = self.user_repository.get_user_by_google_resource_name(resource_name)
        
        contacts = self.google_api_client.get_user_google_contacts(user.token)
        
        return utils.organize_contacts_by_domain(contacts)

