# StuffDoer: Auto clicker and texter


## Installation 

download and extract stuffdoer.zip from [Release](https://github.com/Kan5661/StuffDoer/releases/tag/windows)


## Functionalities

1. **Text Writing:** Allows users to automate input text.
   

https://github.com/Kan5661/StuffDoer/assets/75275776/37f3ee60-53b5-4d13-9a73-16aa142296f8


2. **Clicker:** Provides functionality to automate clicking events.


https://github.com/Kan5661/StuffDoer/assets/75275776/45b2ad26-e371-412f-95a7-ebe4d2548ad8


https://github.com/Kan5661/StuffDoer/assets/75275776/8e573a42-9802-445a-9c3d-4c71ebaa37a0



## Usage

To use the StuffDoer application, follow these steps:

### MAC
1. **Clone the repo and cd into it:**
   ```bash
   git clone https://github.com/Kan5661/StuffDoer.git && cd StuffDoer
2. **Install the requirements:**
    ```bash
    pip install -r requirements.txt
3. **Run StuffDoer.py file:**
    ```bash
    sudo python StuffDoer.py
note: you may need to run the file with admin privilege (sudo command) for it to access and control the keyboard and mouse

### Windows
1. **Follow MAC step 1 & 2**
2. ****Run StuffDoer.py file:****
   ```bash
   python StuffDoer.py

note: You might have to run your terminal as administrator

## Build from code
this is for if you want to modify the code/image assets and recompile
1. **Clone the repository:**
    ``` bash
    git clone https://github.com/Kan5661/StuffDoer.git && cd StuffDoer
2. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt and 
   ```bash
   pip install pyinstaller
4. **Run build command:**
   ```bash
   pyinstaller --icon ./png/Icon.ico --onefile .\StuffDoer.py --windowed --noconsole --add-data "png;png"
   
   

## License
MIT
