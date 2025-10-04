import streamlit as st

# Configuración general
st.set_page_config(
    page_title="Portal de IA Generativa Servicios Generales",
    page_icon="🏥",
    layout="wide"
)

# Encabezado con logo y título
col1, col2 = st.columns([1,5])
with col1:
    st.image("logo.png", width=80)  # coloca aquí tu logo en la carpeta del proyecto
with col2:
    st.title("Portal de IA Generativa Servicios Generales")
    st.markdown("### Herramientas de apoyo para la gestión predictiva, documental y estratégica")

st.write("---")

# Navegación con estilo profesional
st.markdown("## 📌 Selecciona la aplicación que quieras abrir:")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("### 🏗 Gemini Assist")
    st.write("Mantenimiento predictivo y priorización de intervenciones.")
    st.link_button("Abrir", "https://gemini-assist-app-5j6m9sqqzjzycxmiprla2u.streamlit.app/")

with col2:
    st.markdown("### 📑 SmartDocs GPT")
    st.write("Automatización documental y validación normativa.")
    st.link_button("Abrir", "https://smartdocsgpt-ctkktu6gynceqzwtyz6z7n.streamlit.app/")

with col3:
    st.markdown("### 🤝 GenAI-Prove")
    st.write("Contratación estratégica y valoración de ofertas.")
    st.link_button("Abrir", "https://genai-prove-web-fayvacbmbzevljbjappyo5o.streamlit.app/")

with col4:
    st.markdown("### ⚖️ LegisIA Sanidad EU")
    st.write("Asesoramiento normativo y jurídico en IA y Sanidad (UE).")
    st.link_button("Abrir", "https://chatgpt.com/g/g-68d56223e0a48191862830df0aa2aadd-legisia-sanidad-eu")

st.write("---")

# Otros recursos
st.markdown("## 📊 Otros recursos y dashboards")
col5, col6 = st.columns(2)

with col5:
    st.markdown("### 🏥 Portal Normativa Hospitalaria")
    st.link_button("Abrir", "https://ejemplo-normativa.streamlit.app/")

    st.markdown("### 🧾 Cuadro de Mando RRHH")
    st.link_button("Abrir", "https://ejemplo-rrhh.streamlit.app/")

with col6:
    st.markdown("### ⚙️ Panel de Mantenimiento")
    st.link_button("Abrir", "https://ejemplo-mantenimiento.streamlit.app/")

    st.markdown("### 🌍 SmartGenAI – Información General")
    st.link_button("Abrir", "https://ejemplo-info.streamlit.app/")
