from framework.webapp import webapp


class MyModel():
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = MyModel()
        return cls.instance

    def __init__(self):
        self.driver = webapp.get_driver()

    


mymodel = MyModel.get_instance()
