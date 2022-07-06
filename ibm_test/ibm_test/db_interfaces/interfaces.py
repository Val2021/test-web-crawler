from models.models import URL, Base

MOCK = [
    URL(id=1, url="https://www.ibm.com/br-pt/", depth=1, visited=False),
    URL(
        id=2,
        url="https://www.ibm.com/lets-create/br-pt/?lnk=hpmlc",
        depth=2,
        visited=False,
    ),
    URL(
        id=3,
        url="https://www.ibm.com/br-pt/analytics/data-fabric",
        depth=3,
        visited=False,
    ),
]


class Postgres:
    def __init__(self, session, model):
        self.session = session
        self.model = model

    def save(self, model: Base):
        # self.session.add(model)
        # self.session.commit()
        # self.session.refresh(model)
        model.id = MOCK[-1].id + 1
        MOCK.append(model)
        return model

    def get_all_url(self):
        return MOCK
        # return self.session.query(self.model).all()

    def get_url_not_visited(self):
        list_url = []
        for url in MOCK:
            if url.visited == False:
                list_url.append(url)
        return list_url
        # return self.session.query(self.model).filter_by(visited==False).first()

    def update_url(self, id: int, attributes: dict):
        for url in MOCK:
            if url.id == id:
                if "url" in attributes.keys():
                    url.url = attributes["url"]
                if "depth" in attributes.keys():
                    url.depth = attributes["depth"]
                if "visited" in attributes.keys():
                    url.visited = attributes["visited"]
                return True
        return False
        # self.query().filter_by(id=id).update(attributes)
        # self.session.commit()
        # return self.query().filter_by(id=id).first()
