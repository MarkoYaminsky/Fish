from datetime import date


class FishInfo:
    def __init__(self, name: str, price: float, due_date: tuple, origin: str, catch_date: tuple) -> None:
        self.name = name
        self.price_in_uah_per_kilo = price
        self.due_date = date(*due_date)
        self.origin = origin
        self.catch_date = date(*catch_date)


class Fish(FishInfo):
    def __init__(self, name: str, price: float, due_date: tuple, origin: str, catch_date: tuple,
                 age_in_months: float, weight: float) -> None:
        super().__init__(name, price, due_date, origin, catch_date)
        self.weight = weight
        self.age_in_months = age_in_months


class FishBox:
    def __init__(self, fish_info: FishInfo, weight: float, package_date: tuple, height: float,
                 length: float, width: float, is_alive: bool) -> None:
        self.fish_info = fish_info
        self.package_date = date(*package_date)
        self.weight = weight
        self.height = height
        self.width = width
        self.length = length
        self.is_alive = is_alive


class FishShop:
    def __init__(self, fish_boxes: dict[str: list[Fish]], fresh_fish: dict[str: list[Fish]])-> None:
        self.fish_boxes = fish_boxes
        self.fresh_fish = fresh_fish

    def get_fish_names_sorted_by_price(self) -> list[tuple[str, bool, float]]:
        all_fish = []
        for value in self.fresh_fish.values():
            for fish in value:
                all_fish.append((fish.name, fish.is_alive, fish.price_in_uah_per_kilo))
        return sorted(all_fish, key=lambda x: x.price_in_uah_per_kilo)

    def get_fresh_fish_names_sorted_by_price(self) -> list[tuple[str, float]]:
        all_fish = []
        for value in self.fresh_fish.values():
            for fish in value:
                if fish.is_alive:
                    all_fish.append((fish.name, fish.price_in_uah_per_kilo))
        return sorted(all_fish, key=lambda x: x.price_in_uah_per_kilo)

    def get_frozen_fish_names_sorted_by_price(self) -> list[tuple[str, float]]:
        all_fish = []
        for value in self.fresh_fish.values():
            for fish in value:
                if not fish.is_alive:
                    all_fish.append((fish.name, fish.price_in_uah_per_kilo))
        return sorted(all_fish, key=lambda x: x.price_in_uah_per_kilo)

    def add_fish(self, fish: Fish) -> None:
        self.fresh_fish.setdefault(fish.name, []).append(fish)

    def add_fish_box(self, fish_box: FishBox) -> None:
        self.fish_boxes.setdefault(fish_box.fish_info.name, []).append(fish_box)

    def sell_fish(self, name: str, weight: float, is_fresh: bool):
        for i in range(len(self.fresh_fish[name])):
            if self.fresh_fish[name][i].weight == weight and self.fresh_fish[name][i].is_fresh is is_fresh:
                fish = self.fresh_fish[name].pop(i)
                return fish.price_in_uah_per_kilo
