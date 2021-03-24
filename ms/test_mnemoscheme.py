from ms.mnemoscheme_application import MnemoschemeApplication
from random import randrange


class TestMnemoscheme(MnemoschemeApplication):

    def __init__(self, driver):
        super().__init__(driver)

    def __str__(self):
        return 'TestMnemoscheme'

    def test_factory(self):
        self.setup_factory()
        self.setup_home_button()

    def test_phc(self):
        self.setup_phc()
        self.setup_home_button()

    def test_plc(self):
        self.setup_plc()
        self.setup_home_button()

    def test_okri(self):
        self.setup_okri()
        self.setup_home_button()

    def test_trends(self):
        self.setup_trends()
        self.setup_home_button()

    def login(self):
        self.setup_login(log='sam', passwd='sam')

    def start_methods_tm(self):
        methods_def = []

        for method in dir(self):
            if 'test' in method:
                methods_def.append(method)
        random_index = randrange(len(methods_def))
        method_name = methods_def[random_index]
        getattr(self, method_name)()


