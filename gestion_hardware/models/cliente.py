from odoo import models, fields

class Cliente(models.Model):
    _inherit = 'res.partner'

    # One2many para asociar tickets a cada cliente
    ticket_ids = fields.One2many('gestion.ticket', 'cliente_id', string="Tickets")

    def action_view_tickets(self):
        """
        Abre una ventana con la lista de tickets asociados a este cliente.
        """
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Tickets del Cliente',
            'view_mode': 'list,form',
            'res_model': 'gestion.ticket',
            'domain': [('cliente_id', '=', self.id)],
        }
