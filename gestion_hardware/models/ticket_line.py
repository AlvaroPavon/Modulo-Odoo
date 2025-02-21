from odoo import models, fields, api
from odoo.exceptions import ValidationError

class TicketLine(models.Model):
    _name = 'gestion.ticket.line'
    _description = 'Línea de Producto en Ticket'

    # Relación Many2one con el ticket
    ticket_id = fields.Many2one('gestion.ticket', string="Ticket", ondelete='cascade')
    # Relación Many2one con producto
    hardware_id = fields.Many2one('gestion.hardware', string="Producto", required=True)
    # Cantidad de producto, debe ser mayor que 0
    quantity = fields.Integer(string="Cantidad", default=1, required=True)
    # Campo calculado: total de la línea = precio del hardware * cantidad
    line_total = fields.Float(string="Total Línea", compute="_compute_line_total", store=True)

    @api.depends('hardware_id', 'quantity')
    def _compute_line_total(self):
        for line in self:
            if line.hardware_id:
                line.line_total = line.hardware_id.precio * line.quantity
            else:
                line.line_total = 0

    @api.constrains('quantity')
    def _check_quantity_positive(self):
        for line in self:
            if line.quantity <= 0:
                raise ValidationError("La cantidad debe ser mayor a 0")

    @api.model
    def create(self, vals):
        hardware_id = vals.get('hardware_id')
        quantity = vals.get('quantity', 0)
        hardware = self.env['gestion.hardware'].browse(hardware_id)
        if hardware.stock < quantity:
            raise ValidationError("No hay suficiente stock para este producto (stock actual: %s)" % hardware.stock)
        record = super(TicketLine, self).create(vals)
        hardware.stock -= record.quantity
        return record

    def write(self, vals):
        for line in self:
            new_qty = vals.get('quantity', line.quantity)
            if new_qty != line.quantity:
                diff = new_qty - line.quantity
                # Si se incrementa la cantidad, se verifica el stock adicional disponible
                if diff > 0:
                    if line.hardware_id.stock < diff:
                        raise ValidationError("No hay suficiente stock para aumentar la cantidad (stock actual: %s)" % line.hardware_id.stock)
                    line.hardware_id.stock -= diff
                # Si se reduce la cantidad, se devuelve la diferencia al stock
                else:
                    line.hardware_id.stock += -diff
        return super(TicketLine, self).write(vals)

    def unlink(self):
        for line in self:
            if line.hardware_id:
                line.hardware_id.stock += line.quantity
        return super(TicketLine, self).unlink()
