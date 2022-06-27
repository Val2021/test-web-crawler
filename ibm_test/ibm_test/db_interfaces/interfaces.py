
from ibm_test.models.models import Base



MOCK = []

class Postgres:
    def __init__(self, session, model):
        self.session = session
        self.model = model
    
    def save(self, model: Base):
        # self.session.add(model)
        # self.session.commit()
        # self.session.refresh(model)
        MOCK.append(model)
        print(MOCK)
        return model
    
    def get_all_url(self):
        return MOCK
        # return self.session.query(self.model).all()
