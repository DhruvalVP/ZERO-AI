import speedtest
import threading
import pyttsx3

def say(text):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice",voices[4].id) 
    engine.setProperty("rate",165)
    engine.say(text)
    engine.runAndWait()

def download_speed(speed, value_download):
    # Measure the download speed using the Speedtest module.
    download = speed.download()
    # convert download speed into MegaBytes
    download = int(download/800000)
    #print("Downloading speed = ", download, "mbps")
    # Update the first element of the 'value_doenload' list with the download speed.
    value_download[0] = download

def upload_speed(speed, value_upload):
    # Measure the upload speed using thr SpeedTest Module
    upload = speed.upload()
    upload = int(upload/800000)
    #print("Uploading Speed = ", upload, "mbps")
    # Update the first element of the 'value_doenload' list with the download speed.
    value_upload[0] = upload

def testSpeed():
    #print("Checking...")
    # Create an instance of the Speedtest class from the 'speedtest' module.
    speed = speedtest.Speedtest()


    value_download = [0]    # Initialize a list to store the download speed.
    value_upload = [0]  # Initialize a list to store the upload speed.

    # Create two threads for download and upload speed tests.
    download_thread = threading.Thread(target=download_speed, args=(speed, value_download))
    upload_thread = threading.Thread(target=upload_speed, args=(speed, value_upload))

    # Start both Threads.
    download_thread.start()
    upload_thread.start()

    # Wait for both threads to finish.
    download_thread.join()
    upload_thread.join()

    print(f"\nDownloading Speed is {value_download[0]} mbps and\nUploading Speed is {value_upload[0]} mbps")
    try:
        say(f"Your Downloading Speed is {value_download[0]} mbps, and Uploading Speed is {value_upload[0]} mbps")
    except Exception as e:
        print(None)
    # Return the download and upload values stored in the list.
    return f"Downloading Speed is {value_download[0]} mbps and\nUploading Speed is {value_upload[0]} mbps"

# print(testSpeed())
