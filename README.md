# Chess Tournament Management

## Description

 This programme was created to manage chess tournaments according to the swiss system. 

## Setup

Create a virtualenv for the project with Python 3.10.4  
    
```
python -m venv env 
source env/bin/activate
pip install -r requirements.txt 
```  

## Run the script  

Run this command:  

```
python3 controllers.py
```    
## How to use it

After run the script, You can follow the different menu by typing the action you want to do.
Create a new tournament, display some report or quit the script.

## Flake8 report
There is a flake8-html report with no error.
There is a setup.cfg file with this configuration : 
exclude = __pycache__,venv,README.md,
max-line-length = 119

You can also generate another flake8-html report.
Run this command

```
flake8 --format=html --htmldir=flake-report
```


## What I learned with this project is

I learned to use a Model-View-Controller pattern.
To built functions independent, to allow an easier maintenance of the code in case of modification.
And I also learned to respect the PEP8 writing convention.
I was also able to learn object-oriented programming with the manipulation of object classes.
I was also able to use git and GitHub more often,
I better understood how to access the code history. 
For this project I also used PyCharm,
which allowed me to see the possibilities and advantages of an IDE for python. 
