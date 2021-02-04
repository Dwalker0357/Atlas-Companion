from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired, ValidationError
from application.models import maps


class Map_Create_Form(FlaskForm):
    name = StringField("Map Name", validators=[DataRequired()])
    
    regions_id = SelectField("Atlas Region", choices= 
    [(1), (2), (3), (4), (5), (6), (7), (8)], 
    validators=[DataRequired()])
    
    base_tier = IntegerField("Base Map Tier", validators=[DataRequired()])
    
    max_tier = IntegerField("Maximum Map Tier", validators=[DataRequired()])  
    
    Layout = SelectField("Layout Rating", choices=
    [("A"),("B"),("C"),("D")], validators=[DataRequired()])

    boss = IntegerField("Boss Count", validators=[DataRequired()]) 
    
    submit = SubmitField('Submit')

    def validate_name(self, name):
        map_name = maps.query.filter_by(name=name.data).first()
        
        if map_name:
            raise ValidationError("That Map already exists")

