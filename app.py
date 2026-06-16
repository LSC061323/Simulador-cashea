import streamlit as st
from supabase import create_client

# 1. Configuración de conexión (Tu código actual)
@st.cache_resource
def init_connection():
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    return create_client(url, key)

supabase = init_connection()

# 2. Inicializar el estado de sesión (La memoria de la app)
if 'registrado' not in st.session_state:
    st.session_state.registrado = False
if 'logueado' not in st.session_state:
    st.session_state.logueado = False

st.title("💳 Sistema de Registro Cashea")

# 3. Flujo de navegación
if st.session_state.logueado:
    # --- PÁGINA PRINCIPAL (Ya dentro) ---
    st.success("¡Bienvenido al sistema!")
    if st.button("Cerrar sesión"):
        st.session_state.logueado = False
        st.rerun()

elif st.session_state.registrado:
    # --- PÁGINA DE ACCESO (Solo usuario y clave) ---
    st.subheader("Iniciar Sesión")
    user = st.text_input("Correo")
    password = st.text_input("Contraseña", type="password")
    if st.button("Entrar"):
        # AQUÍ: Agregar lógica para verificar en Supabase que el usuario existe
        st.session_state.logueado = True
        st.rerun()

else:
    # --- PÁGINA DE REGISTRO INICIAL (Formulario completo) ---
    st.subheader("Registro Inicial")
    with st.form("registro_form"):
        # AQUÍ: Pon todos tus campos actuales (cédula, foto, etc.)
        email = st.text_input("Correo electrónico")
        # ... resto de tus campos ...
        submit = st.form_submit_button("Registrarse")
        
        if submit:
            # AQUÍ: Agregar lógica para insertar en Supabase
            st.session_state.registrado = True # Marcamos que ya existe
            st.success("¡Registro exitoso! Ya puedes iniciar sesión.")
            st.rerun()