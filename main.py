import os                                # Provides functions to interact with operating system
from dotenv import load_dotenv           # Loads environment variables from a .env file
from video_utils import LipProcessor     # Import the LipProcessor class from video_utils.py
from lip_sync import LipSyncProcessor    # Import the LipSyncProcessor class from lip_sync.py


# To load the .env file
load_dotenv()

# Retrieve the value of an enviroment variable
BASE_DIR = os.getenv("BASE_DIR")

# Check if the BASE_DIR enviroment variable is set 
if BASE_DIR:
    print(f"Main directory of project's: {BASE_DIR}")
else:
    print("BASE_DIR environment variable could not be loaded.")
    exit(1) # Exit the program if BASE_DIR is not set to avoid errors

# Change the current working directory to the base directory of the project
os.chdir(BASE_DIR)

# Print the current working directory 
print(f"Current Working Directory: {os.getcwd()}")

# Create an instance of the LipProcessor class
processor = LipProcessor(BASE_DIR) 

#Create an instance of the LipSyncProcessor class
lip_sync_processor = LipSyncProcessor(BASE_DIR)



# Define  the input text for text to speech 
#text = "Hello, we are testing our ongoing project, and through this, we will be able to understand how much progress we have made." \
#" This text needs to be a bit longer because I am testing the lip synchronization of our model, and I hope to get a successful result." \
#" It has turned out to be a great project. Well done to us! I love you, stay happy and healthy."
text = "Hello I am dogukan sume. I want to a be a good software enginner in the future so i have to study more"


# Call functions for avatar operations
processor.text_to_speech(text)
processor.image_to_video()


# Run the lip-syncing process for video synchronization
lip_sync_processor.run_lip_sync()
