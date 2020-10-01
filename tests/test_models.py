from shop_bridge.models import inventory
from mixer.backend.django import mixer


class TestModels:
    def inventory_price_is_high(self):
        price = mixer.blend('inventory', price=500)
        assert price.is_price_high == True


