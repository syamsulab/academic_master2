from odoo import api, fields, models, _

class Attendee(models.Model):
    _name = 'academic.attendee'
    _rec_name = 'name'

    name = fields.Char("Name")
    session_id = fields.Many2one(comodel_name="academic.session", 
                                 string="Session", required=False, )
    partner_id = fields.Many2one(comodel_name="res.partner", string="Partner", required=False, )

    @api.onchange('partner_id')
    def onchange_partner(self):
        self.name = self.partner_id.id
            
    _sql_constraints = [        
        ('partner_session_unique', 'UNIQUE(session_id,partner_id)','Anda tidak dapat memasukkan peserta yang sama lebih dari sekali!')
    ]

    course_id = fields.Many2one(comodel_name="academic.course", string="Course",
                                required=False,
                                related="session_id.course_id",
                                store=True)
    