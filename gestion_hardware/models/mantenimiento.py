from odoo import models, fields

class Mantenimiento(models.Model):
    # Se renombra el modelo para que se considere custom (nombre que inicia con "x_")
    _name = 'x_gestion.mantenimiento'
    _description = 'Mantenimiento de Hardware'

    # Campos básicos
    name = fields.Char(string="Nombre del Mantenimiento", required=True)
    description = fields.Text(string="Descripción")
    cost = fields.Float(string="Costo", required=True)
    
    # Relación Many2many con Hardware
    hardware_ids = fields.Many2many('gestion.hardware', string="Hardware Asociado",
                                    help="Hardware al que se aplica el mantenimiento")
