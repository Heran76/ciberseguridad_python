# Repaso de Ciberseguridad y Hacking Ético con Python

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

Este repositorio es mi espacio personal para el repaso e investigación en ciberseguridad y hacking ético utilizando Python. Aquí documento mi progreso, mis notas y las herramientas que desarrollo mientras profundizo en técnicas ofensivas y defensivas.

## 📖 Descripción

En este espacio, exploro los fundamentos de la ciberseguridad y el hacking ético, y cómo aplicar Python para crear herramientas propias de análisis, explotación y defensa. A lo largo de los módulos, desarrollo scripts y programas que me permiten:

- Escanear redes y puertos.
- Realizar ataques de fuerza bruta.
- Analizar tráfico de red.
- Crear honeypots y sistemas de detección.
- Automatizar tareas de seguridad.
- Y mucho más.

Todo el contenido está enfocado en el **hacking ético**: el uso responsable de estas técnicas para mejorar la seguridad de sistemas y redes.

## 🎯 Temas de Estudio

- Fundamentos de redes y protocolos.
- Programación en Python aplicada a la seguridad.
- Escaneo de vulnerabilidades y enumeración.
- Explotación básica de sistemas.
- Técnicas de post-explotación.
- Defensa: monitorización, detección y respuesta.
- Buenas prácticas y ética profesional.

## 📋 Punto de Partida

- Conocimientos básicos de Python (variables, condicionales, bucles, funciones).
- Ganas de aprender y curiosidad por la seguridad informática.
- Un entorno Linux o macOS (o Windows con WSL) para las prácticas.
- Conexión a internet para descargar librerías y herramientas.

## 📂 Estructura del Repositorio

El repositorio está organizado en módulos. Cada módulo contiene teoría, ejemplos prácticos y ejercicios.

```bash
📁 01-introduccion
   ├── 01-que-es-hacking-etico.md
   ├── 02-configuracion-entorno.md
   └── ejercicios/

📁 02-python-para-seguridad
   ├── 01-sockets.md
   ├── 02-scapy.md
   ├── 03-requests-y-http.md
   └── ejercicios/

📁 03-escaneo-de-redes
   ├── 01-ping-sweeper.py
   ├── 02-port-scanner.py
   └── ejercicios/

📁 04-ataques-de-fuerza-bruta
   ├── 01-ssh-brute.py
   ├── 02-ftp-brute.py
   └── ejercicios/

📁 05-analisis-de-trafico
   ├── 01-sniffer.py
   ├── 02-analisis-pcap.py
   └── ejercicios/

📁 06-defensa
   ├── 01-honeypot.py
   ├── 02-detector-intrusiones.py
   └── ejercicios/

📁 07-proyecto-final
   └── instrucciones.md

📁 recursos
   ├── cheatsheet-python-seguridad.pdf
   └── enlaces-utiles.md
```

## 🛠️ Herramientas y librerías utilizadas

- Python 3.8+
- Scapy: Manipulación de paquetes de red.
- Requests: Cliente HTTP.
- Paramiko: SSH y SFTP.
- Socket: Comunicaciones de red.
- Threading: Multiprocesamiento.
- Pcapy / dpkt: Captura y análisis de paquetes.
- Nmap: Escaneo de puertos (integración con Python).
- Y más...

## 🚀 Cómo usar este repositorio

Clona el repositorio:

```bash
git clone https://github.com/tu_usuario/tu_repositorio.git
cd tu_repositorio
```

Crea un entorno virtual (opcional pero recomendado):

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

Instala las dependencias:

```bash
pip install -r requirements.txt
```

Explora los módulos en orden y ejecuta los ejemplos. Cada carpeta contiene su propio README con instrucciones específicas.

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

## ⚠️ Aviso legal

Todo el material de este repositorio tiene fines exclusivamente educativos. El hacking ético debe practicarse únicamente en sistemas propios o con autorización explícita. El mal uso de estas técnicas puede ser ilegal. No me responsabilizo del mal uso que se pueda dar a la información aquí proporcionada.

