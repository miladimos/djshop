from django_unicorn.components import UnicornView


class CartView(UnicornView):

    def mount(self):
        return super().mount()
