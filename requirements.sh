#!/usr/bin/env bash

# colors for emphasizing message
NOCOLOR='\033[0m'
#RED='\033[0;31m'
GREEN='\033[0;32m'
ORANGE='\033[0;33m'
BLUE='\033[0;34m'
#PURPLE='\033[0;35m'
#CYAN='\033[0;36m'
#LIGHTGRAY='\033[0;37m'
#DARKGRAY='\033[1;30m'
#LIGHTRED='\033[1;31m'
#LIGHTGREEN='\033[1;32m'
#YELLOW='\033[1;33m'
#LIGHTBLUE='\033[1;34m'
#LIGHTPURPLE='\033[1;35m'
#LIGHTCYAN='\033[1;36m'
#WHITE='\033[1;37m'

LINE_COUNT="THIS IS JUST A PHRASE TO GENREATE THE LINE SEPERATOR DURING EXECUTION"
LINE_SEPERATOR="-"


#_______ VAULT.PY SETUP ____#
# create file [recipes/vault.py]
echo -e "${BLUE}creating file${NOCOLOR} ${GREEN}[vault.py]${NOCOLOR} ${BLUE}in folder${NOCOLOR} ${GREEN}recipes${NOCOLOR}"
touch recipes/vault.py
echo -e "${BLUE}file${NOCOLOR} ${GREEN}[recipes/vault.py]${NOCOLOR} ${BLUE}created${NOCOLOR}"
echo "\n"
echo -e "${LINE_COUNT//?/$LINE_SEPERATOR}\n${LINE_COUNT//?/$LINE_SEPERATOR}"
echo "\n"

# set neccesary variables in vault.py
#---- EMAIL_HOST ----#
echo -e "${BLUE}setting${NOCOLOR} ${ORANGE}[EMAIL_HOST_USER]${NOCOLOR} ${BLUE}variable in${NOCOLOR} ${GREEN}vault.py${NOCOLOR}"
echo -e "EMAIL_HOST = None" >> recipes/vault.py
echo -e "${ORANGE}[EMAIL_HOST_USER]${NOCOLOR} ${BLUE}variable set${NOCOLOR}"
echo "\n"
echo -e "${LINE_COUNT//?/$LINE_SEPERATOR}\n${LINE_COUNT//?/$LINE_SEPERATOR}"
echo "\n"

#---- EMAIL_HOST_USER ----#
echo -e "${BLUE}setting${NOCOLOR} ${ORANGE}[EMAIL_HOST_USER]${NOCOLOR} ${BLUE}variable in${NOCOLOR} ${GREEN}vault.py${NOCOLOR}"
echo -e "EMAIL_HOST_USER = None" >> recipes/vault.py
echo -e "${ORANGE}[EMAIL_HOST_USER]${NOCOLOR} ${BLUE}variable set${NOCOLOR}"
echo "\n"
echo -e "${LINE_COUNT//?/$LINE_SEPERATOR}\n${LINE_COUNT//?/$LINE_SEPERATOR}"
echo "\n"

#---- EMAIL_HOST_PASSWORD ----#
echo -e "${BLUE}setting${NOCOLOR} ${ORANGE}[EMAIL_HOST_PASSWORD]${NOCOLOR} ${BLUE}variable in${NOCOLOR} ${GREEN}vault.py${NOCOLOR}"
echo -e "EMAIL_HOST_PASSWORD = None" >> recipes/vault.py
echo -e "${ORANGE}[EMAIL_HOST_PASSWORD]${NOCOLOR} ${BLUE}variable set${NOCOLOR}"
echo "\n"

#---- DEFAULT_FROM_EMAIL ----#
echo -e "${BLUE}setting${NOCOLOR} ${ORANGE}[DEFAULT_FROM_EMAIL]${NOCOLOR} ${BLUE}variable in${NOCOLOR} ${GREEN}vault.py${NOCOLOR}"
echo -e "DEFAULT_FROM_EMAIL = None" >> recipes/vault.py
echo -e "${ORANGE}[DEFAULT_FROM_EMAIL]${NOCOLOR} ${BLUE}variable set${NOCOLOR}"
echo "\n"
echo -e "${LINE_COUNT//?/$LINE_SEPERATOR}\n${LINE_COUNT//?/$LINE_SEPERATOR}"
echo "\n"

#---- DATABASE_PASSWORD ----#
echo -e "${BLUE}setting${NOCOLOR} ${ORANGE}[DEFAULT_FROM_EMAIL]${NOCOLOR} ${BLUE}variable in${NOCOLOR} ${GREEN}vault.py${NOCOLOR}"
echo -e "DATABASE_PASSWORD = None" >> recipes/vault.py
echo -e "${ORANGE}[DEFAULT_FROM_EMAIL]${NOCOLOR} ${BLUE}variable set${NOCOLOR}"
echo "\n"
echo -e "${LINE_COUNT//?/$LINE_SEPERATOR}\n${LINE_COUNT//?/$LINE_SEPERATOR}"
echo "\n"
#____ END VAULTY.PY SETUP ____#


