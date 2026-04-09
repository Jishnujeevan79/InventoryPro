from django.apps import AppConfig

class InventoryAppConfig(AppConfig):
    name = 'inventory_app'

    def ready(self):
        import inventory_app.signals