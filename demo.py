# below code is to check the logging config

# from src.logger import logging

# logging.debug("This is a debug message.")
# logging.info("This is an info message.")
# logging.warning("This is a warning message.")
# logging.error("This is an error message.")
# logging.critical("This is a critical message.")


# --------------------------------------------------------------------------------

# # below code is to check the exception config
# from src.logger import logging
# from src.exception import MyException
# import sys

# try:
#     a = 1+'Z'
# except Exception as e:
#     logging.info(e)
#     raise MyException(e, sys) from e

# --------------------------------------------------------------------------------

#Running training pipeline
# from src.pipline.training_pipeline import TrainPipeline

# pipline = TrainPipeline()
# pipline.run_pipeline()

#------------------------------------------------------------------------------------
#Running prediction pipeline and making a prediction to check if it is making prediction or not
from src.pipline.prediction_pipeline import VehicleData, VehicleDataClassifier

# Step 1: Create a dummy input matching the model's expected format
vehicle_data = VehicleData(
    Gender=0,
    Age=38,
    Driving_License=1,
    Region_Code=28,
    Previously_Insured=0,
    Annual_Premium=27734,
    Policy_Sales_Channel=26,
    Vintage=174,
    Vehicle_Age_lt_1_Year=1,
    Vehicle_Age_gt_2_Years=0,
    Vehicle_Damage_Yes=1
)

# Step 2: Convert it to DataFrame
input_df = vehicle_data.get_vehicle_input_data_frame()

# Step 3: Load predictor and make prediction
predictor = VehicleDataClassifier()
result = predictor.predict(dataframe=input_df)

print("Prediction result:", result)
