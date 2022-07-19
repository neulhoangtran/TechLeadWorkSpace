from ...domain.entities.house import House


class HouseDAO(House):
    def __init__(self, id: int, owner_id: int, country: str, city: str, district: str, address_detail: str, note: str, house_status: int, house_type_id: int, *args, **kwargs) -> None:
        super().__init__(id, owner_id, country, city, district, address_detail, note, house_status, house_type_id, *args, **kwargs)

    @staticmethod
    def from_json(json_data) -> House:
        return House(1, json_data['owner_id'], json_data['country'], json_data['city'], json_data['district'], json_data['address_detail'], json_data['note'], json_data['house_status'], json_data['house_type_id'])