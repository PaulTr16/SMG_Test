import chromedriver_autoinstaller 
from SeleniumLibrary import SeleniumLibrary
from robot.libraries.BuiltIn import BuiltIn

class ExtendedSeleniumLibrary(SeleniumLibrary):
    def __init__(self):
        self.objRepo = None
        self.builtIn = BuiltIn()
        self.install = chromedriver_autoinstaller.install()
        SeleniumLibrary.__init__(self)

    def set_driver(self):
        """ When you switch to another page and use the different resource file, 
            you need to register driver from built in Selenium Library
        """
        dict = self.builtIn.get_variables()
        driver = dict["${selenium_driver}"]
        super().register_driver(driver, None)