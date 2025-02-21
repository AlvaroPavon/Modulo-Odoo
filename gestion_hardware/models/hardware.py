from odoo import models, fields, api

class Hardware(models.Model):
    _name = 'gestion.hardware'
    _description = 'Gestión de Hardware'

    name = fields.Char(string="Nombre del Hardware", required=True)
    description = fields.Text(string="Descripción")
    modelo = fields.Char(string="Modelo")
    precio = fields.Integer(string="Precio", required=True)
    marca = fields.Char(string="Marca")
    imagen = fields.Binary(string="Imagen")
    stock = fields.Integer(string="Stock", default=0, help="Cantidad disponible")
    user_id = fields.Many2one('res.users', string="Responsable", help="Usuario responsable del hardware")

    # Campo computado: cuenta los tickets asociados a través de ticket_line
    ticket_count = fields.Integer(string="Cantidad de Tickets", compute="_compute_ticket_count", store=False)

    def _compute_ticket_count(self):
        for hw in self:
            ticket_lines = self.env['gestion.ticket.line'].search([('hardware_id', '=', hw.id)])
            hw.ticket_count = len(ticket_lines.mapped('ticket_id'))

    @api.constrains('precio')
    def _check_precio_positive(self):
        for record in self:
            if record.precio < 0:
                raise ValueError("El precio debe ser un valor positivo")

    def action_view_tickets(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Tickets asociados a este Hardware',
            'view_mode': 'list,form,search',
            'res_model': 'gestion.ticket',
            'domain': [('ticket_line_ids.hardware_id', '=', self.id)],
        }
