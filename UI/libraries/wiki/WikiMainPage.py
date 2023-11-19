import sys
import os
sys.path.append(os.getcwd() + '/UI/libraries')

from wiki.WikiBasePage import WikiBasePage
from SeleniumLibrary.base import keyword

class WikiMainPage(WikiBasePage):
    def __int__(self):
        WikiBasePage.__intit__(self)

    @keyword
    def go_to_main_page(self):
        self.set_driver()
        self.go_to(self.builtIn.get_variable_value("${Wiki.url}"))

    @keyword
    def main_page_input_search_value_and_go_to_search_page(self,text):
        self.main_page_input_search_value(text)  
        self.main_page_click_search_for_page_contain()

    @keyword
    def main_page_click_search_bnt(self):
        main_search_bnt = self.builtIn.get_variable_value("${MainPage.search_bnt}")
        self.wait_until_element_is_visible(main_search_bnt)
        self.click_button(main_search_bnt)


    def main_page_input_search_value(self,text):
        self.builtIn.sleep(3)
        main_search_textbox = self.builtIn.get_variable_value("${MainPage.main_search_box}")
        self.mouse_over(main_search_textbox)
        self.input_text(main_search_textbox,text)
        
    
    def main_page_click_search_for_page_contain(self):
        page_contain_dropdown= self.builtIn.get_variable_value("${MainPage.search_for_page_contain}")
        self.wait_until_element_is_visible(page_contain_dropdown)
        self.click_element(page_contain_dropdown)

    
    

    

    
    
    
