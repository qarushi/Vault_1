from framework.webapp import webapp


class Dashboard():
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = Dashboard()
        return cls.instance

    def __init__(self):
        self.driver = webapp.get_driver()

    


dashboard = Dashboard.get_instance()
