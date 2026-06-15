import streamlit as st

# Título y configuración
st.set_page_config(page_title="Simulador Cashea Pro", layout="centered")
st.title("💳 Sistema de Registro Cashea")

# Usamos 'session_state' para recordar si el usuario ya se registró
if 'registrado' not in st.session_state:
    st.session_state.registrado = False

if not st.session_state.registrado:
    # --- PANTALLA DE REGISTRO ---
    st.subheader("Registro Inicial")
    email = st.text_input("Correo electrónico")
    password = st.text_input("Contraseña", type="password")
    fecha_nac = st.date_input("Fecha de nacimiento")
    
    cedula = st.file_uploader("Sube tu copia de cédula (PDF/Imagen)", type=['png', 'jpg', 'pdf'])
    rif = st.file_uploader("Sube tu RIF digital", type=['png', 'jpg', 'pdf'])
    foto = st.camera_input("Tómate una foto frontal")

    if st.button("Enviar para verificación"):
        if email and cedula and rif and foto:
            st.session_state.registrado = True
            st.success("¡Registro exitoso! Ahora puedes acceder al simulador.")
            st.rerun() # Recarga la página para mostrar el simulador
        else:
            st.error("Por favor, completa todos los campos y carga tus documentos.")
else:
    # --- PANTALLA DEL SIMULADOR (Solo visible si registrado = True) ---
    st.success("Acceso concedido.")
    st.title("Simulador de Compras Cashea")
    
    # Aquí pegas el código que ya tenías funcional:
    monto = st.number_input("Monto total del producto ($):", min_value=0.0, value=100.0)
    nivel = st.slider("Selecciona tu Nivel Cashea:", 1, 3)
    
    # ... (el resto de tus cálculos aquí) ...
    
    if st.button("Cerrar sesión"):
        st.session_state.registrado = False
        st.rerun()