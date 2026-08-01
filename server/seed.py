#!/usr/bin/env python3

from datetime import date
from server.app import app
from server.models import *

with app.app_context():

    print("Clearing database...")

    WorkoutExercise.query.delete()
    Workout.query.delete()
    Exercise.query.delete()

    print("creating exercises...")

    push_up = Exercise(
        name="push-up", 
        category="Strength", 
        equipment_needed=False
    )
    squat = Exercise(
        name="Bodyweight Squat",
        category="Strength",
        equipment_needed=False
    )

    jumping_jacks = Exercise(
        name="Jumping Jacks",
        category="Cardio",
        equipment_needed=False
    )

    plank = Exercise(
        name="Plank",
        category="Balance",
        equipment_needed=False
    )

    yoga = Exercise(
        name="Hamstring Stretch",
        category="Flexibility",
        equipment_needed=False
    )

    dumbbell_press = Exercise(
        name="Dumbbell Bench Press",
        category="Strength",
        equipment_needed=True
    )

    db.session.add_all([
        push_up,
        squat,
        jumping_jacks,
        plank,
        yoga,
        dumbbell_press
    ])

    print("Creating workouts...")

    workout1 = Workout(
        date=date(2025, 7, 10),
        duration_minutes=45,
        notes="Upper body workout"
    )

    workout2 = Workout(
        date=date(2025, 7, 12),
        duration_minutes=35,
        notes="Leg day"
    )

    workout3 = Workout(
        date=date(2025, 7, 15),
        duration_minutes=30,
        notes="Morning cardio session"
    )

    db.session.add_all([
        workout1,
        workout2,
        workout3
    ])

    db.session.flush()

    print("Creating workout exercises...")

    workout_exercises = [

        WorkoutExercise(
            workout=workout1,
            exercise=push_up,
            sets=4,
            reps=15
        ),

        WorkoutExercise(
            workout=workout1,
            exercise=dumbbell_press,
            sets=3,
            reps=12
        ),

        WorkoutExercise(
            workout=workout2,
            exercise=squat,
            sets=4,
            reps=20
        ),

        WorkoutExercise(
            workout=workout2,
            exercise=plank,
            duration_seconds=60,
            sets=3
        ),

        WorkoutExercise(
            workout=workout3,
            exercise=jumping_jacks,
            duration_seconds=300
        ),

        WorkoutExercise(
            workout=workout3,
            exercise=yoga,
            duration_seconds=180
        )
    ]

    db.session.add_all(workout_exercises)

    db.session.commit()

    print("Done!")


