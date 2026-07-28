from marshmallow import fields, validate
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from models import *

class WorkoutExerciseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = WorkoutExercise
        load_instance = True
        include_fk = True
        sqla_session = db.session


    workout = fields.Nested(
        "WorkoutSchema",
        exclude=("workout_exercises",)
    )

    exercise = fields.Nested(
        "ExerciseSchema",
        exclude=("workout_exercises",)
    )

class ExerciseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Exercise
        load_instance = True
        sqla_session = db.session


    workout_exercises = fields.Nested(
        WorkoutExerciseSchema,
        many=True,
        exclude=("exercise",)
    )

    name = fields.String(
        required=True,
        validate=validate.Length(
            min=2,
            error="Exercise name must be at least 2 characters."
        )
    )


    category = fields.String(
        required=True,
        validate=validate.OneOf(
            choices=[
                "Strength",
                "Cardio",
                "Flexibility",
                "Balance"
            ],
            error="Invalid exercise category."
        )
    )

class WorkoutSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Workout
        load_instance = True
        sqla_session = db.session


    workout_exercises = fields.Nested(
        WorkoutExerciseSchema,
        many=True,
        exclude=("workout",)
    )


    duration_minutes = fields.Integer(
        required=True,
        validate=validate.Range(
            min=1,
            error="Duration must be greater than zero."
        )
    )



exercise_schema = ExerciseSchema()
exercises_schema = ExerciseSchema(many=True)

workout_schema = WorkoutSchema()
workouts_schema = WorkoutSchema(many=True)

workout_exercise_schema = WorkoutExerciseSchema()
workout_exercises_schema = WorkoutExerciseSchema(many=True)    

   