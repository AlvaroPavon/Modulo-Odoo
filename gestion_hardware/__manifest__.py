{
    'name': "gestion_hardware",
    'summary': "Gestión de Hardware, Tickets y Mantenimientos",
    'description': """
                    Proyecto creado como solución integral para la gestión de inventario de hardware, clientes, reparaciones y tickets.
                    ## Funcionalidades
                    Este módulo ofrece una solución completa para:
                    - 🖥️ **Inventario de Hardware:**  
                    Registrar y mantener un inventario detallado con información como nombre, descripción, modelo, precio, stock, marca e imagen.
                    - 👥 **Gestión de Clientes:**  
                    Administrar la información de clientes y sus interacciones.
                    - 🔧 **Reparaciones y Mantenimientos:**  
                    Registrar reparaciones realizadas en el hardware, actualizando automáticamente el stock y asociándolas a los tickets correspondientes.
                    - 🎫 **Tickets de Soporte:**  
                    Crear y administrar tickets que integran líneas de productos y reparaciones, con vistas personalizadas y la posibilidad de generar **PDF** para imprimirlos.
                    ## Beneficios
                    Ideal para empresas que necesiten:
                    - Centralizar la gestión de sus activos tecnológicos.
                    - Optimizar los procesos de atención al cliente y mantenimiento.
                    - Tener un control detallado y visual de su inventario y reparaciones.
                    ¡Una solución completa para mantener tu negocio en perfecto funcionamiento!
                """,
    'author': "Alvaro",
    'website': "https://www.alvaropavon.com",
    'category': 'Inventario',
    'version': '1.0',
    'license':'LGPL-3',
    'depends': ['base', 'product'],
    'data': [
        'security/ir.model.access.csv',            # Permisos de acceso
        'views/hardware_views.xml',                # Vistas para Hardware
        'views/ticket_views.xml',                  # Vistas para Ticket (incluye referencia a la vista de líneas)
        'views/mantenimiento_views.xml',           # Vistas para Mantenimiento (modelo custom)
        'views/cliente_views.xml',                 # Vistas extendidas para Clientes (res.partner)
        'views/menu_views.xml',                    # Menú de navegación
        'views/report_layout.xml',                 # Layout para reportes
        'reports/report_ticket.xml',               # Reporte PDF para Ticket
    ],
    'images': ['static/description/icon.png'],     # Icono de la aplicación
    'installable': True,
    'application': True,
}
