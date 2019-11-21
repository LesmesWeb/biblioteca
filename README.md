# django-learn

Instalaciones 
1. En Windows Añadir siempre el Python Path, al momento de instalar (https://www.python.org/downloads/windows/)
2. https://www.djangoproject.com/download/ #Revisar la LTS
3. cmd --> pip install virtualenv #Entorno virtual en Windows
4. virtualenv django_2_0
5. pip install -r requeriments.txt
5. cd django_2_0/Scripts
6. activate / deactivate /source activate #en visual code es .\activate 

Visual Code
(Ctrl+ Shift + p) #se crear una carpeta .vscode
*Visual Code --> View --> Command Palette --> Python: select interpretter -->python3
*Visual Code --> View --> Command Palette --> Select Default Shell --> bash github
*Para habilitar la ejecución de Script en visualCode escribir en la consola:
Set-ExecutionPolicy Unrestricted

Crear proyecto y App en Django
1. django-admin startproject biblioteca
2. cd biblioteca
2. mkdir apps
4. cd apps
5. django-admin startapp libro
6. 'apps.libro', #registramos el app en settings.py  INSTALLED_APPS
7. Añadir __init__py en la carpeta de apss
Notas:
**manage.py define cuales van a ser las configuraciones de nuestro proyecto
**__init__.py Es necesario que este creado este archivo para que reconozca la carpeta como parte del proyecto
*Settings -- Debug #tener presente que esta linea permite mostrar los errores no usar en producción

GitHub
git config --global user.email "@hotmail.com"
git config --global user.name "Dev-Lesmes"
git clone https://github.com/Dev-Lesmes/biblioteca.git
git add -A
git push origin master

PostgreSQL
psql -U postgresql -d biblioteca
\d #listo las tablas
