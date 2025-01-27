from flask import request, jsonify
from flask_smorest import Blueprint, abort
from app.services.auth_service import AuthService
from app.repositories.user_repository import UserRepository
from app.exceptions.google_api_exc import GoogleAPIError

blueprint = Blueprint("Auth", __name__, url_prefix='/auth')

auth_service = AuthService()
user_repository = UserRepository()

@blueprint.route("/login", methods=['POST'])
def login():
    token = request.json.get('token')
    if not token:
        return jsonify({'error': 'Token is required'}), 400

    try:
        user = auth_service.get_user_and_check_if_its_registered(token)

        user_info = {"id": user.id, "google_resource_name": user.google_resource_name, "display_name": user.display_name}
        return jsonify({'message': 'Login successful', 'data': user_info})
    except GoogleAPIError as e:
        abort(401, message=str(e))
    except Exception as e:
        print(str(e))
        abort(500, message='Unexpected error happened')

@blueprint.route("/contacts/<string:resource_name>", methods=['GET'])
def get_contacts(resource_name=None):
    if not resource_name:
        return jsonify({'error': 'Resource Name is required'}), 400

    user = user_repository.get_user_by_google_resource_name(f'people/{resource_name}')
    print(user)
    if not user:
        return jsonify({'error': 'Invalid resource name'}), 400
    try:
        contacts = auth_service.get_user_contacts_organized_by_domain(f'people/{resource_name}')
        return jsonify({"data": contacts})
    except GoogleAPIError as e:
        abort(401, message=str(e))
    except Exception as e:
        print(str(e))
        abort(500, message='Unexpected error happened')
