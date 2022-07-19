from kink import inject

from ..repository.house_repository import HouseRepository


@inject
class BaseHouseUsecase:
    def __init__(self, repository: HouseRepository) -> None:
        self.repository = repository