#___ SETUP PYTHON3 VIRTUALENV __#
echo -e "${BLUE}creating virtual environment named${NOCOLOR} ${ORANGE}[venv]${NOCOLOR}"
python3 -m venv venv
echo -e "${BLUE}virtual environment ${ORANGE}[venv]${NOCOLOR} created"
echo "\n"
echo -e "${LINE_COUNT//?/$LINE_SEPERATOR}\n${LINE_COUNT//?/$LINE_SEPERATOR}"
echo "\n"

echo -e "${BLUE}initiating virtual environment${NOCOLOR} ${ORANGE}[venv]"
source venv/bin/activate
echo -e "${BLUE}virtual environment initiated${NOCOLOR}"
echo "\n"
echo -e "${LINE_COUNT//?/$LINE_SEPERATOR}\n${LINE_COUNT//?/$LINE_SEPERATOR}"
echo "\n"


#____ INSTALL REQUIREMENTS.TXT ____#
# change from "equal to" to "greater than or equal to"
# for fetching the latest package in requirements.txt
echo -e "${BLUE}editing${NOCOLOR} ${ORANGE}[==]${NOCOLOR} ${BLUE}in${NOCOLOR} ${GREEN}requirements.txt${NOCOLOR} ${BLUE}to${NOCOLOR} ${ORANGE}[>=]${NOCOLOR}"
sed -i 's/==/>=/g' requirements.txt
echo -e "${BLUE}changes made in${NOCOLOR} ${GREEN}requirements.txt${NOCOLOR}"
echo "\n"
echo -e "${LINE_COUNT//?/$LINE_SEPERATOR}\n${LINE_COUNT//?/$LINE_SEPERATOR}"
echo "\n"

echo -e "${BLUE}installing requirements from${NOCOLOR} ${GREEN}requirements.txt${NOCOLOR}"
pip install -r requirements.txt
echo -e "${BLUE}requirements installed${NOCOLOR}"
echo "\n"
echo -e "${LINE_COUNT//?/$LINE_SEPERATOR}\n${LINE_COUNT//?/$LINE_SEPERATOR}"
echo "\n"


#____ CREATE MISSING MIGRATION FOLDERS ____#
echo -e "${BLUE}creating${NOCOLOR} ${GREEN}migrations${NOCOLOR} ${BLUE}folders for django${NOCOLOR} ${GREEN}[APP_NAME]${NOCOLOR} ${BLUE}apps${NOCOLOR}"
mkdir account/migrations
touch account/migrations/__init__.py
echo -e "${GREEN}migrations${NOCOLOR} ${BLUE}folder in${NOCOLOR} ${GREEN}[APP_NAME]${NOCOLOR} ${BLUE}app created${NOCOLOR}"
echo "\n"
echo -e "${LINE_COUNT//?/$LINE_SEPERATOR}\n${LINE_COUNT//?/$LINE_SEPERATOR}"
echo "\n"

echo -e "${BLUE}creating${NOCOLOR} ${GREEN}migrations${NOCOLOR} ${BLUE}folders for django${NOCOLOR} ${GREEN}[APP_NAME]${NOCOLOR} ${BLUE}apps${NOCOLOR}"
mkdir blog/migrations
touch blog/migrations/__init__.py
echo -e "${BLUE}migrations${NOCOLOR} ${BLUE}folder in ${GREEN}[APP_NAME]${NOCOLOR} ${BLUE}app created${NOCOLOR}"
echo "\n"
echo -e "${LINE_COUNT//?/$LINE_SEPERATOR}\n${LINE_COUNT//?/$LINE_SEPERATOR}"
echo "\n"


#____ INITIATE GIT ____#
echo -e "${BLUE}initializing git${NOCOLOR}"
git init
echo -e "${BLUE}git initiated${NOCOLOR}"
echo "\n"
echo -e "${LINE_COUNT//?/$LINE_SEPERATOR}\n${LINE_COUNT//?/$LINE_SEPERATOR}"
echo "\n"


#____ CREATE GITIGNORE FILE ____#
echo -e "${BLUE}creating${NOCOLOR} ${GREEN}.gitignore${NOCOLOR} ${BLUE}file${NOCOLOR}"
touch .gitignore
echo -e "venv/" >> .gitignore
echo -e "vault.py" >> .gitignore
echo -e "db.sqlite3" >> .gitignore
echo -e "migrations/" >> .gitignore
echo -e "venv/" >> .gitignore
echo -e "__pycache__" >> .gitignore
echo -e ".DS_Store" >> .gitignore
echo -e "static/admin" >> .gitignore
echo -e "session_security/" >> .gitignore
echo -e "cloud_sql_proxy" >> .gitignore
echo -e ".gcloudignore" >> .gitignore
echo -e "${GREEN}.gitignore${NOCOLOR} ${BLUE}file created${NOCOLOR}"
echo "\n"
echo -e "${LINE_COUNT//?/$LINE_SEPERATOR}\n${LINE_COUNT//?/$LINE_SEPERATOR}"
echo "\n"
