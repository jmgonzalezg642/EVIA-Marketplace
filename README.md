# ⚡ EVIA - Marketplace de Vehículos Eléctricos

Sistema completo para la compra y venta de vehículos eléctricos.

## Estructura del Proyecto

EVIA-Marketplace/
├── backend-python/ # Sistema CLI en Python
│ ├── config/ # Conexión a BD
│ ├── controllers/ # Lógica de negocio
│ ├── models/ # Entidades (Carro, Motocicleta, etc.)
│ ├── patterns/ # Singleton, Factory, Facade
│ ├── repositories/ # Operaciones SQL
│ ├── views/ # Interfaz de usuario
│ ├── main.py # Punto de entrada
│ └── requirements.txt
│
├── database/ # Scripts SQL
│ ├── schema.sql # Estructura de la BD
│ ├── data.sql # Datos de ejemplo
│ └── README.md
│
└── README.md


## Requisitos

- Python 3.8+
- XAMPP (MySQL)

## Instalación Rápida

### 1. Clonar el repositorio
```bash
git clone https://github.com/tu-usuario/EVIA-Marketplace.git
cd EVIA-Marketplace