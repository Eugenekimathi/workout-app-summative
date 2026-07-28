from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

# Define Models here

class Exercise(db.Model):
    __tablename__ = 'exercises'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False , unique=True)
    category = db.Column(db.String(50), nullable=False)
    equipment_needed = db.Column(db.Boolean, nullable=False, default=False)

    workout_exercises = db.relationship("WorkoutExercise", back_populates="exercise", cascade="all, delete-orphan")

    # Model Validation
    @validates("name")
    def validate_name(self, key, value):
        if not value or not value.strip():
            raise ValueError("Exercise name cannot be empty.")
        value = value.strip()
        if len(value) < 2:
            raise ValueError("Exercise name must be at least 2 characters long.")
        return value

    @validates("category")
    def validate_category(self, key, value):

        allowed_categories = [
            "Strength",
            "Cardio",
            "Flexibility",
            "Balance"
        ]

        if value not in allowed_categories:
            raise ValueError(
                f"Category must be one of {allowed_categories}"
            )

        return value

class Workout(db.Model):
    __tablename__ = 'workouts'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    duration_minutes = db.Column(db.Integer, nullable=False)  # Duration in minutes
    notes = db.Column(db.Text)

    workout_exercises = db.relationship("WorkoutExercise", back_populates="workout", cascade="all, delete-orphan")

    # Table Constraints
    __table_args__ = (
        db.CheckConstraint('duration_minutes > 0', name='check_duration_minutes_positive'),
    )

    # Model Validation
    @validates("duration_minutes")
    def validate_duration(self, key, value):
        if value <= 0:
            raise ValueError("Duration must be a positive integer.")
        return value


class WorkoutExercise(db.Model):
    __tablename__ = "workout_exercises"  

    id = db.Column(db.Integer, primary_key=True) 
    workout_id = db.Column(db.Integer, db.ForeignKey("workouts.id"), nullable=False)
    exercise_id = db.Column(db.Integer, db.ForeignKey("exercises.id"), nullable=False)
    reps = db.Column(db.Integer)
    sets = db.Column(db.Integer)
    duration_seconds = db.Column(db.Integer)

    workout = db.relationship("Workout", back_populates="workout_exercises")
    exercise = db.relationship("Exercise", back_populates="workout_exercises")

    # Model Validation
    @validates("reps", "sets", "duration_seconds")
    def validate_workout_exercise_fields(self, key, value):
        if value is not None and value < 0:
            raise ValueError(f"{key} must be a non-negative integer.")
        return value

    # Table Constraints
    __table_args__ = (
        db.CheckConstraint('reps >= 0', name='check_reps_non_negative'),
        db.CheckConstraint('sets >= 0', name='check_sets_non_negative'),
        db.CheckConstraint('duration_seconds >= 0', name='check_duration_seconds_non_negative'),)


   
    