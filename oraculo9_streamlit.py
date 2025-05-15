import streamlit as st
from datetime import datetime

# ----------- MÓDULO ÉTICO SIMULADO ------------
class EticaSistema:
    def __init__(self):
        self.principios = {
            'vida_humana': 0.9,
            'privacidad': 0.7,
            'seguridad': 0.8,
            'libertad_expresion': 0.6,
            'cohesion_social': 0.75
        }

    def evaluar_conflicto(self, variables):
        score = 0
        for clave, valor in variables.items():
            score += self.principios.get(clave, 0.5) * valor
        return score

# ----------- MÓDULO DE CONTEXTO ----------------
class ContextoCiudadano:
    def __init__(self, situacion):
        self.situacion = situacion

    def analizar(self):
        situaciones = {
            "manifestacion": {
                'libertad_expresion': 0.9,
                'cohesion_social': 0.6,
                'seguridad': 0.7
            },
            "corte_energia": {
                'vida_humana': 0.8,
                'seguridad': 0.6
            },
            "vigilancia_festival": {
                'privacidad': 0.9,
                'seguridad': 0.8
            },
            "uso_drones": {
                'privacidad': 0.8,
                'seguridad': 0.85,
                'vida_humana': 0.5
            },
            "crisis_alimentos": {
                'vida_humana': 0.95,
                'cohesion_social': 0.8,
                'seguridad': 0.6
            }
        }
        return situaciones.get(self.situacion, {})

# ----------- MOTOR DE DECISIÓN ----------------
class Oraculo9:
    def __init__(self):
        self.etica = EticaSistema()
        self.registro = []

    def tomar_decision(self, contexto):
        factores = contexto.analizar()
        puntuacion = self.etica.evaluar_conflicto(factores)
        decision = "APROBADO" if puntuacion > 0.65 else "DENEGADO"
        self.registrar_decision(contexto.situacion, decision, puntuacion, factores)
        return decision, puntuacion, factores

    def registrar_decision(self, situacion, decision, score, factores):
        entrada = {
            'timestamp': datetime.now().isoformat(),
            'situacion': situacion,
            'decision': decision,
            'puntaje_etico': round(score, 3),
            'factores': factores
        }
        self.registro.append(entrada)

# ----------- SISTEMA DE APRENDIZAJE FICTICIO ----------------
class RetroalimentacionCiudadana:
    def __init__(self, oraculo):
        self.oraculo = oraculo

    def aplicar_feedback(self, principio, nuevo_peso):
        if principio in self.oraculo.etica.principios:
            self.oraculo.etica.principios[principio] = nuevo_peso
            return True
        else:
            return False

# ----------- STREAMLIT APP ----------------
def main():
    st.title("Simulación Ética - ORÁCULO-9")

    oraculo = Oraculo9()
    feedback = RetroalimentacionCiudadana(oraculo)

    situacion = st.selectbox("Seleccione una situación:", [
        "manifestacion", "corte_energia", "vigilancia_festival",
        "uso_drones", "crisis_alimentos"
    ])

    if st.button("Evaluar Decisión"):
        contexto = ContextoCiudadano(situacion)
        decision, score, factores = oraculo.tomar_decision(contexto)
        st.write(f"**Situación:** {situacion}")
        st.write(f"**Decisión:** {decision}")
        st.write(f"**Puntaje Ético:** {round(score,3)}")
        st.write(f"**Factores:** {factores}")

    st.markdown("---")
    st.header("Ajustar Principio Ético")

    principios = list(oraculo.etica.principios.keys())
    principio_sel = st.selectbox("Seleccione principio:", principios)
    nuevo_valor = st.slider("Nuevo valor (peso)", 0.0, 1.0, oraculo.etica.principios[principio_sel], 0.01)

    if st.button("Aplicar Feedback"):
        success = feedback.aplicar_feedback(principio_sel, nuevo_valor)
        if success:
            st.success(f"Se ajustó '{principio_sel}' a {nuevo_valor}")
        else:
            st.error("Principio no encontrado.")

    st.markdown("---")
    st.subheader("Pesos actuales de principios éticos")
    for p, v in oraculo.etica.principios.items():
        st.write(f"- **{p}**: {v}")

if __name__ == "__main__":
    main()
