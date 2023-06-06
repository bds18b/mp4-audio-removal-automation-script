# MP4 Audio Removal Automation with Python 

A Python script that automates audio removal from MP4 files by using moviepy.\
I made this because I had a lot of MP4 files that I needed to remove audio from. I figured someone else might find this useful. 

## Table of Contents

- [Background Removal Automation with Python Selenium](#background-removal-automation-with-python-selenium)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Installation and Instructions](#installation-and-instructions)
  - [Dependencies](#dependencies)
  - [License](#license)


## Introduction

This project provides a Python script that removes the audio from all MP4 files within 
the folder 'videos-with-audio' and outputs them to the folder 'videos-with-no-audio' 


## Installation and Instructions

Clone the repository

To use this script, you need to have the moviepy library installed. You can install it using pip:

```bash
pip3 install moviepy
```

To run the script, you first need to put your MP4 files within the 'videos-with-audio folder'\
Running the script will create a new folder 'videos-with-no-audio' in the same directory and will save the new videos with no audio to that folder. 

## Dependencies

- Python 3.8 or higher
- moviepy

## License
[MIT License Text](https://opensource.org/licenses/MIT)