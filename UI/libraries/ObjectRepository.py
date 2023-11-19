import os

from SeleniumLibrary import SeleniumLibrary

from SeleniumLibrary import SeleniumLibrary

from robot.libraries.BuiltIn import BuiltIn

from robot.api import logger

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class ObjectRepository(metaclass=SingletonMeta):
    def load_object_repositories(self, obj_repo_dir=None):
        execdir = BuiltIn().get_variable_value('${EXECDIR}')
        if(obj_repo_dir is None):
            obj_repo_dir = execdir + 'UI/resources/data/object_repositories/'
        for root, _, files in os.walk(obj_repo_dir): #Get the root, files
            for x in files:
                if x.endswith('.yaml'): #Check the extension
                    yamlFile = f'{root}/{x}'
                    if(not yamlFile.startswith("/")):
                        yamlFile =  execdir + '/' + yamlFile
                    BuiltIn().import_variables(yamlFile)

