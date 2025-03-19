import os                        # Provides functions to interact with operating system
from dotenv import load_dotenv   # Loads environment variables from a .env file
from video_utils import LipProcessor  # import functions from the helper pyton file
from lip_sync import LipSyncProcessor

# To load the .env file
load_dotenv()

# Retrieves the value of an enviroment variable
BASE_DIR = os.getenv("BASE_DIR")

# Check if the BASE_DIR enviroment variable is set 
if BASE_DIR:
    print(f"Main directory of project's: {BASE_DIR}")
else:
    print("BASE_DIR environment variable could not be loaded.")
    exit(1) # Exit the program if BASE_DIR is not set

os.chdir(BASE_DIR)


# Create an instance of the LipProcessor class
processor = LipProcessor(BASE_DIR) 


print(f"Current Working Directory: {os.getcwd()}")



# Define  the input text
#text = "Hello, we are testing our ongoing project, and through this, we will be able to understand how much progress we have made." \
" This text needs to be a bit longer because I am testing the lip synchronization of our model, and I hope to get a successful result." \
" It has turned out to be a great project. Well done to us! I love you, stay happy and healthy."

text = "HELLO i am dogukan and I love you so much my mother and father"
#text = "Hello I am Doğukan Süme and i want to be a software enginneer in the future so i am here to be a engineer"

# Call functions for avatar operations

processor.text_to_speech(text)
processor.image_to_video()


lip_sync_processor = LipSyncProcessor(BASE_DIR)
lip_sync_processor.run_lip_sync()
