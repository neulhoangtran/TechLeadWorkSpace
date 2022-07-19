class House:
    def __init__(self, id: int, owner_id: int, country: str, city: str, district: str, address_detail: str, note: str, house_status: int, house_type_id: int) -> None:
        self.id = id
        self.owner_id = owner_id
        self.country = country
        self.city = city
        self.district = district
        self.address_detail = address_detail
        self.note = note
        self.house_status = house_status
        self.house_type_id = house_type_id
