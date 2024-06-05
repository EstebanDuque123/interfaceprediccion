import streamlit as st
import requests
import os
import socket

# Título de la aplicación
st.title("Predicción de Modalidad de Robo de Motos")

# Entradas del usuario
municipio = st.text_input("Municipio")
fecha_hecho = st.text_input("Fecha del Hecho (MM-DD)")

# Botón para realizar la predicción
if st.button("Predecir"):
    # Definimos los datos de entrada
    datos_entrada = {
        "MUNICIPIO": municipio,
        "FECHA_HECHO": fecha_hecho
    }
    print("Seabrio la interface")
    # Realizamos la solicitud al endpoint de FastAPI
    response = requests.post("https://predicci-n-de-modalidad-de-robo-de-motos1.onrender.com/predecir_modalidad_robo1/", json=datos_entrada)
    
    # Verificamos la respuesta
    if response.status_code == 200:
        resultado = response.json()
        st.success(f"Modalidad Predicha: {resultado['Modalidad_Predicha']}")
    else:
        st.error("Error en la predicción. Por favor, verifica los datos de entrada.")

# # Para ejecutar la aplicación Streamlit
if __name__ == "__main__":
     import os
     os.system("streamlit run app.py")
