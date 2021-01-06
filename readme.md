# GCDev Python Website Speed Tests

## Ensure Using Software Versions
* python 3.8.6
* pip 20.2.4

## Install Dependencies
* pip install selenium
* pip install webdriver_manager

## Running The Speed Tests
* write your code inside the "run_speed_tests.py" file
* create a python list of websites (without the beginning http or www.)
* pass the list of website to the *RunPageSpeedTests( website_list )* function
* then run the entire file via the command *python3 run_speed_tests.py*

## What Does It Test?
* Initial Server Response Time
* Server Page Loadtime (in Chrome)

### Intial Server Response
(measured in seconds)
* First Connected
* Time Till First Byte
* Total Time for Server Response

### Server Page Loadtime
(measured in seconds)
* Back End Connection Loaded Time
* Front End DOM Content Loaded Time
* Total Time for Page to Load
