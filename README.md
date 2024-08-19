# crear entorno virtual
virtualenv env
/env/Script/activate.bat
# Dependencias
pip install streamlit pandas
# Ejecución en el RAIZ (en command prompt)
streamlit run cuestionario1.py
# cambiar puerto
streamlit run cuestionario1.py --server.port 8080  
# Detener en servicio con CTRL+c