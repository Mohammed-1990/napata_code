
from odoo import models, fields, api ,exceptions
import datetime
class napataPresntaion(models.Model):
    _inherit = ['mail.thread']
    _name = 'napata.presntaionfees'
    _rec_name = 'presntaion_type'
    _description = 'presntaionfees information'
    presntaion_type = fields.Many2one('napata.presentationtype', string='PresntaionType',
                             ondelete='cascade', required=True)
    presntaion_fees=fields.Integer(string="The Presntaion Fees",required=True)
    type_of_fees=fields.Selection([('local','Local currency'),('foreign','Foreign currency')],string="Type Of Fees",required=True)
    year = fields.Char('Study Year',  default=lambda self: datetime.datetime.now().year)

    # active_id  = fields.Selection ([('active', 'ِActive'), ('closed', 'Closed')],
    #           string="Active Presentaion")

    # @api.onchange('active_id')
    # def presntaion_active(self):
    #     last_id = self.env['napata.accounting'].search([])[-1].id
    #     ax = self.env['napata.accounting'].search([('id','=',last_id)])
    #
    #
    #     # self.env['napata.accounting'].write({
    #     #     'presntaion_active': self.pretyep.name,
    #     #
    #     # })
    #     print("@" * 10)
    #
    #     print(ax.presntaion_active)
    #     ax.presntaion_active="mohamed"
    #     print("$" * 10)
    #
    #     print(ax.presntaion_active)



        # if self.active_id:
        #     if self.pretyep:
        #         print(self.active_id)
        #         print("@"*30)
        #         print(self.pretyep)
        #         print(self.pretyep.name)
        #         print("@"*30)
        #     else:
        #         print("#" * 30)
        #         print(self.pretyep)
        #         print(self.pretyep.name)
        #
        #         print("#" * 30)


    # @api.constrains('fees')
    # def _check_something(self):
    #     for record in self:
    #         if record.fees < 100:
    #             raise exceptions.ValidationError("Amount cannot be negative")




# @api.onchange('states_id')
# def get_local(self):
#         get_local_list = []
#         Locals = self.env['reg.locals'].search(
#             [('states_id', '=', self.states_id.id)])
#         if Locals:
#             for rec in Locals:
#                 get_local_list.append(rec.id)
#         return {'domain': {'Local_id': [('id', 'in', get_local_list)]}}





class napataStudy(models.Model):
    _inherit = ['mail.thread']
    _name = 'napata.studyfees'
    _rec_name ='program'
    _description = 'studyfees information'
    program=fields.Many2one("napata.program",ondelete="cascade",string="program")
    # study fees
    sudaness_study=fields.Integer(string="  Study Fees",required=True)
    foreigners_study=fields.Integer(string="  Study Fees",required=True)
    # register fees
    sdn_register_fees = fields.Integer(string="  Register Fees", required=True)
    foriegn_register_fees = fields.Integer(string="  Register Fees ", required=True)
    # card fees
    year = fields.Char('Study Year',  default=lambda self: datetime.datetime.now().year)