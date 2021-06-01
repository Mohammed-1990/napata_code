import datetime
import re


from num2words import num2words

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class napataAccounting(models.Model):
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _name = 'napata.accounting'
    _description = 'information accounting'
    _order = "id  desc"
    name = fields.Char(string="full name", compute="get_student_name")
    # studnt  full name
    first = fields.Char(string="First Name")
    second = fields.Char(string="Second Name")
    third = fields.Char(string="Third Name")
    last = fields.Char(string="Last Name")
    # get student name
    student_ids = fields.Many2one(
        'napata.register', string='Student Name')
    college =fields.Many2one("napata.collage", ondelete="cascade",string="College")
    program =fields.Many2one("napata.program", ondelete="cascade",string="Brogram")
    level  = fields.Many2one('napata.level', string='the level',
                                    ondelete='cascade')
    semester = fields.Many2one('napata.semester', string='Semester',
                               ondelete='cascade')
    money_type = fields.Selection([
        ('cash', 'Cash'),
        ('bank', 'Bank'),
    ], string='Method Of Payment')
    # end of name field
    presentation_type = fields.Many2one('napata.presentationtype', string='Bresntaion Type',
                                        ondelete='cascade' )
    student_ids = fields.Char(string="student_ids")
    the_fees = fields.Float(string=" The Fees")
    # fees
    receipt_code = fields.Char(string="Receipt Number"
                               , copy=False, readonly=True, index=True, default=lambda self: _('New'))
    the_amount = fields.Char(string="The Amount")
    about = fields.Char(string="About")
    year = fields.Char(string='Date ', default=lambda self: datetime.datetime.today().strftime('%Y-%m-%d'))
    presentation = fields.Boolean(string='yes ', default=False )
    register_office = fields.Boolean(string='register Office ', default=False )
    #
    admission_ids = fields.Char(string="Admission Name", default=lambda self: self.env.user.name)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirm'),
        ('done', 'done'),
    ], string='Status', default="draft", readonly=True)
    register_office = fields.Boolean(string='register Office ', default=False )
    type_of_fees = fields.Boolean(string=" Type Of Fees",default=False)
    is_managemanent = fields.Boolean(string=" Type Of Fees")



    def get_student_name(self):
        for rec in self:
            rec.name = str(rec.first) + " " + str(rec.second) + " " + str(rec.third) + " " + str(rec.last)

    @api.depends('presentation_type')
    def _compute_presentation_type_name(self):
        for record in self:
            record.name = "Record with value %s" % record.value

    @api.onchange('presentation_type')
    def _compute_fees(self):
        curr_year = datetime.datetime.now().year
        fees = self.env['napata.presntaionfees'].search([('year', '=', curr_year)])
        if fees:
            for record in fees:
                  if record.presntaion_type ==self.presentation_type :
                      if record.presntaion_fees:
                          self.the_fees=record.presntaion_fees
                          if record.type_of_fees== "local":
                              self.the_fees=record.presntaion_fees
                              if self.the_fees > 0.0:
                                  self.the_amount = " فقط " + str(
                                                  "\t " + num2words(self.the_fees, lang='ar')) + " \t    جنية سوداني  لا  غير"
                                  self.about="رسوم تقديم"

                          elif record.type_of_fees == "foreign":
                              self.the_fees=record.presntaion_fees
                              if self.the_fees > 0.0:
                                  self.the_amount = " فقط " + str(
                                                                    "\t " + num2words(self.the_fees, lang='ar')) + " \t  دولار  امريكي لا  غير"
                                  self.about="رسوم تقديم"

                          else:
                              self.the_fees= 0.0
                              self.the_amount ="لم يتم تحديد نوع العملة"
                              self.about = "لم يتم تحديد نوع الرسوم "



    @api.model
    def create(self, vals):
        if vals.get('receipt_code', _('New')) == _('New'):
            vals['receipt_code'] = self.env['ir.sequence'].next_by_code('napata_accounting.account_code.sequence') or _(
                'New')
            result = super(napataAccounting, self).create(vals)

        return result

        # Validate student Frist Name

    @api.constrains('first')
    def validate_student_full_name(self):
        if self.first:
            if not re.search(r'^(?:[^\W\d_]| )+$',
                             str(self.first) + " " + str(self.second) + " " + str(self.third) + " " + str(
                                 self.last)) != None:
                raise UserError(_('The value of student name must only letters'))

    def action_register(self):
       pass

    def action_done(self):
        self.state = "done"
        about = self.about
        result = self.env['napata.register'].browse(int(self.student_ids))
        if self.type_of_fees ==False :
            if self.is_managemanent ==False :
                if result.is_first_installment == True:
                    Remaining_amount = self.the_fees - result.register_fees
                    result.Remaining_amount =    result.Remaining_amount-Remaining_amount
                    result.is_first_installment = False
                elif  result.is_first_installment == False:
                    result.Remaining_amount = (result.Remaining_amount - self.the_fees )


        if self.register_office:
            self.env['napata.feepaid'].create({
                'student_id': self.student_ids,
                'amount': self.the_fees,
                'type': about,
                'the_amount': self.the_amount,
                'receipt_number': self.receipt_code,
                'paid_date': self.year,
                'level': self.level.id,
                'semester': self.semester.id,
            })

        # else:
            # self.state = "done"
            # self.env['napata.chackup'].create({
            #     'name': self.name,
            #     'first': self.first,
            #     'second': self.second,
            #     'third': self.third,
            #     'last': self.last,
            #     'presentation_type': self.presentation_type.id,
            #     'application_fees': self.the_fees,
            #     'pay_date': self.year,
            #     'receipt_code': self.receipt_code,
            # })

    # self.state = "done"
        # self.env['napata.chackup'].create({
        #     'name': self.name,
        #     'first': self.first,
        #     'second': self.second,
        #     'third': self.third,
        #     'last': self.last,
        #     'presentation_type': self.presentation_type.id,
        #     'application_fees': self.the_fees,
        #     'pay_date': self.year,
        #     'receipt_code': self.receipt_code,
        # })

    def print_account_report(self):
      return self.env.ref('napata_accounting.report_session').report_action(self)


