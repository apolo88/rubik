###Comandos iniciales

# Prerequisitos
sudo pip3 install virtualenvwrapper

export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
export PROJECT_HOME=$HOME/Devel
source /usr/local/bin/virtualenvwrapper.sh






# Compilar source
source ~/.bash_profile




# Levantar ambiente virtual
mkvirtualenv my_django_environment

# Instalar Django si hace falta
pip3 install django



# Levantar Server Django
python3 manage.py runserver

# Home
http://127.0.0.1:8000/