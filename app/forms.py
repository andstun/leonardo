from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired, NumberRange

# Form to create sliders for spending type
class sliderForm(FlaskForm):
    
    income = IntegerField("Please enter your income (between 0 and 10,000,000): ", validators = [DataRequired(), NumberRange(min = -1, max = 10000000)])
    tag_select = SelectField("Please enter which type of venues you would like recommendations for: ", 
                            choices = [('Auto and Transport', 'Auto and Transport'), ('Entertainment', 'Entertainment'), ('Food and Dining', 'Food and Dining'), ('Health and Fitness', 'Health and Fitness'), ('Home', 'Home'), ('Shopping', 'Shopping')],
                            validators = [DataRequired()])
    
    slider_1 = IntegerField("Please enter a rough percentage of your money per week that you would like to allocate for Auto and Transport: ", validators = [DataRequired(), NumberRange(min = -1, max = 100)])
    slider_2 = IntegerField("Please enter a rough percentage of your money per week that you would like to allocate for Entertainment: ", validators = [DataRequired(), NumberRange(min = -1, max = 100)])
    slider_3 = IntegerField("Please enter a rough percentage of your money per week that you would like to allocate for Food and Dining: ", validators = [DataRequired(), NumberRange(min = -1, max = 100)])
    slider_4 = IntegerField("Please enter a rough percentage of your money per week that you would like to allocate for Health and Fitness: ", validators = [DataRequired(), NumberRange(min = -1, max = 100)])
    slider_5 = IntegerField("Please enter a rough percentage of your money per week that you would like to allocate for Home: ", validators = [DataRequired(), NumberRange(min = -1, max = 100)])
    slider_6 = IntegerField("Please enter a rough percentage of your money per week that you would like to allocate for Shopping: ", validators = [DataRequired(), NumberRange(min = -1, max = 100)])
    submit = SubmitField('Submit Percentages')