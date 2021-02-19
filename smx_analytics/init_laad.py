import subprocess
requirements = subprocess.Popen('pip install -r requirements.txt'.split(), stdout=subprocess.PIPE)
output, error = requirements.communicate()
print(output,error)
makemigrations = subprocess.Popen('python manage.py makemigrations'.split(), stdout=subprocess.PIPE)
output, error = makemigrations.communicate()
migrate = subprocess.Popen('python manage.py migrate'.split(), stdout=subprocess.PIPE)
output, error = migrate.communicate()

empresa = subprocess.Popen('python manage.py loaddata backup/backups_config/referenciaempresa-2020-10-30.yaml'.split(), stdout=subprocess.PIPE)
output, error = empresa.communicate()

planta = subprocess.Popen('python manage.py loaddata backup/backups_config/referenciaplanta-2020-10-30.yaml'.split(), stdout=subprocess.PIPE)
output, error = planta.communicate()

linea = subprocess.Popen('python manage.py loaddata backup/backups_config/referencialinea-2020-10-30.yaml'.split(), stdout=subprocess.PIPE)
output, error = linea.communicate()

maquina = subprocess.Popen('python manage.py loaddata backup/backups_config/referenciamaquina-2020-10-30.yaml'.split(), stdout=subprocess.PIPE)
output, error = empresa.communicate()



