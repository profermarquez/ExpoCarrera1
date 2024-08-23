# crear entorno virtual
virtualenv env
/env/Script/activate.bat
# Dependencias
pip install streamlit pandas
# Ejecución en el RAIZ (en command prompt)
streamlit run cuestionario1.py
streamlit run cuestionario2.py
streamlit run dc1.py
streamlit run dc2.py
# cambiar puerto
streamlit run cuestionario1.py --server.port 8080  
streamlit run cuestionario2.py --server.port 8088  
# Detener en servicio con CTRL+c
# Para generar 500 registros
py generar_cuestionario1.py
py generar_cuestionario2.py

# Comando para solucionar Error powershell FullyQualifiedErrorId : UnauthorizedAccess
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned

