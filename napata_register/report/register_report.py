import datetime
from num2words import num2words
from odoo import models, fields, api, _
from odoo.exceptions import UserError


class CreateRegisterReport(models.TransientModel):
    _name = 'create.register_report'
    _description = "Create User for selected Student(s)"
    PARAMS = [
        ('general', 'General'),
        ('student', 'student'),
        ('program', 'program'),
        ('presntaion_type', 'presntaion_type'),
        ('certificate_type', 'certificate_type'),
        ('program_presntaion', 'program & presntaion_type'),
        ('program_presntaion_certif', 'program & presntaion_type & certificate_type'),
        ('program_certif', 'program & certificate_type '),
    ]

    student_ids = fields.Many2one(
        'napata.register', string='Student Name')
    program =fields.Many2one("napata.program", ondelete="cascade", string="programs")
    presntaion_type=fields.Many2one("napata.presentationtype",ondelete="cascade",string="Presntaion Type")

    certificate_type = fields.Selection([
        ('sudanese', 'Sudanese'),
        ('foreign', 'Foreign'), ],
        string="Nationality")
    params = fields.Selection(PARAMS, string='Parameters', default='general')


    # def get_report(self):
    #     data = {
    #         'ids': self.ids,
    #         'model': self._name,
    #         'from': {
    #             'student_ids': self.student_ids.ids,
    #             'program': self.program.id,
    #             'presntaion_type': self.presntaion_type,
    #             'certificate_type': self.certificate_type,
    #         }
    #     }
        # return self.env.ref('napata_register.register_custom_report_action').report_action(self, data=data)


# class RegisterReport(models.AbstractModel):
#     _name = 'report.napata_register.Register_template'

#
# def print_register_report(self):
#     """
#     This Function Get The Data For Register Reports
#     """
#     register_ids = self.env['napata.register'].search([])
#     data = {}
#     register_list = []
#
#     if self.program:
#         for rec in register_ids:
#             if rec.program == self.program:
#                 register_list.append(rec.id)
#         register_ids = register_ids.search([('id', 'in', register_list)])
#         register_list = []
#
#     if self.presntaion_type:
#         for rec in register_ids:
#             if rec.presntaion_type == self.presntaion_type:
#                 register_list.append(rec.id)
#         register_ids = register_ids.search([('id', 'in', register_list)])
#         register_list = []
#
#     if self.certificate_type:
#         for rec in register_ids:
#             if rec.certificate_type == self.certificate_type:
#                 register_list.append(rec.id)
#         register_ids = register_ids.search([('id', 'in', register_list)])
#         register_list = []
#
#     for rec in register_ids:
#         register_list.append(rec.id)
#     data = {'register_ids': register_list}
#     return self.env.ref('napata_register.register_custom_report_action').report_action(self, data=data)
