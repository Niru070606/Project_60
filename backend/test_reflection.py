import os
import sys

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(__file__)
)

sys.path.insert(0, PROJECT_ROOT)

from app import app

from services.reflection.reflection_service import (
    run_reflection,
)

with app.app_context():

    reflections = run_reflection()

    print("\n===== Reflections =====\n")

    for reflection in reflections:
        print(reflection)