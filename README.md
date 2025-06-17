# Sistema de Gestión de Tickets

Este es un sistema simple de gestión de tickets desarrollado en Python que permite:
- Generar nuevos tickets con un número único.

- Leer tickets existentes.

- Almacenar los tickets en archivos `.pkl` (serializados con `pickle`).

## 📋 Requisitos
- Python 3.8 o superior.

## 📂 Funcionalidades
- Generar un nuevo ticket:

- Solicita nombre, sector, asunto y mensaje.

- Genera un número de ticket aleatorio.

- Guarda los datos en un archivo .pkl.

- Leer un ticket existente:

- Pide el número de ticket.

- Muestra los detalles si existe.

## ⚠️ Notas
- Los tickets se guardan en archivos .pkl en el mismo directorio.

- No requiere base de datos externa (usa serialización con pickle).
