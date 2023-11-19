import sys
import os
sys.path.append(os.getcwd() + '/UI/libraries')

from ExtendedSeleniumLibrary import ExtendedSeleniumLibrary
from ObjectRepository import ObjectRepository
from selenium.webdriver.chrome.options import Options
from SeleniumLibrary.base import keyword


class WikiBasePage(ExtendedSeleniumLibrary):
    def __intit__(self):
        ExtendedSeleniumLibrary.__init__()
    

    @keyword
    def open_web_browser(self):
        if(self.objRepo is None):
            self.objRepo = ObjectRepository()
            execdir = self.builtIn.get_variable_value('${EXECDIR}')
            objRepoDirs = self.builtIn.get_variable_value('${Wiki.object_repositories}')
            self.objRepo.load_object_repositories(execdir+objRepoDirs)

        web_browser =  self.builtIn.get_variable_value("${Wiki.web_browser}")
        caps = self.builtIn.get_variable_value("${Wiki.caps}")
        chrome_options=self._get_browsers_option(caps)
        self.open_browser(browser=web_browser,options=chrome_options)
        self.builtIn.set_global_variable("${selenium_driver}", self.driver)

    def _get_browsers_option(self,caps):
            #print(caps)
            options=(caps['chromeOptions']['args'])
            chrome_options = Options()
            for option in options: 
                chrome_options.add_argument(option)
            return chrome_options