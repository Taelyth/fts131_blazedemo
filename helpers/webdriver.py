from helpers.helper_base import HelperFunc


def __init__(self, driver):
    super(HelperFunc, self).__init__()
    self._driver = driver

    HelperFunc.open(self, 'url')
