from app.model import models
from app.infra.db import db

class UserRepository:
    def get_user_by_google_resource_name(self, resource_name: str):
        return models.User.query.filter(models.User.google_resource_name == f'people/{resource_name}').one_or_none()

    def save_user(self, user: models.User):
        db.session.add(user)
        db.session.commit()

    def update_user_token(self, user: models.User, token: str):
        user.token = token
        db.session.commit()