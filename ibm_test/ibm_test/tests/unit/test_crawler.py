
from tests.factories.crawler_factory import URLFactory, update_mock



def test_update():
    url = URLFactory()
    url_updated = update_mock(url.id,{"visited": True})
    assert url_updated == True
    

    