DROP DATABASE IF EXISTS rv_cargo;
CREATE DATABASE rv_cargo;
USE rv_cargo;

CREATE TABLE clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    dni VARCHAR(20) UNIQUE,
    telefono VARCHAR(50),
);

CREATE TABLE conductores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    dni VARCHAR(20) UNIQUE,
    licencia VARCHAR(50) NOT NULL,
    telefono VARCHAR(50)
);

CREATE TABLE costos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    concepto VARCHAR(100) NOT NULL,
    costo_combustible DECIMAL(10,2) DEFAULT 165.00,
    mantenimiento DECIMAL(10,2) DEFAULT 45.00
);

CREATE TABLE presupuestos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    origen VARCHAR(255) NOT NULL,
    destino VARCHAR(255) NOT NULL,
    distancia_km DECIMAL(10,2) NOT NULL,
    monto_total DECIMAL(10,2) NOT NULL,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE paquetes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    descripcion VARCHAR(255) NOT NULL,
    peso_kg DECIMAL(10,2),
    volumen_m3 DECIMAL(10,2),
    presupuesto_id INT,
    FOREIGN KEY (presupuesto_id) REFERENCES presupuestos(id) ON DELETE SET NULL
);

CREATE TABLE vehiculos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    patente VARCHAR(20) UNIQUE NOT NULL,
    modelo VARCHAR(100) NOT NULL,
    capacidad_carga DECIMAL(10,2),
    estado VARCHAR(50) DEFAULT 'Disponible'
);