

# Assistant Bot
A bot to help you do things differently

[![Stories in Ready](https://badge.waffle.io/spaamteam/airbnbchallenge.png?label=ready&title=Ready)](https://waffle.io/spaamteam/airbnbchallenge)
[![Code Climate](https://codeclimate.com/github/spaamteam/airbnbchallenge/badges/gpa.svg)](https://codeclimate.com/github/spaamteam/airbnbchallenge)
[![Build Status](https://travis-ci.org/spaamteam/airbnbchallenge.svg?branch=master)](https://travis-ci.org/spaamteam/airbnbchallenge)
[![Coverage Status](https://coveralls.io/repos/spaamteam/airbnbchallenge/badge.svg?branch=master&service=github)](https://coveralls.io/github/spaamteam/airbnbchallenge?branch=master)

## Installation:

1. Download Python 3.5 (Anaconda includes basic utility packages so one doesn't have to worry about installing them individually) from https://www.continuum.io/downloads
2. Download Git's latest version for your OS from https://git-scm.com/downloads
3. Run git-bash (Git Shell) and navigate to your source directory (e.g. `cd ~/Desktop/assistant-bot`)
4. Time to configure Git, by running `git config --global user.name "Your Name"` and then `git config --global user.email username@email.com` (make sure your email and name is same as used on GitHub while creating your account)
5. For great speed at development, install the powerful **Atom** by GitHub from https://atom.io
6. Time to configure atom to work with Git by running `git config --global core.editor "atom --wait"`
7. Run `git clone https://github.com/spaamteam/codeday.git assistant-bot` to create a folder on your computer with initial source code.
8. Navigate to this newly created directory *assistant-bot* `cd assistant-bot`
9. **Add remote to connect/modify to our team's GitHub repo `git remote add origin master https://github.com/spaamteam/codeday.git`**
10. Run test script to check if you installed properly `python3 test_install.py` , which should run test cases.
11. Test python by running `python3 your_script.py` from Terminal/Command-Prompt.
12. To edit your python script, `atom your_script.py` and atom props up, ready for you to make changes and save.

# Setup:

1. Install Anaconda
2. Run `pip install -r requirements.txt`

## Working with Git

*Required every time one wants to publish an update*
- `git status` : Informs you about which files are modified/added
- `git add filename.py` : Adds the file to version tracking
- `git commit -m "Informative Message"` : Message to inform others of the update [usually less than 50 characters]
- `git pull` : Pulls new changes from the central repository @ GitHub
- `git push` : Publishes changes to central repo for others to observe and work on

## Testing

nosetests -v --with-coverage --cover-package=assistant-bot --cover-inclusive --cover-erase tests

## Team Members (alphabetical)

Aditya Purandare, Alok Satpathy, Atif Tahir & Saddam Hussain

## References

- http://blog.pandorabots.com/connecting-a-pandorabot-to-sms-via-twilio/

## License

    Copyright 2015 SPAAM Team

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
