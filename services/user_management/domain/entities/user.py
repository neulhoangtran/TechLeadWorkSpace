class User:
    def __init__(self,
                id: int,
                first_name: str,
                last_name: str,
                phone_number: str,
                user_name: str,
                password: str,
                email: str,
                *args, **kwargs) -> None:
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.user_name = user_name
        self.password = password
        self.email = email
            