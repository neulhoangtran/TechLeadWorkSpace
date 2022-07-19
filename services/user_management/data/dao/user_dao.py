from ...domain.entities.user import User


class UserDAO(User):
    def __init__(self,
                id: int,
                first_name: str,
                last_name: str,
                phone_number: str,
                user_name: str,
                password: str,
                email: str,
                *args, **kwargs) -> None:
        super().__init__(id, first_name, last_name, phone_number, user_name, password, password, email, *args, **kwargs)
    @staticmethod
    def from_json(json_data) -> User:
        try:
            return User(
                json_data['id'],
                json_data['first_name'],
                json_data['last_name'],
                json_data['phone_number'],
                json_data['user_name'],
                json_data['password'],
                json_data['email']
            )
        except Exception as ex:
            return None