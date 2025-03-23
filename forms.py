from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, DecimalField, SelectField, FileField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo

class LoginForm(FlaskForm):
    email = StringField('Email', validators=)
    password = PasswordField('Password', validators=)
    submit = SubmitField('Accedi')

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=)
    password = PasswordField('Password', validators=)
    confirm_password = PasswordField('Conferma Password', validators=)
    submit = SubmitField('Registrati')

class QuoteForm(FlaskForm):
    material_type = SelectField('Tipologia Materiale', validators=)
    max_dimension = StringField('Dimensioni Massime Elemento', validators=)
    quantity = IntegerField('Quantitativo Richiesto', validators=)
    drawing = FileField('Disegno (PDF/DXF)')
    production_type = SelectField('Tipologia Produzione', validators=)
    submit = SubmitField('Calcola Preventivo')

class MaterialForm(FlaskForm):
    name = StringField('Nome Materiale', validators=)
    cost_per_unit = DecimalField('Costo per Unità', validators=)
    unit = StringField('Unità', validators=)
    dimensions = StringField('Dimensioni')
    thickness = DecimalField('Spessore')
    submit = SubmitField('Salva Materiale')

class ProductionForm(FlaskForm):
    name = StringField('Nome Lavorazione', validators=)
    setup_cost = DecimalField('Costo Setup', validators=)
    cutting_cost_per_sheet = DecimalField('Costo Taglio per Lastra', validators=)
    submit = SubmitField('Salva Lavorazione')

class UserForm(FlaskForm):
    email = StringField('Email', validators=)
    role = SelectField('Ruolo', choices=[('user', 'Utente'), ('admin', 'Amministratore')], validators=)
    submit = SubmitField('Salva Utente')