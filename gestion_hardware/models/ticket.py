from odoo import models, fields, api
from datetime import datetime

class Ticket(models.Model):
    _name = 'gestion.ticket'
    _description = 'Ticket de Soporte'

    # Campos básicos
    name = fields.Char(string="Título", required=True)
    description = fields.Text(string="Descripción")
    fecha_creacion = fields.Datetime(string="Fecha de Creación", default=fields.Datetime.now, required=True)
    fecha_ticket = fields.Date(string="Fecha del Ticket", required=True)
    
    estado = fields.Selection(
        [
            ('pendiente', 'Pendiente'),
            ('pagado', 'Pagado')
        ],
        string="Estado",
        default='pendiente'
    )
    
    # Relaciones con res.partner
    cliente_id = fields.Many2one('res.partner', string="Cliente", required=True)
    partner_ids = fields.Many2many('res.partner', string="Contactos Asociados",
                                   help="Contactos adicionales relacionados con este ticket")
    
    # Relación One2many: líneas de producto, para mas de un producto
    ticket_line_ids = fields.One2many('gestion.ticket.line', 'ticket_id', string="Productos")
    
    # Campo calculado: suma el total de las líneas + el costo de mantenimientos para obtener el precio total
    total_price = fields.Float(string="Precio Total", compute="_compute_total_price", store=True)
    
    # Mantenimientos realizados asociados al ticket
    maintenance_ids = fields.Many2many(
        'x_gestion.mantenimiento',
        string="Mantenimientos realizados",
        help="Mantenimientos realizados al hardware asociados a este ticket"
    )

    @api.depends('ticket_line_ids.line_total', 'maintenance_ids.cost')
    def _compute_total_price(self):
        for ticket in self:
            total_lines = sum(line.line_total for line in ticket.ticket_line_ids)
            total_maintenance = sum(m.cost for m in ticket.maintenance_ids)
            ticket.total_price = total_lines + total_maintenance
            
    pagado = fields.Html(string="Pagado", compute="_compute_estado_icon", store=False)

    @api.depends('estado')
    def _compute_estado_icon(self):
        for record in self:
            if record.estado == 'pagado':
                record.pagado = '<span style="color:green; font-size:16px;">&#x2713;</span>'
            else:
                record.pagado = '<span style="color:red; font-size:16px;">&#x2717;</span>'

    def toggle_estado(self):
        for record in self:
            record.estado = 'pagado' if record.estado == 'pendiente' else 'pendiente'

    def action_print_ticket(self):
        self.ensure_one()
        return self.env.ref('gestion_hardware.action_report_ticket').report_action(self)
