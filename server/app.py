from flask import Flask, make_response ,request
from flask_migrate import Migrate

from models import *
from schemas import (
    exercise_schema,
    exercises_schema,
    workout_schema,
    workouts_schema,
    workout_exercise_schema
)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

# Define Routes here
# GET /workouts
@app.route("/workouts", methods=["GET"])
def get_workouts():
    workouts = Workout.query.all()
    return make_response(workouts_schema.dump(workouts), 200)

# GET /workouts/<id>
@app.route("/workouts/<int:id>", methods=["GET"])
def get_workout(id):
    workout = Workout.query.filter_by(id=id).first()
    if not workout:
        return make_response({"error": "Workout not found"}, 404)
    return make_response(workout_schema.dump(workout), 200)

# POST /workouts
@app.route("/workouts", methods=["POST"])
def create_workout():
    try:
        workout = workout_schema.load(request.get_json())
        db.session.add(workout)
        db.session.commit()
        return make_response(workout_schema.dump(workout), 201)
    except Exception as e:
        db.session.rollback()
        return make_response({"error": str(e)}, 400)

# DELETE /workouts/<id>
@app.route("/workouts/<int:id>", methods=["DELETE"])
def delete_workout(id):
    workout = Workout.query.filter_by(id=id).first()
    if not workout:
        return make_response({"error": "Workout not found"}, 404)
    db.session.delete(workout)
    db.session.commit()
    return make_response({"message": "Workout deleted successfully"}, 200)

# GET /exercises
@app.route("/exercises", methods=["GET"])
def get_exercises():
    exercises = Exercise.query.all()
    return make_response(exercises_schema.dump(exercises), 200)

# GET /exercises/<id>
@app.route("/exercises/<int:id>", methods=["GET"])
def get_exercise(id):
    exercise = Exercise.query.filter_by(id=id).first()
    if not exercise:
        return make_response({"error": "Exercise not found"}, 404)
    return make_response(exercise_schema.dump(exercise), 200)


# POST /exercises
@app.route("/exercises", methods=["POST"])
def create_exercise():
    try:
        exercise = exercise_schema.load(request.get_json())
        db.session.add(exercise)
        db.session.commit()
        return make_response(exercise_schema.dump(exercise), 201)
    except Exception as e:
        db.session.rollback()
        return make_response({"error": str(e)}, 400)

# DELETE /exercises/<id>
@app.route("/exercises/<int:id>", methods=["DELETE"])  
def delete_exercise(id):
    exercise = Exercise.query.filter_by(id=id).first()
    if not exercise:
        return make_response({"error": "Exercise not found"}, 404)
    db.session.delete(exercise)
    db.session.commit()
    return make_response({"message": "Exercise deleted successfully"}, 200)

#  POST  workout exercise relationship
@app.route("/workouts/<int:workout_id>/exercises/<int:exercise_id>", methods=["POST"])
def create_workout_exercise(workout_id, exercise_id):
    try:
        data = request.get_json()
        workout_exercise = WorkoutExercise(
            workout_id=workout_id,
            exercise_id=exercise_id,
            reps=data.get("reps"),
            sets=data.get("sets"),
            duration_seconds=data.get("duration_seconds")
        )
        db.session.add(workout_exercise)
        db.session.commit()
        return make_response(workout_exercise_schema.dump(workout_exercise), 201)
    except Exception as e:
        db.session.rollback()
        return make_response({"error": str(e)}, 400)

if __name__ == '__main__':
    app.run(port=5555, debug=True)


