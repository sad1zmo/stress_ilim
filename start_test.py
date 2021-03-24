import os
from random import randrange
import logging
import datetime as dt
from ms.test_mnemoscheme import TestMnemoscheme
from driver.wd import SelDrv


class Start:

    def __init__(self):
        self.drv = SelDrv()
        self.tm = TestMnemoscheme(self.drv)
        self.path = './logs/'
        os.makedirs(self.path, exist_ok=True)
        self.time = dt.datetime.now().strftime("%d.%m.%Y")
        logging.basicConfig(filename=f'./logs/{self.time}.log', format='%(asctime)s;%(message)s', datefmt='%d-%m-%Y %H:%M:%S')

    def run(self):
        dicts = {
            0: ['start_methods_tm', self.tm],
        }

        while True:
            random_method = randrange(len(dicts))
            getattr(dicts[random_method][1], dicts[random_method][0])()


st = Start()
st.tm.login()
# st.tm.test_factory()
# st.tm.test_phc()
# st.tm.test_plc()
# st.tm.test_okri()
# st.tm.test_trends()
st.run()



