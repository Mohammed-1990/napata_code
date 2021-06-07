from odoo import models, fields, api, exceptions

class clearanceRequest(models.Model):
    _inherit = ['mail.thread']
    _name = 'napata.freezing'
    _description = 'freezing information'
    _order = " id desc"
    _rec_name = "student_ids"
    student_ids = fields.Many2one(
        'napata.register', string='Student Name')
    college = fields.Many2one("napata.collage", ondelete="cascade", string="College"
                              , related='student_ids.college_id')
    program = fields.Many2one("napata.program", ondelete="cascade", string="Program"
                              , related='student_ids.program')
    level = fields.Many2one('napata.level', string='the level',
                            ondelete='cascade', related='student_ids.level')
    semester = fields.Many2one('napata.semester', string='Semester',
                               ondelete='cascade', related='student_ids.semester')
    sitting_number = fields.Char(string='Sitting number', related='student_ids.siting_number')
    location_exam = fields.Char(string='School', related='student_ids.school_name')
    st_phone = fields.Char(string=" Phone Number", related='student_ids.phone1')
    st_moble = fields.Char(string="WatsApp", related='student_ids.phone2')
    attachments_one = fields.Image(string="Attachments One")
    attachments_two = fields.Image(string="Attachments Two")
    date_admission = fields.Char(string='Date of admission', related='student_ids.accept_year')
    academic_position = fields.Many2one('napata.result', string='academic position',
                                        ondelete='cascade', related='student_ids.academic_position')
    data = fields.Date(string="Date current action", required=False, readonly=True
                       , default=lambda self: fields.date.today())
    user_name = fields.Char(string="System User ", default=lambda self: self.env.user.name)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('registrar', 'Registrar'),
        ('done', 'done'),
    ], string='Status', default="draft", readonly=True)
    reg_name = fields.Char(string='Register Name ', default=lambda self: self.env.user.name)
    reg_date =fields.Date(string="Date current action", required=False, readonly=True
                       , default=lambda self: fields.date.today())



    def action_confirm_registrar(self):
        self.state = "registrar"
    def action_done(self):
        self.state = "done"

