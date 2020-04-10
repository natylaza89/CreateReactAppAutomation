import sys
import os
import json
import concurrent.futures

from decorator import creator_logger
from logger import Logger


class CreateReactApp:

    def __init__(self, project_name="react_project"):
        self.__project_name = sys.argv[1] if len(sys.argv) > 1 else project_name
        self.__folders_to_create = None
        self.__packages_list = None

    def __repr__(self):
        return f"CreateReactApp('{self.project_name}')"

    @property
    def project_name(self):
        return self.__project_name

    @project_name.setter
    def project_name(self, project_name):
        self.__project_name = project_name

    @property
    def folders_to_create(self):
        return self.__folders_to_create

    @folders_to_create.setter
    def folders_to_create(self, folders_to_create):
        self.__folders_to_create = folders_to_create

    @property
    def packages_list(self):
        return self.__packages_list

    @packages_list.setter
    def packages_list(self, packages_list):
        self.__packages_list = packages_list

    def __create_project_folders(self, project_name):
        """" Gets folders's list from json file and then creates it """
        with open("folders.json", "r") as json_file:
            folders_to_create = json.load(json_file)
            self.folders_to_create = folders_to_create['folders']

            with concurrent.futures.ThreadPoolExecutor() as executer:
                results = (executer.submit(
                    os.makedirs(f'{self.project_name}/src/{folder}', exist_ok=True), folder)
                        for folder in self.folders_to_create)

                for _ in concurrent.futures.as_completed(results):
                    pass

    def __create_react_app(self):
        """ Creates React App via command line """
        command_status = os.system(f'create-react-app {self.project_name}')
        return command_status

    def __install_packages(self):
        """" Gets packages's list from json file and then creates it """
        with open("packages.json", "r") as json_file:
            packages_list = json.load(json_file)
            self.packages_list = ' '.join(packages_list['packages'])
            os.system(f"cd {sys.path[0]}//{self.project_name} & npm install --save {self.packages_list}")

    @creator_logger(logger_instance=Logger())
    def run(self):
        project_creation_status = self.__create_react_app()
        if project_creation_status == 0:
            result = []

            with concurrent.futures.ThreadPoolExecutor() as executer:
                result.append(executer.submit(self.__create_project_folders))
                result.append(executer.submit(self.__install_packages))

                for _ in concurrent.futures.as_completed(result):
                    pass
        else:
            print("operation failed")