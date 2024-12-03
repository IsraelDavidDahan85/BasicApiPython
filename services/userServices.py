from models.userModel import UserModel, user_schema, users_schema
from logger.log import log

class UserServices:

    @staticmethod
    def login_user(data):
        log.debug('login_user', data=data['email'])
        user_model = UserModel().get_user_by_email(data['email'])
        if user_model and user_model.get_decrypted_password() == data['password']:
            user_model.generate_token()
            log.info('User logged in', user=user_model.email)
            return user_schema.dump(user_model), user_model.token
        log.error('User not found', user=data['email'])
        return None, None

    @staticmethod
    def logout_user(data):
        # get token from header Authorization
        log.debug('logout_user')
        token = data.headers["Authorization"].split(" ")[1]
        user_model = UserModel().get_user_by_token(token)
        if user_model:
            user_model.delete_token()
            log.info('User logged out', user=user_model.email)


    @staticmethod
    def register_user(data):
        log.info('register_user', data=data)
        user_model = UserModel(**data).create_user()
        user_model.generate_token()
        return user_schema.dump(user_model), user_model.token


    @staticmethod
    def get_all_users(limit, offset):
        user_model = UserModel()
        users = user_model.get_all_users(limit, offset)
        return users_schema.dump(users)

    @staticmethod
    def get_user_by_id(user_id):
        user_model = UserModel()
        user = user_model.get_user_by_id(user_id)
        return user_schema.dump(user)

    @staticmethod
    def get_user_by_email(email):
        user_model = UserModel()
        user = user_model.get_user_by_email(email)
        return user_schema.dump(user)

    @staticmethod
    def create_user(data):
        user_model = UserModel(**data).create_user()
        return user_schema.dump(user_model)

    @staticmethod
    def update_user(user_id, data):
        new_user = UserModel(**data)
        user_model = UserModel().get_user_by_id(user_id)
        user_model.update_user(new_user)
        return user_schema.dump(user_model)

    @staticmethod
    def update_user_by_email(email, data):
        new_user = UserModel(**data)
        user_model = UserModel().get_user_by_email(email)
        user_model.update_user(new_user)
        return user_schema.dump(user_model)

    @staticmethod
    def delete_user(user_id: int):
        user_model = UserModel()
        user_model.delete_user(user_id)
        return user_schema.dump(user_model)