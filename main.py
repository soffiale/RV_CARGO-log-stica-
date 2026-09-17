from flask import Flask, render_template, request, redirect, url_for
# Importamos desde la carpeta 'models'
from models.cliente import obtener_clientes, agregar_cliente
from models.conductor import obtener_conductores, agregar_conductor
from models.costos import obtener_costos, agregar_costo
from models.paquete import obtener_paquetes, agregar_paquete
from models.vehiculo import obtener_vehiculos, agregar_vehiculo
from models.viaje import obtener_viajes, agregar_viaje

# Importamos desde la carpeta 'controllers'
from controllers.cotizador import procesar_cotizacion

app = Flask(__name__)

@app.route('/')
def inicio():
    # Enviamos los datos de todas las entidades a la vista principal
    return render_template(
        'index.html',
        lista_clientes=obtener_clientes(),
        lista_conductores=obtener_conductores(),
        lista_costos=obtener_costos(),
        lista_paquetes=obtener_paquetes(),
        lista_vehiculos=obtener_vehiculos(),
        lista_viajes=obtener_viajes(),
        cotizacion=None
    )

# --- Ruta para el Cotizador Express ---

@app.route('/calcular_presupuesto', methods=['POST'])
def calcular_presupuesto():
    # Captura de datos del formulario de la pestaña Cotizador
    origen = request.form.get('origen')
    destino = request.form.get('destino')
    horas_espera = float(request.form.get('horas_espera', 0))
    paradas = int(request.form.get('paradas', 0))

    # Cálculo mediante el módulo externo
    resultado_cotizacion = procesar_cotizacion(origen, destino, horas_espera, paradas)

    # Renderiza nuevamente index.html incluyendo el resultado de la cotización
    return render_template(
        'index.html',
        lista_clientes=obtener_clientes(),
        lista_conductores=obtener_conductores(),
        lista_costos=obtener_costos(),
        lista_paquetes=obtener_paquetes(),
        lista_vehiculos=obtener_vehiculos(),
        lista_viajes=obtener_viajes(),
        cotizacion=resultado_cotizacion
    )

# --- Rutas para procesar la carga de cada entidad ---

@app.route('/nuevo_cliente', methods=['POST'])
def nuevo_cliente():
    agregar_cliente(
        request.form.get('nombre'),
        request.form.get('apellido'),
        request.form.get('dni'),
        request.form.get('edad'),
        request.form.get('palabra_clave'),
        request.form.get('direccion'),
        request.form.get('localidad')
    )
    return redirect(url_for('inicio'))

@app.route('/nuevo_conductor', methods=['POST'])
def nuevo_conductor():
    agregar_conductor(
        request.form.get('nombre'),
        request.form.get('apellido'),
        request.form.get('dni'),
        request.form.get('licencia'),
        request.form.get('telefono')
    )
    return redirect(url_for('inicio'))

@app.route('/nuevo_costo', methods=['POST'])
def nuevo_costo():
    agregar_costo(
        request.form.get('concepto'),
        request.form.get('costo_combustible'),
        request.form.get('peajes'),
        request.form.get('mantenimiento'),
    )
    return redirect(url_for('inicio'))

@app.route('/nuevo_paquete', methods=['POST'])
def nuevo_paquete():
    agregar_paquete(
        request.form.get('peso_kg'),
        request.form.get('alto_cm'),
        request.form.get('ancho_cm'),
        request.form.get('largo_cm'),
        request.form.get('descripcion')
    )
    return redirect(url_for('inicio'))

@app.route('/nuevo_vehiculo', methods=['POST'])
def nuevo_vehiculo():
    agregar_vehiculo(
        request.form.get('patente'),
        request.form.get('marca'),
        request.form.get('modelo'),
        request.form.get('capacidad_carga_kg'),
        request.form.get('tipo')
    )
    return redirect(url_for('inicio'))
if __name__ == '__main__':
    app.run(debug=True)