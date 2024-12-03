from services.userServices import UserServices


class UserControllers:
    @staticmethod
    def login_user(req):
        data = req.get_json()
        user, token = UserServices.login_user(data)
        if not user:
            return {'message': 'Invalid email or password'}, 401
        return {'message': 'success', 'data': user, 'token': token}, 200

    @staticmethod
    def register_user(req):
        data = req.get_json()
        user, token = UserServices.register_user(data)
        return {'message': 'success', 'data': user, 'token': token}, 201

    @staticmethod
    def create_user(req):
        data = req.get_json()
        user = UserServices.create_user(data)
        return {'message': 'success', 'data': user}, 201

    @staticmethod
    def get_user_by_id(user_id):
        user = UserServices.get_user_by_id(user_id)
        return {'data': user}, 200

    @staticmethod
    def update_user(req):
        user_id = req.args.get('id')
        data = req.get_json()
        user = UserServices.update_user(user_id, data)
        return {'data': user}, 200

    @staticmethod
    def delete_user(req):
        user_id = req.args.get('id')
        return UserServices.delete_user(int(user_id))

    @staticmethod
    def get_all_users(req):
        limit = req.args.get('limit') or 10
        offset = req.args.get('offset') or 0
        users = UserServices.get_all_users(limit, offset)
        return {'data': users, 'total': len(users)}, 200

    @staticmethod
    def get_user_by_email(email):
        return UserServices.get_user_by_email(email)

    @staticmethod
    def update_user_by_email(email, data):
        return UserServices.update_user_by_email(email, data)

    @staticmethod
    def logout_user(req):
        return UserServices.logout_user(req)