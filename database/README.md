# Base de Datos EVIA

## Requisitos
- XAMPP / MySQL 5.7 o superior

## Instalación Rápida

### Opción 1: Usando phpMyAdmin
1. Abre phpMyAdmin: http://localhost/phpmyadmin
2. Ve a la pestaña "Importar"
3. Selecciona `schema.sql` → Ejecutar
4. Luego importa `data.sql` → Ejecutar

### Opción 2: Usando línea de comandos
```bash
mysql -u root -p < database/schema.sql
mysql -u root -p < database/data.sql