import streamlit as st

# Configuración general
st.set_page_config(page_title="Portal IA Sanitaria", page_icon="🏥", layout="wide")

# Título y bienvenida
st.title("🏥 Portal de Aplicaciones IA Sanitaria")
st.markdown("""
Bienvenido al **portal unificado de herramientas de IA** para el sector sanitario.  
Aquí puedes acceder directamente a cada aplicación desplegada en **Streamlit Cloud**.
""")

# Menú lateral
st.sidebar.title("📌 Navegación")
opcion = st.sidebar.radio("Selecciona una aplicación:", [
    "🏗 Gemini Assist (Mantenimiento Predictivo)",
    "📑 SmartDocs GPT (Documentación Normativa)",
    "🤝 GenAI-Prove (Contratación Estratégica)",
    "📊 Dashboards y Otros Recursos"
])

# Secciones
if opcion.startswith("🏗 Gemini Assist"):
    st.subheader("🏗 Gemini Assist")
    st.markdown("🔗 [Abrir aplicación Gemini Assist](https://gemini-assist-app-5j6m9sqqzjzycxmiprla2u.streamlit.app/)")

elif opcion.startswith("📑 SmartDocs GPT"):
    st.subheader("📑 SmartDocs GPT")
    st.markdown("🔗 [Abrir aplicación SmartDocs GPT](https://smartdocsgpt-ctkktu6gynceqzwtyz6z7n.streamlit.app/)")

elif opcion.startswith("🤝 GenAI-Prove"):
    st.subheader("🤝 GenAI-Prove")
    st.markdown("🔗 [Abrir aplicación GenAI-Prove](https://genai-prove-web-fayvacbmbzevljbjappyo5o.streamlit.app/)")

elif opcion.startswith("📊 Dashboards y Otros Recursos"):
    st.subheader("📊 Otros proyectos disponibles")
    st.markdown("- 🏥 [Portal Normativa Hospitalaria](https://ejemplo-normativa.streamlit.app/)")
    st.markdown("- 🧾 [Cuadro de Mando RRHH Hospitalarios](https://ejemplo-rrhh.streamlit.app/)")
    st.markdown("- ⚙️ [Panel de Mantenimiento de Instalaciones](https://ejemplo-mantenimiento.streamlit.app/)")
    st.markdown("- 🌍 [SmartGenAI – Información General](https://ejemplo-info.streamlit.app/)")
