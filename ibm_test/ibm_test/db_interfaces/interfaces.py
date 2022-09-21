from models.models import URL, Base


class Postgres:
    def __init__(self, session, model):
        self.session = session
        self.model = model

    def save(self, model: Base):
        self.session.add(model)
        self.session.commit()
        self.session.refresh(model)
        return model

    def get_all_url(self):
        return self.session.query(self.model).all()

    def get_url_not_visited(self):
        return self.session.query(self.model).filter_by(visited=False)

    def update_url(self, id: int, attributes: dict):
        self.session.query(self.model).filter(URL.id == id).update(attributes)
        self.session.commit()
        return self.session.query(self.model).filter(URL.id == id).first()

    def get_url_by_url(self, url: str):
        return self.session.query(self.model).filter_by(url=url)
