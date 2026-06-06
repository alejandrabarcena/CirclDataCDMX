# ♻️ CirclData CDMX

Sistema inteligente de gestión de residuos para eventos masivos, diseñado para apoyar la sostenibilidad urbana durante el Mundial FIFA 2026 en la Ciudad de México.

![CirclData CDMX](https://raw.githubusercontent.com/alejandrabarcena/CirclDataCDMX/refs/heads/main/CDMX%20Event%20Simulation.png)

---

## 🌎 Descripción

CirclData CDMX es una plataforma de análisis y monitoreo que permite estimar, visualizar y optimizar la generación de residuos en recintos con alta afluencia de personas.

El sistema busca apoyar la toma de decisiones mediante métricas de sustentabilidad, simulación de escenarios y recomendaciones para una gestión eficiente de residuos sólidos urbanos.

---

## 🚀 Funcionalidades

* Selección de sedes y recintos.
* Configuración de parámetros operativos del evento.
* Estimación de generación de residuos.
* Predicción de residuos por tipo.
* Cálculo de indicadores de sostenibilidad.
* Recomendación de distribución de contenedores.
* Visualización de métricas ambientales.
* Generación de reportes.
* API backend preparada para futuras integraciones.
* Escalabilidad para eventos deportivos, culturales y masivos.

---

## 📸 Capturas del Proyecto

### Dashboard Principal

![Dashboard Principal](https://raw.githubusercontent.com/alejandrabarcena/CirclDataCDMX/refs/heads/main/CDMX%20Event%20Simulation.png)

---

### Simulación de Eventos CDMX

![Simulación de Eventos](https://raw.githubusercontent.com/alejandrabarcena/CirclDataCDMX/refs/heads/main/CDMX%20Event%20Simulation%20%C2%B7%20Streamlit.png)

---

### Predicción de Residuos

![Predicción de Residuos](https://raw.githubusercontent.com/alejandrabarcena/CirclDataCDMX/refs/heads/main/Prediccion%20de%20Residuos%20-%20CDMX%202026%20%C2%B7%20Streamlit.png)

---

## 🏗 Arquitectura del Proyecto

```text
CirclDataCDMX
│
├── src/
│   ├── app/
│   ├── imports/
│   └── styles/
│
├── backend/
│   ├── main.py
│   └── requirements.txt
│
├── public/
├── package.json
├── vite.config.ts
└── README.md
```

---

## 🛠 Tecnologías

### Frontend

* React
* TypeScript
* Vite
* Tailwind CSS
* Motion
* Radix UI
* Recharts

### Backend

* Python
* FastAPI
* Uvicorn

### Herramientas

* Git
* GitHub
* VS Code
* GitHub Codespaces
* Figma
* Vercel
* Render

---

## ⚙️ Instalación

### Frontend

Instalar dependencias:

```bash
npm install
```

Iniciar entorno de desarrollo:

```bash
npm run dev
```

o utilizando pnpm:

```bash
pnpm install
pnpm dev
```

---

### Backend

Crear entorno virtual:

```bash
python -m venv venv
```

Activar entorno virtual:

Linux / Codespaces

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Ejecutar API:

```bash
python -m uvicorn main:app --reload --port 8000
```

---

## 📊 Caso de Uso

Durante eventos masivos como el Mundial FIFA 2026, miles de personas generan grandes cantidades de residuos sólidos.

CirclData CDMX permite:

* Anticipar la generación de residuos.
* Optimizar la ubicación de contenedores.
* Reducir acumulaciones de basura.
* Apoyar estrategias de economía circular.
* Generar métricas para autoridades y organizadores.
* Mejorar la sostenibilidad de eventos urbanos.

---

## 🎯 Objetivos

* Promover ciudades más limpias y sostenibles.
* Utilizar datos para la toma de decisiones.
* Facilitar la gestión de residuos en eventos masivos.
* Reducir impactos ambientales.
* Impulsar soluciones tecnológicas para la sustentabilidad urbana.

---

## 🔗 Enlaces

### Repositorio

https://github.com/alejandrabarcena/CirclDataCDMX

### Frontend

Pendiente de despliegue

### Backend API

Pendiente de despliegue

---

## 👥 Equipo

Proyecto desarrollado para Hackathon Conciencia IA.

### Integrantes

* Alejandra Bárcena — Frontend, UX/UI y documentación.
* Kevin Pavón — Desarrollo.
* Omar Bolaños— Desarrollo.

---

## 📄 Licencia

Proyecto desarrollado con fines educativos, de innovación cívica y prototipado tecnológico.
