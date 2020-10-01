from django.urls import reverse, resolve

class TestUrls:
    def test_inventory_list_url(self):
        list_path = reverse('list')
        assert resolve(list_path).view_name == 'list'

    def test_inventory_show_url(self):
        show_path = reverse('show', kwargs={'id':10})
        assert resolve(show_path).view_name == 'show'

    def test_inventory_add_url(self):
        add_path = reverse('add')
        assert resolve(add_path).view_name == 'add'

    def test_inventory_remove_url(self):
        remove_path = reverse('remove', kwargs={'id':10})
        assert resolve(remove_path).view_name == 'remove'
    
    


