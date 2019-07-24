from odoo import models, fields, api 
class TableEtudiant(models.Model):
    _name='gestion.etudiant'
    _description = 'Iset etudiant'
    cin = fields.Char('CIN Etudiant', size=8, required=True) 
    nome = fields.Char('Nom Etudiant', size=32, required=True) 
    prenome = fields.Char('Prenom Etudiant', size=32, required=True)
    nomc = fields.Char('Classe', size=16, required=True) 