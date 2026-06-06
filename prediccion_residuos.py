"""
Módulo Independiente: Modelo Predictivo de Generación de Residuos
Basado en Regresión Lineal Múltiple con Estrategia de Valorización (Reciclaje)
"""

import streamlit as st
import pandas as pd

# ============================================================================
# CONFIGURACIÓN DE PÁGINA 
# ============================================================================
st.set_page_config(
    page_title="Predicción de Residuos - CDMX 2026",
    page_icon="♻️",
    layout="wide"
)

# ============================================================================
# LÓGICA DEL MODELO PREDICTIVO (HÍBRIDO ESTADÍSTICO)
# ============================================================================
def calcular_tonelaje_predicho(aforo, flotante, duracion, indice_comercio):
    """
    Simula la regresión matemática basándose en los coeficientes históricos documentados.
    """
    beta_0 = 2500 
    
    factor_duracion_interno = min(duracion / 4, 1.0) 
    coef_aforo = 0.20 + (0.80 * factor_duracion_interno) 
    basura_interna = aforo * coef_aforo
    
    coef_flotante = 1.06
    basura_flotante = flotante * coef_flotante
    
    basura_comercio = indice_comercio * 150
    
    total_kg = beta_0 + basura_interna + basura_flotante + basura_comercio
    toneladas_totales = total_kg / 1000
    
    return toneladas_totales, coef_aforo

# ============================================================================
# INTERFAZ DE USUARIO
# ============================================================================
def main():
    st.title("📈 Modelo Predictivo de Residuos Sólidos Urbanos (RSU)")
    st.markdown("""
    Esta herramienta analítica estima la generación de basura en megaeventos 
    utilizando variables demográficas y formula estrategias de **Gobernanza Fiscal Preventiva y Economía Circular**.
    """)
    st.markdown("---")
    
    col1, col2 = st.columns([1, 1.2])
    
    with col1:
        st.subheader("⚙️ Variables de Generación")
        
        aforo = st.number_input(
            "X₁ - Aforo Oficial Efectivo (Personas)",
            min_value=0, max_value=150000, value=83000, step=1000
        )
        
        flotante = st.number_input(
            "X₂ - Población Flotante / Fan Zones (Personas)",
            min_value=0, max_value=200000, value=45000, step=1000
        )
        
        duracion = st.slider(
            "X₃ - Duración del Evento y Pre-concentración (Horas)",
            min_value=2.0, max_value=12.0, value=6.0, step=0.5
        )
        
        indice_comercio = st.slider(
            "X₄ - Índice de Comercio Informal (1 - 100)",
            min_value=0, max_value=100, value=75
        )
        
        st.markdown("---")
        st.subheader("♻️ Estrategia de Economía Circular")
        st.markdown("Define la eficiencia del operativo de separación y reciclaje durante el evento.")
        
        tasa_recuperacion = st.slider(
            "Porcentaje del total rescatado para reciclaje (%)",
            min_value=0, max_value=100, value=30,
            help="Del 100% de la basura generada, ¿cuánto lograremos separar antes de que llegue al camión de basura?"
        )
        
        # Constantes de mercado
        costo_mitigacion_tonelada = 4000.00 
        precio_aluminio_ton = 22000.00
        precio_carton_ton = 1500.00
        precio_pet_ton = 5000.00 # Nuevo valor agregado para el PET
        
    with col2:
        st.subheader("📊 Resultados de la Inferencia y Valorización")
        
        # 1. Ejecutar modelo base
        toneladas, coef_real = calcular_tonelaje_predicho(aforo, flotante, duracion, indice_comercio)
        
        # 2. Cálculos de Economía Circular
        toneladas_recuperadas = toneladas * (tasa_recuperacion / 100)
        toneladas_a_disposicion = toneladas - toneladas_recuperadas # La basura que SÍ se va al relleno sanitario
        
        # Distribución de volumen recuperado: 20% Aluminio, 60% Cartón, 20% PET
        toneladas_aluminio = toneladas_recuperadas * 0.20
        toneladas_carton = toneladas_recuperadas * 0.60
        toneladas_pet = toneladas_recuperadas * 0.20
        
        ingreso_aluminio = toneladas_aluminio * precio_aluminio_ton
        ingreso_carton = toneladas_carton * precio_carton_ton
        ingreso_pet = toneladas_pet * precio_pet_ton
        
        ingresos_totales = ingreso_aluminio + ingreso_carton + ingreso_pet
        
        # Costo logístico original (Si no hiciéramos nada de reciclaje)
        costo_sin_reciclar = toneladas * costo_mitigacion_tonelada
        
        # 3. Cálculos de Gobernanza Fiscal Ajustada
        costo_operativo_bruto = toneladas_a_disposicion * costo_mitigacion_tonelada
        balance_financiero_final = costo_operativo_bruto - ingresos_totales
        impuesto_pigouviano = (balance_financiero_final / aforo) if (aforo > 0 and balance_financiero_final > 0) else 0
            
        # --- VISUALIZACIÓN ---
        # Fila 1: Métricas base y costo original
        m1, m2, m3 = st.columns(3)
        m1.metric(label="Generación Bruta (Y)", value=f"{toneladas:,.1f} Ton", delta="Volumen total")
        m2.metric(label="Desecho Real a Relleno", value=f"{toneladas_a_disposicion:,.1f} Ton", delta=f"-{toneladas_recuperadas:,.1f} Ton recuperadas", delta_color="normal")
        m3.metric(label="Costo SIN Reciclar", value=f"${costo_sin_reciclar:,.2f}", delta="Gasto logístico inicial", delta_color="inverse")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Fila 2: Tarjeta HTML destacada para los Ingresos + Letras chiquitas
        st.markdown(f"""
        <div style="background-color: #f0fdf4; padding: 25px; border-radius: 12px; text-align: center; border: 2px solid #22c55e; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
            <h4 style="color: #166534; margin-bottom: 0px; font-weight: 600;">💰 Ingresos por Economía Circular</h4>
            <h1 style="color: #15803d; font-size: 3.5rem; margin-top: 10px; margin-bottom: 10px;">${ingresos_totales:,.2f} MXN</h1>
            <p style="color: #166534; font-size: 1.1rem; margin-bottom: 0px;">Valorización de Aluminio, Cartón y PET</p>
        </div>
        <p style="text-align: center; font-size: 0.85rem; color: #6b7280; margin-top: 8px;">
            <i>* Se reciclaron exitosamente un total de <b>{toneladas_recuperadas:,.1f} toneladas</b> de residuos sólidos.</i>
        </p>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Desglose visual rápido
        st.markdown("**Desglose de Materiales Recuperados y Proyección de Ingresos:**")
        df_reciclaje = pd.DataFrame({
            "Material": ["Aluminio (Latas)", "Cartón/Papel", "PET (Botellas plásticas)", "Total Ingresos"],
            "Toneladas Capturadas": [toneladas_aluminio, toneladas_carton, toneladas_pet, toneladas_aluminio + toneladas_carton + toneladas_pet],
            "Ingreso Estimado (MXN)": [ingreso_aluminio, ingreso_carton, ingreso_pet, ingreso_aluminio + ingreso_carton + ingreso_pet],
        })
        
        st.dataframe(
            df_reciclaje.style.format({
                "Toneladas Capturadas": "{:,.2f}",
                "Ingreso Estimado (MXN)": "${:,.2f}"
            }),
            use_container_width=True,
            hide_index=True
        )
if __name__ == "__main__":
    main()