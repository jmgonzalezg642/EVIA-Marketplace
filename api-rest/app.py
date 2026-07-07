# =============================================================================
# API REST para EVIA - Conecta la app móvil con la base de datos
# Archivo: api-rest/app.py
# =============================================================================

from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector
import jwt
import datetime
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)  # Permitir peticiones desde la app móvil

# Configuración
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'evia-secret-key-2024')

# =============================================================================
# CONEXIÓN A BASE DE DATOS
# =============================================================================

def get_db_connection():
    """Obtiene una conexión a la base de datos MySQL"""
    try:
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST', 'localhost'),
            user=os.getenv('DB_USER', 'root'),
            password=os.getenv('DB_PASSWORD', ''),
            database=os.getenv('DB_NAME', 'bd_evia')
        )
        return connection
    except mysql.connector.Error as e:
        print(f"❌ Error al conectar a la BD: {e}")
        return None

# =============================================================================
# DECORADOR DE AUTENTICACIÓN
# =============================================================================

def token_required(f):
    """Decorador para proteger rutas con JWT"""
    def decorator(*args, **kwargs):
        token = request.headers.get('x-api-key')
        
        if not token:
            return jsonify({
                'ok': False,
                'message': 'Token no proporcionado'
            }), 401
        
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            request.user = data
        except jwt.ExpiredSignatureError:
            return jsonify({
                'ok': False,
                'message': 'Token expirado'
            }), 401
        except jwt.InvalidTokenError:
            return jsonify({
                'ok': False,
                'message': 'Token inválido'
            }), 401
        
        return f(*args, **kwargs)
    
    decorator.__name__ = f.__name__
    return decorator

# =============================================================================
# RUTAS DE LA API
# =============================================================================

@app.route('/api/v1/health', methods=['GET'])
def health():
    """Verifica que la API esté funcionando"""
    return jsonify({
        'ok': True,
        'message': 'API EVIA funcionando correctamente',
        'timestamp': datetime.datetime.now().isoformat()
    })

# -----------------------------------------------------------------------------
# AUTENTICACIÓN
# -----------------------------------------------------------------------------

@app.route('/api/v1/auth/login', methods=['POST'])
def login():
    """Autentica un usuario y devuelve un token JWT"""
    try:
        data = request.get_json()
        correo = data.get('email')
        
        if not correo:
            return jsonify({
                'ok': False,
                'message': 'Correo electrónico requerido'
            }), 400
        
        connection = get_db_connection()
        if not connection:
            return jsonify({
                'ok': False,
                'message': 'Error de conexión a la base de datos'
            }), 500
        
        cursor = connection.cursor(dictionary=True)
        cursor.execute(
            "SELECT id_usuario, nombre_usuario, correo_usuario, rol_usuario, ciudad_usuario, telefono_usuario "
            "FROM usuarios WHERE correo_usuario = %s",
            (correo,)
        )
        user = cursor.fetchone()
        cursor.close()
        connection.close()
        
        if not user:
            return jsonify({
                'ok': False,
                'message': 'Usuario no encontrado'
            }), 401
        
        # Generar token JWT
        token = jwt.encode({
            'id': user['id_usuario'],
            'email': user['correo_usuario'],
            'name': user['nombre_usuario'],
            'role': user['rol_usuario'],
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
        }, app.config['SECRET_KEY'], algorithm='HS256')
        
        return jsonify({
            'ok': True,
            'data': {
                'message': 'Login exitoso',
                'apiKey': token,
                'user': {
                    'id': user['id_usuario'],
                    'name': user['nombre_usuario'],
                    'email': user['correo_usuario'],
                    'role': user['rol_usuario'],
                    'city': user['ciudad_usuario'],
                    'phone': user['telefono_usuario']
                }
            }
        })
        
    except Exception as e:
        return jsonify({
            'ok': False,
            'message': f'Error en el servidor: {str(e)}'
        }), 500

# -----------------------------------------------------------------------------
# PRODUCTOS (Vehículos)
# -----------------------------------------------------------------------------

@app.route('/api/v1/products', methods=['GET'])
@token_required
def get_products():
    """Obtiene todos los vehículos disponibles"""
    try:
        connection = get_db_connection()
        if not connection:
            return jsonify({
                'ok': False,
                'message': 'Error de conexión a la base de datos'
            }), 500
        
        cursor = connection.cursor(dictionary=True)
        cursor.execute("""
            SELECT 
                v.id_vehiculo as id,
                v.tipo_vehiculo,
                v.marca,
                v.modelo,
                v.precio,
                v.autonomia_km,
                v.capacidad_bateria_kwh,
                v.peso_kg,
                v.velocidad_maxima,
                v.tipo_conector,
                v.garantia_meses,
                v.año,
                v.es_nuevo,
                v.estado_vehiculo,
                u.nombre_usuario as vendedor
            FROM vehiculos v
            JOIN usuarios u ON v.id_vendedor = u.id_usuario
            WHERE v.estado_vehiculo = 'DISPONIBLE'
            ORDER BY v.id_vehiculo DESC
        """)
        
        products = cursor.fetchall()
        cursor.close()
        connection.close()
        
        return jsonify({
            'ok': True,
            'data': products
        })
        
    except Exception as e:
        return jsonify({
            'ok': False,
            'message': f'Error al obtener productos: {str(e)}'
        }), 500

# -----------------------------------------------------------------------------
# PRODUCTO POR ID
# -----------------------------------------------------------------------------

@app.route('/api/v1/products/<int:product_id>', methods=['GET'])
@token_required
def get_product_by_id(product_id):
    """Obtiene un vehículo por su ID"""
    try:
        connection = get_db_connection()
        if not connection:
            return jsonify({
                'ok': False,
                'message': 'Error de conexión a la base de datos'
            }), 500
        
        cursor = connection.cursor(dictionary=True)
        cursor.execute("""
            SELECT 
                v.id_vehiculo as id,
                v.tipo_vehiculo,
                v.marca,
                v.modelo,
                v.precio,
                v.autonomia_km,
                v.capacidad_bateria_kwh,
                v.peso_kg,
                v.velocidad_maxima,
                v.tipo_conector,
                v.garantia_meses,
                v.año,
                v.es_nuevo,
                v.estado_vehiculo,
                u.nombre_usuario as vendedor
            FROM vehiculos v
            JOIN usuarios u ON v.id_vendedor = u.id_usuario
            WHERE v.id_vehiculo = %s
        """, (product_id,))
        
        product = cursor.fetchone()
        cursor.close()
        connection.close()
        
        if not product:
            return jsonify({
                'ok': False,
                'message': 'Producto no encontrado'
            }), 404
        
        return jsonify({
            'ok': True,
            'data': product
        })
        
    except Exception as e:
        return jsonify({
            'ok': False,
            'message': f'Error al obtener producto: {str(e)}'
        }), 500

# =============================================================================
# INICIAR SERVIDOR
# =============================================================================

if __name__ == '__main__':
    print("=" * 55)
    print("     ⚡ API EVIA - Servicio para App Móvil")
    print("=" * 55)
    print(f"   📡 Servidor corriendo en: http://localhost:5000")
    print(f"   📊 Base de datos: bd_evia")
    print("=" * 55)
    app.run(debug=True, host='0.0.0.0', port=5000)