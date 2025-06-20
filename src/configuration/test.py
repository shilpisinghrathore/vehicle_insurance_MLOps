import os
from src.constants import AWS_ACCESS_KEY_ID_ENV_KEY
print("Loaded AWS Key:", os.getenv(AWS_ACCESS_KEY_ID_ENV_KEY))