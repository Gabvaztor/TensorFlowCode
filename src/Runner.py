# -*- coding: utf-8 -*-
"""
Author: @gabvaztor
StartDate: 04/03/2017

This file contains the next information:
    - Libraries to import with installation comment and reason.
    - Data Mining Algorithm.
    - Sets (train,validation and test) information.
    - ANN Arquitectures.
    - A lot of utils methods which you'll get useful advantage


The code's structure is:
    - Imports
    - Global Variables
    - Interface
    - Reading data algorithms
    - Data Mining
    - Training and test
    - Show final conclusions

Style: "Google Python Style Guide"
https://google.github.io/styleguide/pyguide.html

Notes:
    * This file use TensorFlow version >2.0.
"""

from src.config.Configurator import Configurator
from src.Executor import Executor
from src.config.GlobalSettings import IS_PREDICTION

def run(user_id=None, model_selected=None):
    if user_id and model_selected:
        Executor(user_id=user_id, model_selected=model_selected).execute()
    else:
        if Configurator().run():
            Executor().execute()

if __name__ == "__main__":
    if IS_PREDICTION:
        run(user_id="Test")
    else:
        run()
else:
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--userID", required=False,
                    help="userID")
    ap.add_argument("-m", "--userModelSelection", required=False,
                    help="userModelSelection")
    args = vars(ap.parse_args())
    USER_ID = args["userID"] if "userID" in args else None
    MODEL_SELECTED = args["userModelSelection"] if "userModelSelection" in args else None

    run(user_id=USER_ID)  # This means it is a new client petition from PHP.
