import streamlit as st

# Configuración de la página web
st.set_page_config(page_title="Simulador Cashea", page_icon="💳", layout="centered")

st.title("💳 Simulador de Compras Cashea")
st.write("Calcula tu pago inicial y tus cuotas quincenales según tu nivel de usuario.")

# Sección de entrada de datos (Interactivos)
st.sidebar.header("Configuración de la Compra")

monto_total = st.sidebar.number_input(
    "Monto total del producto ($):", 
    min_value=1.0, 
    value=100.0, 
    step=5.0
)

nivel_usuario = st.sidebar.slider(
    "Selecciona tu Nivel Cashea:", 
    min_value=1, 
    max_value=3, 
    value=1,
    help="El nivel determina el porcentaje del pago inicial."
)

# Lógica del modelo Cashea
if nivel_usuario == 1:
    porcentaje_inicial = 0.50
elif nivel_usuario == 2:
    porcentaje_inicial = 0.40
else:
    porcentaje_inicial = 0.30

monto_inicial = monto_total * porcentaje_inicial
monto_restante = monto_total - monto_inicial
monto_cuota = monto_restante / 3

# Mostrar los resultados estéticos en la pantalla principal
st.subheader("📊 Resumen del Financiamiento")

col1, col2 = st.columns(2)
with col1:
    st.metric(label="Pago Inicial (Hoy)", value=f"${monto_inicial:,.2f}", delta=f"{porcentaje_inicial*100:.0f}% inicial")
with col2:
    st.metric(label="Monto Financiado", value=f"${monto_restante:,.2f}")

st.markdown("---")
st.subheader("📅 Cronograma de Pagos Quincenales")
st.write("El saldo restante se divide en 3 cuotas iguales sin interés (cada 14 días):")

# Crear una tabla visual para el cronograma
cronograma_datos = [
    {"Cuota": "Cuota 1", "Plazo": "En 14 días", "Monto a Pagar": f"${monto_cuota:,.2f}"},
    {"Cuota": "Cuota 2", "Plazo": "En 28 días", "Monto a Pagar": f"${monto_cuota:,.2f}"},
    {"Cuota": "Cuota 3", "Plazo": "En 42 días", "Monto a Pagar": f"${monto_cuota:,.2f}"},
]

st.table(cronograma_datos)

st.info("💡 Consejo: Mantén tus pagos al día para aumentar tu nivel y reducir el porcentaje de tu pago inicial en futuras compras.")