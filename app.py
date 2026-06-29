olución de ventasimport streamlit as st
import pandas as pd
# Título de la aplicación
st.title("Grafica de series de tiempo")
entrada = st.text_input("Ingrese la serie, separada por comas:", value = "10,15,18,26,31")
entrada2 = entrada.split(",")
serie =[float(i) for i in entrada2]
# --- OPCIÓN 1: Gráfica simple con tu lista original ---
serie = [10, 15, 18, 26, 31,48]
st.line_chart(serie)
