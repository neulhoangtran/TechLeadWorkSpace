from kink import inject

from ..repository.user_repository import UserRepository


@inject
class BaseUserUsecase:
    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository