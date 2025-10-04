import streamlit as st

# Configuración
st.set_page_config(
    page_title="Portal de IA Generativa Servicios Generales",
    page_icon="🏥",
    layout="wide"
)

# Cargar usuarios desde secrets
USERS = st.secrets["USERS"]

# Estado inicial
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user = None
    st.session_state.role = None

# Si NO ha iniciado sesión
if not st.session_state.logged_in:
    st.sidebar.title("🔒 Acceso restringido")
    username = st.sidebar.text_input("Usuario:")
    password = st.sidebar.text_input("Contraseña:", type="password")

    if st.sidebar.button("Iniciar sesión"):
        if username in USERS and USERS[username]["password"] == password:
            st.session_state.logged_in = True
            st.session_state.user = username
            st.session_state.role = USERS[username]["role"]
            st.sidebar.success(f"Bienvenido {username} 👋")
            st.rerun()
        else:
            st.error("Usuario o contraseña incorrectos ❌")
            st.stop()
    else:
        st.stop()

# ------------------------------
# Si la autenticación fue correcta
# ------------------------------

# Botón de logout
if st.sidebar.button("🚪 Cerrar sesión"):
    st.session_state.logged_in = False
    st.session_state.user = None
    st.session_state.role = None
    st.rerun()

# Encabezado
col1, col2 = st.columns([1,5])
with col1:
    st.image("logo.png", width=80)
with col2:
    st.title("Portal de IA Generativa Servicios Generales")
    st.markdown(f"### Bienvenido **{st.session_state.user}** 👋 (Rol: **{st.session_state.role.upper()}**)")

st.write("---")

# Navegación principal
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

# Otros recursos según rol
if st.session_state.role == "admin":
    st.success("🔐 Acceso completo (Admin)")
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

else:
    st.warning("🔑 Acceso limitado (Usuario)")
    st.info("Contacta con el administrador para permisos adicionales.")
