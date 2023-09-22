from odoo import api, fields, models, _


class ApprovalModelStateWizard(models.TransientModel):
    _name = 'approval.model.state.wizard'

    def get_vals(self):
        return self._context['selection_list']

    state = fields.Selection(get_vals, string='Select Status')

    def action_save(self):
        approval_model = self.env['approval.model'].browse(self._context['active_id'])
        if approval_model:
            approval_model.write({'state': self.state})
        return {'type': 'ir.actions.act_window_close'}
