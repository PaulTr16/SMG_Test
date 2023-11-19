import sys
import os
sys.path.append(os.getcwd() + '/UI/libraries')

from wiki.WikiBasePage import WikiBasePage
from SeleniumLibrary.base import keyword
from robot.libraries.BuiltIn import BuiltIn



class WikiSearchPage(WikiBasePage):
    def __int__(self):
        WikiBasePage.__intit__(self)
        
    @keyword
    def go_to_search_page(self):
        self.set_driver()

    @keyword
    def search_page_input_search_value(self,text):
        search_textbox_field = self.builtIn.get_variable_value("${SearchPage.search_input_tab}")
        self.mouse_over(search_textbox_field)
        self.input_text(search_textbox_field,text)
        
    
    @keyword
    def search_page_click_search_bnt(self):
        search_bnt = self.builtIn.get_variable_value("${SearchPage.search_btn}")
        print(search_bnt)
        self.click_button(search_bnt)


#----------------------VERIFYING------------------------------------------------
    @keyword
    def ui_search_page(self):
        h1=self.builtIn.get_variable_value("${SearchPage.search_heading}")
        search_textbox_field = self.builtIn.get_variable_value("${SearchPage.search_input_tab}")
        advanced_search= self.builtIn.get_variable_value("${SearchPage.advanced_search_tab}")
        search_in = self.builtIn.get_variable_value("${SearchPage.search_in_tab}")
        self.page_should_contain_element(h1)
        self.page_should_contain_element(search_textbox_field)
        self.page_should_contain_element(advanced_search)
        self.page_should_contain_element(search_in)


    @keyword
    def verify_no_result(self,text):
        none_found_mess= self.builtIn.get_variable_value("${SearchResult.none_found_message}")
        create_draft_submit=self.builtIn.get_variable_value("${SearchResult.create_draft_and_submit}")
        request_redirect=self.builtIn.get_variable_value("${SearchResult.request_redirect_created}")
        result_container = self.builtIn.get_variable_value("${SearchResult.page_results_container}")

        self.page_should_contain_element(f"//a[@title='{text.capitalize()} (page does not exist)']")
        
        self.page_should_contain_element(none_found_mess)
        self.page_should_contain_element(create_draft_submit)
        self.page_should_contain_element(request_redirect)
        self.page_should_not_contain_element(result_container)

    @keyword
    def page_contain_result_container(self):
        result_container = self.builtIn.get_variable_value("${SearchResult.page_results_container}")
        self.page_should_contain_element(result_container)

        


    
