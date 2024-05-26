#!/bin/bash

## set/export pyenv vars
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
if command -v pyenv 1>/dev/null 2>&1; then
 eval "$(pyenv init --path)"
fi

#checking pyenv commands
pyenv versions

#Enable reqd python from pyenv
pyenv global 3.10.0 #Colocamos la version de python a usar
python -m venv myenv # creamos el entorno virtual
source myenv/bin/activate # lo activamos
python -V # verificamos la version de python
which python # vemos la ubicacion de python

#Verificar que el codigo se haya clonado
ls -l

#Instalar los requirements.txt
pip install -r ./requirements.txt

#Correr las pruebas
echo '###### Running API Tests#####'
pytest APIPetStoreTests --junitxml=./xmlReport/output.xml
#--alluredir=./allure_results: Esto especifica el directorio donde se guardarán los resultados de las pruebas en formato Allure.
#--junitxml=./xmlReport/output.xml: Esto especifica la ubicación donde se guardará el informe de resultados en formato JUnit XML.

#desactivar el entorno virtual
echo '## deactivate venv ##'
deactivate

#regresar la version de python a la del sistema
echo '### reset the pyenv version to system python ###'
pyenv global system

