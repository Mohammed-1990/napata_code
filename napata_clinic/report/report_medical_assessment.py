# -*- coding: utf-8 -*-

from odoo import api, models, fields
import datetime

# Added For report
class ReportMedicalAssessment(models.AbstractModel):
    _name = 'report.napata_clinic.report_napata_assessment'
    _description = 'Assessment Report'

    def from_dob_to_age(self, dob):
        if dob:
            today = datetime.date.today()
            return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        else:
            return ""

    @api.model
    def _get_report_values(self, docids, data=None):

        # active_id = data['active_id']
        
        # Make Query
        docs = self.env['napata.assessment'].browse(docids)

        return {
            'doc_ids': docs.ids,
            'doc_model': 'napata.assessment',
            'docs': docs,
            'get_age': self.from_dob_to_age,
            # 'active_id': active_id
    
        }

"""
from dateutil.parser import parse
dt = parse('Mon Feb 15 2010')
print(dt)
# datetime.datetime(2010, 2, 15, 0, 0)
print(dt.strftime('%d/%m/%Y'))
# 15/02/2010
"""