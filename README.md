# SMG Test Interview
 Answer for test automation project

## Setup

### Requirements

1. Python 3.6+
    
    - For Windows, download latest python version from [here](https://www.python.org/downloads/windows/) and run the installer executable
    - For Mac and Linux, run `python --version` to see what python version is pre-installed. If you want a different version download from [here](https://www.python.org/downloads/)

2. Package Manager pip

    Note : `pip` comes installed with Python 2.7.9+ and python 3.4+

    - If `pip` is not installed, follow these instructions:
        - Securely download get-pip.py by following this link: [get-pip.py](https://bootstrap.pypa.io/get-pip.py) or use following cURL command to download it:

        ```sh
        curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
        ```

        - After dowloading, run the file :

            - For Python 3

                ```sh
                python3 get-pip.py
                ```

### Install the dependencies

To install the dependencies, run the following command in project's base directory:

- For Python 3

    ```sh
    pip3 install -r requirements.txt
    ```
    Or
    
    ```sh
    python -m pip install -r requirements.txt
    ```

### Run your test ():
- For Question 2
Run thoes 3 file for the test
```
robot API/tests/valid_data.robot  
robot API/tests/invalid_search.robot
robot API/tests/invalid_offset.robot

```
- For Question 3

```
robot -V UI/config/wiki.yaml -d results -T --report NONE UI/tests/test_nofound_search.robot
robot -V UI/config/wiki.yaml -d results -T --report NONE UI/tests/test_valid_basic_searh.robot

```