from django.shortcuts import render, redirect
from django.templatetags.static import static
from .forms import RegistrationForm
from .forms import AttendanceForm
import cv2
import os
import time
from skimage.metrics import structural_similarity as ssim
import pandas as pd
from datetime import datetime
import csv
from .forms import ShowAttendanceForm
from django.shortcuts import render, HttpResponseRedirect
import numpy as np
import shutil
import re
# ---for mac address
import psutil
import socket
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout, get_user_model
from .forms import CustomUserCreationForm, CustomAuthenticationForm, ContactForm
from collections import defaultdict
from django.contrib.auth.decorators import login_required
from .models import Attendance, Registration, SystemInfo
from datetime import datetime
from django.utils import timezone
import psutil
import sounddevice as sd
from scipy.io.wavfile import write
import os
import sounddevice as sd
from scipy.io.wavfile import write
import speech_recognition as sr
import time
import pyaudio
import wave
from datetime import datetime



def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def team(request):
    return render(request, 'team.html')

# def contact(request):
#     return render(request, 'contact.html')


def contact_view(request):
    success_message = None
    submission_time = None

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            success_message = "Thank you! Your message has been successfully submitted."
            submission_time = contact.created_at  # Get the submission time
            form = ContactForm()  # Reset form after successful submission
    else:
        form = ContactForm()

    return render(request, 'contact.html', {
        'form': form,
        'success_message': success_message,
        'submission_time': submission_time
    })

# Create your views here.

def get_mac_address():
    for _, addrs in psutil.net_if_addrs().items():
        for addr in addrs:
            if addr.family == psutil.AF_LINK and addr.address:
                return addr.address
    return None


ALLOWED_MAC_ADDRESSES = ["00-E0-4C-0A-BC-8B", "10-68-38-54-AE-C6", "12-68-38-54-8E-E6", "8C-16-45-E7-CC-2C", "00-E0-4C-0A-BC-A2","D8-9D-67-CA-86-F8","B8-76-3F-27-42-5D"]


def index(request):
    # Get user's MAC address
    mac_address = get_mac_address()
    local_ip_address = socket.gethostbyname(socket.gethostname())

    # Check if the MAC address is in the allowed list
    if mac_address in ALLOWED_MAC_ADDRESSES:
        print("welcome to the attendance system")
        # Render the index.html template
        user_authenticated = request.user.is_authenticated
        context = {
            'mac_address': mac_address,
            'local_ip_address': local_ip_address,
            'user_authenticated': user_authenticated,
        }
        return render(request, 'index.html', context)
    else:
        # Redirect to the success_page.html
        return redirect('success_page')


# def capture_images_for_dataset(trade, roll_number, user_name):
#     cam = cv2.VideoCapture(0)
#     file_path = os.path.join('systemAPP', 'haarcascade_frontalface_default.xml')
#     detector = cv2.CascadeClassifier(file_path)
#     sampleNum = 0

#     # Specify the directory to save images
#     save_path = os.path.join("dataSet", trade, str(roll_number),"face")

#     # Check if the directory exists, if not, create it
#     if not os.path.exists(save_path):
#         os.makedirs(save_path)

#     # Remove existing images if the user is registering again
#     existing_images = os.listdir(save_path)
#     for existing_image in existing_images:
#         os.remove(os.path.join(save_path, existing_image))

#     # List to store the image paths
#     image_paths = []

#     # Capture 100 images for the dataset
#     while sampleNum < 100:
#         ret, img = cam.read()
#         gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#         faces = detector.detectMultiScale(gray, 1.3, 5)

#         for (x, y, w, h) in faces:
#             cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
#             sampleNum += 1
#             # Use userName and rollNumber in the image_path
#             image_path = os.path.join(save_path, f'{user_name}.{roll_number}.{sampleNum}.jpg')
#             cv2.imwrite(image_path, gray[y:y + h, x:x + w])
#             image_paths.append(image_path)
#             cv2.imshow('frame', img)

#         if cv2.waitKey(100) & 0xFF == ord('q'):
#             break

#     cam.release()
#     cv2.destroyAllWindows()

#     # Print the captured image paths
#     for path in image_paths:
#         print(f"Captured image: {path}")


# @login_required
# def register_view(request):
#     already_register = False
#     already_register_message = ""
#     mac_address = get_mac_address()
#     local_ip_address = socket.gethostbyname(socket.gethostname())

#     if mac_address in ALLOWED_MAC_ADDRESSES:
#         print("Welcome to the attendance system")
#         if request.method == 'POST':
#             form = RegistrationForm(request.POST)
#             if form.is_valid():
#                 trade = form.cleaned_data['trade']
#                 roll_number = form.cleaned_data['rollNumber']
#                 user_name = form.cleaned_data['userName']
#                 latitude = request.POST.get('latitude')
#                 longitude = request.POST.get('longitude')

#                 # Specify the directory to check for existing images
#                 save_path = os.path.join("dataSet", trade, str(roll_number),"face")

#                 # Check if the directory exists and has images
#                 if os.path.exists(save_path) and len(os.listdir(save_path)) > 0:
#                     # User is already registered
#                     already_register = True
#                     already_register_message = f"User {user_name} with roll number {roll_number} is already registered."
#                 else:
#                     # If not registered, proceed with image capturing
#                     capture_images_for_dataset(trade, roll_number, user_name)

#                     # If not registered, save the data to the database 
#                     Registration.objects.create(trade=trade, roll_number=roll_number, full_name=user_name)

#                     # Get public IP address, handle None case 
#                     public_ip_address = request.META.get('HTTP_X_FORWARDED_FOR')
#                     if not public_ip_address:
#                         public_ip_address = "Unknown"

#                     # Save system information to the database
#                     SystemInfo.objects.create(
#                         mac_address=mac_address,
#                         public_ip_address=public_ip_address,
#                         local_ip_address=local_ip_address,
#                         latitude=latitude,
#                         longitude=longitude,
#                         trade=trade,
#                         roll_number=roll_number
#                     )
#                     # For example, you can save the data to the database

#                     # Process form data here
#                     # For example, you can save the data to the database
#                     # and then redirect to a success page
#                     messages.success(request,
#                                      f"{user_name}! your registration is successful with roll number {roll_number}.")
#                     return redirect('index')
#         else:
#             form = RegistrationForm()

#         context = {
#             'form': form,
#             'already_register': already_register,
#             'already_register_message': already_register_message,
#             'mac_address': mac_address,
#             'local_ip_address': local_ip_address,
#         }
#         return render(request, 'register.html', context)
#     else:
#         # Redirect to the success_page.html or handle unauthorized access differently
#         return redirect('success_page')





# Capture images for dataset (with enhanced eye image quality)
def capture_images_for_dataset(trade, roll_number, user_name, data_type='face'):
    cam = cv2.VideoCapture(0)
    
    if data_type == 'face':
        cascade_file = 'haarcascade_frontalface_default.xml'
    elif data_type == 'eye':
        cascade_file = 'haarcascade_eye.xml'
    else:
        raise ValueError("Invalid data type")

    file_path = os.path.join('systemAPP', cascade_file)
    detector = cv2.CascadeClassifier(file_path)
    sampleNum = 0

    save_path = os.path.join("dataSet", trade, str(roll_number), data_type)

    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # Remove existing images if the user is registering again
    existing_images = os.listdir(save_path)
    for existing_image in existing_images:
        os.remove(os.path.join(save_path, existing_image))

    image_paths = []

    while sampleNum < 100:
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        features = detector.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in features:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            sampleNum += 1
            image_path = os.path.join(save_path, f'{user_name}.{roll_number}.{sampleNum}.jpg')

            # Enhance image quality (for eye detection)
            if data_type == 'eye':
                enhanced_image = cv2.equalizeHist(gray[y:y + h, x:x + w])  # Enhance contrast
                cv2.imwrite(image_path, enhanced_image)
            else:
                cv2.imwrite(image_path, gray[y:y + h, x:x + w])

            image_paths.append(image_path)
            cv2.imshow('Scanning', img)

        if cv2.waitKey(100) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()

    for path in image_paths:
        print(f"Captured image: {path}")

# Capture voice dataset with a message in HTML
def capture_voice_for_dataset(trade, roll_number, user_name):
    import os
    import sounddevice as sd
    from scipy.io.wavfile import write
    import speech_recognition as sr
    import numpy as np

    fs = 44100
    seconds = 10

    save_path = os.path.join("dataSet", trade, str(roll_number), "voice")

    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # Display message in HTML (this will be controlled from the view using context variables)
    print("Speak Now, your voice is being recorded...")

    # Record the voice sample
    voice_sample = sd.rec(int(seconds * fs), samplerate=fs, channels=1)  # Use mono channel
    sd.wait()
    voice_file_path = os.path.join(save_path, f'{user_name}.{roll_number}.wav')

    # Ensure the data type is correct for saving
    voice_sample = np.int16(voice_sample * 32767)  # Convert to 16-bit PCM

    # Write the WAV file
    write(voice_file_path, fs, voice_sample)
    print(f"Captured voice sample: {voice_file_path}")

    # Convert voice to text
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(voice_file_path) as source:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data)
            print(f"Voice to text conversion successful: {text}")
            
            # Save the text to a file
            text_file_path = os.path.join(save_path, f'{user_name}.txt')
            with open(text_file_path, 'w') as text_file:
                text_file.write(text)
            print(f"Text file saved at: {text_file_path}")
    
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")



# View function for user registration
@login_required
def register_view(request):
    already_register = False
    already_register_message = ""
    mac_address = get_mac_address()
    local_ip_address = socket.gethostbyname(socket.gethostname())

    if mac_address in ALLOWED_MAC_ADDRESSES:
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                trade = form.cleaned_data['trade']
                roll_number = form.cleaned_data['rollNumber']
                user_name = form.cleaned_data['userName']
                latitude = request.POST.get('latitude')
                longitude = request.POST.get('longitude')

                capture_type = request.POST.get('capture_type')

                face_path = os.path.join("dataSet", trade, str(roll_number), "face")
                eye_path = os.path.join("dataSet", trade, str(roll_number), "eye")
                voice_path = os.path.join("dataSet", trade, str(roll_number), "voice")

                # Check if face is registered first
                if capture_type == 'eye' and not os.path.exists(face_path):
                    messages.error(request, "Please register face first before registering eyes.")
                elif capture_type == 'voice' and not os.path.exists(face_path):
                    messages.error(request, "Please register face first before registering voice.")
                elif capture_type == 'voice' and not os.path.exists(eye_path):
                    messages.error(request, "Please register eyes before registering voice.")
                else:
                    # Capture based on the type selected
                    if capture_type == 'face':
                        capture_images_for_dataset(trade, roll_number, user_name, 'face')
                    elif capture_type == 'eye':
                        capture_images_for_dataset(trade, roll_number, user_name, 'eye')
                    elif capture_type == 'voice':
                        capture_voice_for_dataset(trade, roll_number, user_name)

                    Registration.objects.create(trade=trade, roll_number=roll_number, full_name=user_name)

                    SystemInfo.objects.create(
                        mac_address=mac_address,
                        public_ip_address=request.META.get('HTTP_X_FORWARDED_FOR') or "Unknown",
                        local_ip_address=local_ip_address,
                        latitude=latitude,
                        longitude=longitude,
                        trade=trade,
                        roll_number=roll_number
                    )
                    messages.success(request, f"{user_name}, your {capture_type} registration is successful with roll number {roll_number}.")
                    return redirect('register')
        else:
            form = RegistrationForm()

        context = {
            'form': form,
            'already_register': already_register,
            'already_register_message': already_register_message,
            'mac_address': mac_address,
            'local_ip_address': local_ip_address,
        }
        return render(request, 'register.html', context)
    else:
        return redirect('success_page')



#  --------register task is over ------



# def capture_and_compare(trade, roll_number):
#     # Wait for 1 second before capturing another image
#     time.sleep(0)
#     cam = cv2.VideoCapture(0)
#     file_path = os.path.join('systemAPP', 'haarcascade_frontalface_default.xml')
#     detector = cv2.CascadeClassifier(file_path)

#     ret, img = cam.read()
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     faces = detector.detectMultiScale(gray, 1.3, 5)

#     captured_image = None  # Initialize captured_image outside the loop

#     for (x, y, w, h) in faces:
#         cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
#         captured_image = gray[y:y + h, x:x + w]
#         cv2.imshow('frame', img)

#     # Save the captured image to the capture_image folder
#     capture_images_folder = os.path.join("capture_image", trade, str(roll_number))
#     if not os.path.exists(capture_images_folder):
#         os.makedirs(capture_images_folder)

#     if captured_image is not None:
#         # Check if there are any existing images in the folder
#         existing_images = [f for f in os.listdir(capture_images_folder) if
#                            os.path.isfile(os.path.join(capture_images_folder, f))]

#         if existing_images:
#             # If there are existing images, overwrite the first one
#             existing_image_path = os.path.join(capture_images_folder, existing_images[0])
#             cv2.imwrite(existing_image_path, captured_image)
#             captured_image_path = existing_image_path
#         else:
#             # If there are no existing images, create a new one
#             current_time = time.strftime("%Y%m%d_%H%M%S")
#             captured_image_path = os.path.join(capture_images_folder, f'captured_{current_time}.jpg')
#             cv2.imwrite(captured_image_path, captured_image)

#         cam.release()
#         cv2.destroyAllWindows()

#         return captured_image_path
#     else:
#         # Handle the case when no faces are detected
#         print("No faces detected.")
#         cam.release()
#         cv2.destroyAllWindows()
#         return redirect('/take-attendance/')  # or raise an exception, or redirect as needed

# -----herer i am do some code --- -------------------------------

# def capture_and_compare(trade, roll_number):
#     # Initialize the camera
#     cam = cv2.VideoCapture(0)
#     if not cam.isOpened():
#         print("Error: Camera not opened.")
#         return redirect('/take-attendance/')  # Handle camera error

#     file_path = os.path.join('systemAPP', 'haarcascade_frontalface_default.xml')
#     detector = cv2.CascadeClassifier(file_path)

#     ret, img = cam.read()
#     if not ret:
#         print("Error: Unable to capture image.")
#         cam.release()
#         cv2.destroyAllWindows()
#         return redirect('/take-attendance/')  # Handle image capture error

#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     faces = detector.detectMultiScale(gray, 1.3, 5)

#     captured_image = None

#     for (x, y, w, h) in faces:
#         cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
#         captured_image = gray[y:y + h, x:x + w]
#         # Uncomment for debugging purposes
#         # cv2.imshow('frame', img)
#         # cv2.waitKey(0)

#     # Release the camera and close windows
#     cam.release()
#     cv2.destroyAllWindows()

#     # Save the captured image
#     capture_images_folder = os.path.join("capture_image", trade, str(roll_number))
#     if not os.path.exists(capture_images_folder):
#         os.makedirs(capture_images_folder)

#     if captured_image is not None:
#         existing_images = [f for f in os.listdir(capture_images_folder) if os.path.isfile(os.path.join(capture_images_folder, f))]

#         if existing_images:
#             existing_image_path = os.path.join(capture_images_folder, existing_images[0])
#             cv2.imwrite(existing_image_path, captured_image)
#             captured_image_path = existing_image_path
#         else:
#             current_time = time.strftime("%Y%m%d_%H%M%S")
#             captured_image_path = os.path.join(capture_images_folder, f'captured_{current_time}.jpg')
#             cv2.imwrite(captured_image_path, captured_image)

#         return captured_image_path
#     else:
#         print("No faces detected.")
#         return redirect('/take-attendance/')

#  ------code is over --------    

# ------new code ---- 

# def capture_and_compare(trade, roll_number, capture_type):
#     print(f"Capture Type kapil: {capture_type}")
#     cam = cv2.VideoCapture(0)
#     if not cam.isOpened():
#         print("Error: Camera not opened.")
#         return redirect('/take-attendance/')

#     if capture_type == 'face':
#         cascade_file = 'haarcascade_frontalface_default.xml'
#     elif capture_type == 'eye':
#         cascade_file = 'haarcascade_frontalface_default.xml'  # First detect face for eye detection
#         eye_cascade_file = 'haarcascade_eye.xml'
#     else:
#         print("Error: Invalid capture type.")
#         cam.release()
#         cv2.destroyAllWindows()
#         return redirect('/take-attendance/')

#     face_detector = cv2.CascadeClassifier(os.path.join('systemAPP', cascade_file))

#     ret, img = cam.read()
#     if not ret:
#         print("Error: Unable to capture image.")
#         cam.release()
#         cv2.destroyAllWindows()
#         return redirect('/take-attendance/')

#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     faces = face_detector.detectMultiScale(gray, 1.3, 5)

#     captured_image = None
#     for (x, y, w, h) in faces:
#         cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
#         if capture_type == 'face':
#             captured_image = gray[y:y + h, x:x + w]
#         elif capture_type == 'eye':
#             face_roi = gray[y:y + h, x:x + w]  # Region of interest for eyes
#             eye_detector = cv2.CascadeClassifier(os.path.join('systemAPP', eye_cascade_file))
#             eyes = eye_detector.detectMultiScale(face_roi, 1.1, 3)

#             for (ex, ey, ew, eh) in eyes:
#                 cv2.rectangle(img, (x + ex, y + ey), (x + ex + ew, y + ey + eh), (0, 255, 0), 2)
#                 captured_image = face_roi[ey:ey + eh, ex:ex + ew]  # Capture the eye region
#                 break  # Capture only one eye for simplicity

#     cam.release()
#     cv2.destroyAllWindows()

#     # Save the captured image as before
#     capture_images_folder = os.path.join("capture_image", trade, str(roll_number))
#     if not os.path.exists(capture_images_folder):
#         os.makedirs(capture_images_folder)

#     if captured_image is not None:
#         existing_images = [f for f in os.listdir(capture_images_folder) if os.path.isfile(os.path.join(capture_images_folder, f))]

#         if existing_images:
#             existing_image_path = os.path.join(capture_images_folder, existing_images[0])
#             cv2.imwrite(existing_image_path, captured_image)
#             captured_image_path = existing_image_path
#         else:
#             current_time = time.strftime("%Y%m%d_%H%M%S")
#             captured_image_path = os.path.join(capture_images_folder, f'captured_{current_time}.jpg')
#             cv2.imwrite(captured_image_path, captured_image)

#         return captured_image_path
#     else:
#         print(f"No {capture_type} detected.")
#         return redirect('/take-attendance/')

# -------new code is over ---- 

def capture_and_compare(trade, roll_number, capture_type):
    print(f"Capture Type kapil: {capture_type}")
    cam = cv2.VideoCapture(0)
    if not cam.isOpened():
        print("Error: Camera not opened.")
        return redirect('/take-attendance/')

    if capture_type == 'face':
        cascade_file = 'haarcascade_frontalface_default.xml'
    elif capture_type == 'eye':
        cascade_file = 'haarcascade_frontalface_default.xml'  # First detect face for eye detection
        eye_cascade_file = 'haarcascade_eye.xml'
    else:
        print("Error: Invalid capture type.")
        cam.release()
        cv2.destroyAllWindows()
        return redirect('/take-attendance/')

    face_detector = cv2.CascadeClassifier(os.path.join('systemAPP', cascade_file))

    ret, img = cam.read()
    if not ret:
        print("Error: Unable to capture image.")
        cam.release()
        cv2.destroyAllWindows()
        return redirect('/take-attendance/')

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    captured_image = None
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        if capture_type == 'face':
            captured_image = gray[y:y + h, x:x + w]
        elif capture_type == 'eye':
            face_roi = gray[y:y + h, x:x + w]  # Region of interest for eyes
            eye_detector = cv2.CascadeClassifier(os.path.join('systemAPP', eye_cascade_file))
            eyes = eye_detector.detectMultiScale(face_roi, 1.1, 3)

            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(img, (x + ex, y + ey), (x + ex + ew, y + ey + eh), (0, 255, 0), 2)
                captured_image = face_roi[ey:ey + eh, ex:ex + ew]  # Capture the eye region
                break  # Capture only one eye for simplicity

    cam.release()
    cv2.destroyAllWindows()

    # Save the captured image as before
    capture_images_folder = os.path.join("capture_image", trade, str(roll_number))
    if not os.path.exists(capture_images_folder):
        os.makedirs(capture_images_folder)




    if captured_image is not None:
        existing_images = [f for f in os.listdir(capture_images_folder) if os.path.isfile(os.path.join(capture_images_folder, f))]

        if existing_images:
            existing_image_path = os.path.join(capture_images_folder, existing_images[0])
            cv2.imwrite(existing_image_path, captured_image)
            captured_image_path = existing_image_path
        else:
            current_time = time.strftime("%Y%m%d_%H%M%S")
            captured_image_path = os.path.join(capture_images_folder, f'captured_{current_time}.jpg')
            cv2.imwrite(captured_image_path, captured_image)

        # Update the database
        try:
            # Fetch the Attendance record for the given roll_number
            attendance = Attendance.objects.get(roll_number=roll_number, trade_name=trade)

            if capture_type == 'face':
                # If face is captured and comparison is true
                attendance.face_points = '1'  # Update this based on your  face_points comparison logic
            elif capture_type == 'eye':
                # If eye is captured and comparison is true
                attendance.eye_points = '1'  # Update this based on your eye_points comparison logic
           
            attendance.save()
            print("Database updated successfully.")
        except Attendance.DoesNotExist:
            print(f"Attendance record for roll number {roll_number} not found.")
        
        return captured_image_path
    else:
        print(f"No {capture_type} detected.")
        return redirect('/take-attendance/')

    

def image_matching(image1_path, capture_folder):
    # Load images
    image1 = cv2.imread(image1_path, cv2.IMREAD_GRAYSCALE)

    if image1 is None:
        print(f"Error: Unable to read image {image1_path}")
        return 0

    # Resize image1 to a fixed size (adjust if needed)
    image1 = cv2.resize(image1, (300, 300))

    # List all files in the "capture_folder"
    capture_images = [f for f in os.listdir(capture_folder) if
                      os.path.isfile(os.path.join(capture_folder, f))]

    if capture_images:
        # Get the latest image from the folder
        latest_image_path = os.path.join(capture_folder, max(capture_images))
        image2 = cv2.imread(latest_image_path)

        # Resize image2 to the same dimensions as image1
        image2 = cv2.resize(image2, (300, 300))

        # Convert image2 to grayscale
        gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

        try:
            # Calculate Structural Similarity Index (SSI)
            ssim_index, _ = ssim(image1, gray2, full=True)

            # Calculate Mean Squared Error (MSE)
            mse = ((image1 - gray2) ** 2).mean()

            # Adjust the thresholds based on your requirements
            ssim_threshold = 0.5  # Adjust as needed
            mse_threshold = 1500  # Adjust as needed

            print(f"Comparison result for {os.path.basename(image1_path)} and {os.path.basename(latest_image_path)}:")
            print(f"SSI: {ssim_index}, MSE: {mse}")

            if ssim_index > ssim_threshold and mse < mse_threshold:
                return 1, ssim_index, mse  # Images match
            else:
                return 0, ssim_index, mse  # Images do not match
        except Exception as e:
            print(f"Error during image comparison: {e}")
            return 0
    else:
        print(f"No images found in the capture folder: {capture_folder}")
        return 0



def record_audio(duration=10, filename="audio_recording.wav"):
    # Set up parameters for recording audio
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000

    # Initialize pyaudio
    audio = pyaudio.PyAudio()

    # Open stream for recording
    stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

    print("Recording started...")
    frames = []

    # Record the audio for the given duration
    for _ in range(int(RATE / CHUNK * duration)):
        data = stream.read(CHUNK)
        frames.append(data)

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Save the recorded audio to a file
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))

    print(f"Recording finished. Audio saved as {filename}")
    return filename

def convert_audio_to_text(audio_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as audio_file:
        audio = recognizer.record(audio_file)
        try:
            # Convert the audio to text using Google Speech Recognition
            text = recognizer.recognize_google(audio)
            print("Audio converted to text:", text)
            return text
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
    return None





# def take_attendance_view(request):
#     form = AttendanceForm()
#     mac_address = get_mac_address()
#     local_ip_address = socket.gethostbyname(socket.gethostname())
#     if mac_address in ALLOWED_MAC_ADDRESSES:

#         if request.method == 'POST':
#             form = AttendanceForm(request.POST)
#             if form.is_valid():
#                 # Process form data here
#                 trade = form.cleaned_data['trade']
#                 roll_number = form.cleaned_data['rollNumber']
#                 # capture_type = request.POST.get('captureType', 'face')

#                 # Capture type can be 'face', 'eye', or 'voice'
#                 capture_type = request.POST.get('captureType')  # Default to face
                
#                 if capture_type == 'voice':
#                     # Record 10-second audio using SpeechRecognition
#                     r = sr.Recognizer()
#                     with sr.Microphone() as source:
#                         print("Recording audio for 10 seconds...")
#                         audio_data = r.record(source, duration=10)
                    
#                     # Convert audio to text
#                     try:
#                         text_from_audio = r.recognize_google(audio_data)
#                         print(f"Audio Text: {text_from_audio}")
#                     except sr.UnknownValueError:
#                         return render(request, 'take_attendance.html', {'form': form, 'error_message': "Audio not clear, please try again."})
#                     except sr.RequestError:
#                         return render(request, 'take_attendance.html', {'form': form, 'error_message': "Could not process audio."})

#                     # Define paths for saving audio and text files
#                     dataSet_dir = os.path.join("capture_audio", trade, str(roll_number), capture_type)
#                     if not os.path.exists(dataSet_dir):
#                         os.makedirs(dataSet_dir)

#                     # Save the audio file
#                     audio_file_path = os.path.join(dataSet_dir, 'audio_recording.wav')
#                     with open(audio_file_path, 'wb') as f:
#                         f.write(audio_data.get_wav_data())

#                     # Save the transcribed text to a file
#                     audio_text_file_path = os.path.join(dataSet_dir, 'audio_text.txt')
#                     with open(audio_text_file_path, 'w') as f:
#                         f.write(text_from_audio)

#                     # Define path for the comparison text file
#                     stored_images_dir = os.path.join("dataSet", trade, str(roll_number), capture_type)

#                     try:
#                         # Automatically detect a .txt file in the comparison directory
#                         comparison_text_file = None
#                         for file in os.listdir(stored_images_dir):
#                             if file.endswith(".txt"):
#                                 comparison_text_file = os.path.join(stored_images_dir, file)
#                                 break

#                         if comparison_text_file:
#                             # Read the comparison file content
#                             with open(comparison_text_file, 'r') as f:
#                                 comparison_text = f.read()

#                             # Compare the two texts
#                             if text_from_audio.strip() == comparison_text.strip():
#                                 voice_points = '1'
#                                 message = "Your attendance is being recorded. Please check the 'Show Attendance' page."
#                                 print("Your Voice matches in our database.")

#                                 # Get or create the Attendance object
#                                 attendance, created = Attendance.objects.get_or_create(
#                                     trade_name=trade,
#                                     roll_number=roll_number,
#                                 )
#                                 # Update voice points
#                                 attendance.voice_points = voice_points
#                                 attendance.save()
#                             else:
#                                 message = "Both text files are different."
#                                 print("Your Voice is Not match in our database.")
#                         else:
#                             form = AttendanceForm()
#                             message = "Comparison file not found. Please make sure it exists."
#                             print(message)
                            
#                     except FileNotFoundError:
#                         message = "You are not registered. Please register first and get back to you."
#                         print(message)

#                     # Return context
#                     context = {
#                         'form': form,
#                         'message': message,
#                         'audio_text': text_from_audio,
#                         'audio_file_path': audio_file_path,
#                         'success': True if message == "Both text files are the same." else False,
#                     }
#                     return render(request, 'take_attendance.html', context)
#                 print("hy capcture data is **********************************************",capture_type)

#                 # Present and absent condition where all three point should be 1
                
#                 # Get the current date and time               
#                 now = datetime.now()
#                 attendance_date = now.strftime("%Y-%m-%d")

#                 # Call the function to capture images for attendance
#                 captured_image_path = capture_and_compare(trade, roll_number, capture_type)

#                 if captured_image_path is None:
#                     error_message = "No faces detected. Please try again."
#                     context = {'form': form, 'error_message': error_message}
#                     return render(request, 'take_attendance.html', context)

#                 captured_image_path_data = os.path.join("capture_image", trade, str(roll_number))

#                 stored_images_dir = os.path.join("dataSet", trade, str(roll_number),capture_type)

#                 try:
#                     # Check if the directory exists
#                     if not os.path.exists(stored_images_dir):
#                         raise FileNotFoundError(f'The system cannot find the path specified: {stored_images_dir}')

#                     # List all files in the directory
#                     stored_images = [f for f in os.listdir(stored_images_dir) if
#                                      os.path.isfile(os.path.join(stored_images_dir, f))]

#                     # Create a list to store matching results
#                     matching_results = []

#                     # Counters for "Match: Yes" and "Match: No"
#                     match_yes_count = 0
#                     match_no_count = 0

#                     # Iterate through stored images and compare with the captured image
#                     for stored_image in stored_images:
#                         dataset_image_path = os.path.join(stored_images_dir, stored_image)

#                         # Call the function to compare the captured and stored images
#                         matching_result, ssim_index, mse = image_matching(dataset_image_path, captured_image_path_data)

#                         # Append the matching result and image paths to the list
#                         matching_results.append({
#                             'image_path': dataset_image_path,
#                             'result': matching_result,
#                             'ssi': ssim_index,
#                             'mse': mse,
#                         })

#                         # Update the counters based on matching result
#                         if matching_result:
#                             match_yes_count += 1
#                         else:
#                             match_no_count += 1
#                     # point count here 
#                     # Determine attendance status based on match_yes_count
#                     attendance_status = "Present" if match_yes_count > 2 else "Absent"
                    
#                     # if attendance.face_points=='1' and attendance.eye_points=='1' and attendance.voice_points=='1':
#                     #     attendance.attendance_status='Present'
#                     #     attendance_entry.save()
#                     # else:
#                     #     attendance.attendance_status='Absent'
#                     #     attendance_entry.save()
#                     # attendance_date = now.strftime("%Y-%m-%d")

#                     # Check if the status is "Present" before adding or updating data in the CSV file
#                     if attendance_status == "Present":
#                         try:

#                             # registration = Registration.objects.get(trade=trade, roll_number=roll_number)
#                             registration = Registration.objects.filter(roll_number=roll_number, trade=trade).first()
#                             full_name = registration.full_name

#                             # Get public IP address, handle None case 
#                             public_ip_address = request.META.get('HTTP_X_FORWARDED_FOR') 
#                             if not public_ip_address: 
#                                 public_ip_address = "Unknown" 
        
#                             # Save system information to the database 
#                             SystemInfo.objects.create(mac_address=mac_address, public_ip_address=public_ip_address, 
#                                                     local_ip_address=local_ip_address, trade=trade, roll_number=roll_number) 
#                             # Process form data here
                            
#                            # Try to retrieve an existing attendance entry for the current date, trade, and roll number
#                             attendance_entry = Attendance.objects.get(attendance_date=attendance_date, trade_name=trade, roll_number=roll_number)
                            
#                             # Update existing attendance entry
#                             attendance_entry.full_name = full_name 
#                             attendance_entry.attendance_status = attendance_status
#                             # attendance_entry.InTime = timezone.now()  # Assuming you want to update the time as well
#                             attendance_entry.OutTime = timezone.now()  # Assuming you want to update the time as well
#                             attendance_entry.save()


#                         except Attendance.DoesNotExist:
#                             # If no entry exists for the current date, create a new attendance entry
#                             attendance_entry = Attendance(
#                                 trade_name=trade,
#                                 roll_number=roll_number,
#                                 full_name='',  # Update this with the actual full name
#                                 attendance_status=attendance_status,
#                                 attendance_date=attendance_date,
#                                 InTime=timezone.now(),  # Assuming you want to set the current time
#                                 OutTime=timezone.now(),  # Assuming you want to set the current time
#                                 # Populate other fields as needed
#                             )
#                             attendance_entry.save()
#                         # ------logic for images store if user is present ----
#                         date_folder = now.strftime("%d-%m-%Y")
#                         attendance_img_folder = os.path.join("attand_img", trade, str(roll_number), date_folder)
#                         if not os.path.exists(attendance_img_folder):
#                             os.makedirs(attendance_img_folder)

#                         # Count the number of times the user has taken images
#                         image_count = len([f for f in os.listdir(attendance_img_folder) if f.startswith("Intime.")])

#                         # Determine if it's the first, second, or subsequent time
#                         if image_count == 0:
#                             # First time, use Intime.rollnumber.jpg
#                             image_type = "Intime"
#                         else:
#                             # Subsequent times, use Outtime.rollnumber.jpg
#                             image_type = "Outtime"

#                         # Save the captured image to the attendance_img folder
#                         timestamp_for_filename = re.sub(r'[^a-zA-Z0-9]', '_', attendance_date)
#                         destination_filename = f"{image_type}.{str(roll_number)}.{timestamp_for_filename}.jpg"
#                         destination_path = os.path.join(attendance_img_folder, destination_filename)

#                         # Copy the captured image to the attendance_img folder
#                         shutil.copy(captured_image_path, destination_path)
#                         # ---logic over image store
#                         # --logic for same images store in  dataset folder
#                         # Save the captured image to the dataSet folder
#                         stored_images_dir = os.path.join("dataSet", trade, str(roll_number),capture_type)
#                         if not os.path.exists(stored_images_dir):
#                             os.makedirs(stored_images_dir)

#                         destination_path_dataset = os.path.join(stored_images_dir, destination_filename)

#                         # Copy the captured image to the dataSet folder
#                         shutil.copy(captured_image_path, destination_path_dataset)
#                         # logic is over to store image in dataset ----

                        


#                         # --code for store data in database ----

#                         # Prepare data for CSV file
#                         csv_file_path = 'attendance_data.csv'
#                         fieldnames = ['S.no.', 'Trade_name', 'Roll_number', 'Full_Name', 'Attendance_Status',
#                                       'Attendance_date', 'Attendance_Take', 'InTime', 'OutTime']

#                         # Check if the CSV file exists
#                         if os.path.exists(csv_file_path):
#                             # If the file exists, read the existing data to determine the next serial number
#                             with open(csv_file_path, mode='r', newline='') as csv_file:
#                                 reader = csv.DictReader(csv_file)
#                                 existing_data = list(reader)

#                                 # Check if an entry already exists for the same trade, roll number, and date
#                                 existing_entry_index = next((index for index, entry in enumerate(existing_data) if
#                                                              entry['Trade_name'] == trade and
#                                                              entry['Roll_number'] == roll_number and
#                                                              entry['Attendance_date'].split()[0] ==
#                                                              attendance_date.split()[
#                                                                  0]),
#                                                             None)

#                                 if existing_entry_index is not None:
#                                     # Update the existing entry with OutTime
#                                     existing_data[existing_entry_index]['OutTime'] = attendance_date
#                                 else:
#                                     # Increment the serial number based on the number of existing entries
#                                     new_serial_number = len(existing_data) + 1

#                                     # Add a new entry
#                                     new_data = {
#                                         'S.no.': new_serial_number,
#                                         'Trade_name': trade,
#                                         'Roll_number': roll_number,
#                                         'Full_Name': '',  # Update this with the actual full name
#                                         'Attendance_Status': attendance_status,
#                                         'Attendance_date': attendance_date,
#                                         'Attendance_Take': attendance_date,
#                                         'InTime': attendance_date,
#                                         'OutTime': '',
#                                     }

#                                     existing_data.append(new_data)

#                             # Write back to the CSV file
#                             with open(csv_file_path, mode='w', newline='') as csv_file:
#                                 writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#                                 writer.writeheader()
#                                 writer.writerows(existing_data)
#                         else:
#                             # If the file doesn't exist, create a new file and write the header and the new entry
#                             with open(csv_file_path, mode='w', newline='') as csv_file:
#                                 writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#                                 writer.writeheader()

#                                 # Add a new entry
#                                 new_data = {
#                                     'S.no.': 1,
#                                     'Trade_name': trade,
#                                     'Roll_number': roll_number,
#                                     'Full_Name': '',  # Update this with the actual full name
#                                     'Attendance_Status': attendance_status,
#                                     'Attendance_date': attendance_date,
#                                     'Attendance_Take': attendance_date,
#                                     'InTime': attendance_date,
#                                     'OutTime': '',
#                                 }

#                                 writer.writerow(new_data)
#                     else:
#                         absent_message = f"Your face is not recognized. Please try again."
#                         print(absent_message)
#                         context = {
#                             'form': form,
#                             'absent_message': absent_message,
#                         }
#                         # If the student is Absent, redirect to the same page
#                         return render(request, 'take_attendance.html', context)

#                     # Pass the matching results, counts, attendance status, branch, and roll number to the success page
#                     context = {
#                         'captured_image_path_data': captured_image_path_data,
#                         'stored_images_dir': stored_images_dir,
#                         'matching_results': matching_results,
#                         'match_yes_count': match_yes_count,
#                         'match_no_count': match_no_count,
#                         'attendance_status': attendance_status,
#                         'branch_name': trade,
#                         'roll_number': roll_number,
#                         'Attendance_date': attendance_date,
#                         'capture_type': capture_type,
#                     }
#                     return render(request, 'take_attendance.html', context)
#                     # return render(request, 'success_page.html', context)



#                 except FileNotFoundError as e:

#                     error_message = "You are not registered. First register and then get back."

#                     context = {'form': form, 'error_message': error_message}

#                     return render(request, 'take_attendance.html', context)

#                 except TypeError as e:

#                     error_message = f"No faces detected Soo Don't Move your faces and make sure your camera is open . Please try again."

#                     context = {'form': form, 'error_message': error_message}

#                     return render(request, 'take_attendance.html', context)

        
#         return render(request, 'take_attendance.html',
#                       {'form': form, 'mac_address': mac_address, 'local_ip_address': local_ip_address})
#     else:
#         # Redirect to the success_page.html
#         return redirect('success_page')




def take_attendance_view(request):
    form = AttendanceForm()
    mac_address = get_mac_address()
    local_ip_address = socket.gethostbyname(socket.gethostname())
    if mac_address in ALLOWED_MAC_ADDRESSES:

        if request.method == 'POST':
            form = AttendanceForm(request.POST)
            if form.is_valid():
                # Process form data here
                trade = form.cleaned_data['trade']
                roll_number = form.cleaned_data['rollNumber']
                # capture_type = request.POST.get('captureType', 'face')

                # Capture type can be 'face', 'eye', or 'voice'
                capture_type = request.POST.get('captureType')  # Default to face
                
                if capture_type == 'voice':
                    # Record 10-second audio using SpeechRecognition
                    r = sr.Recognizer()
                    with sr.Microphone() as source:
                        print("Recording audio for 10 seconds...")
                        audio_data = r.record(source, duration=10)
                    
                    # Convert audio to text
                    try:
                        text_from_audio = r.recognize_google(audio_data)
                        print(f"Audio Text: {text_from_audio}")
                    except sr.UnknownValueError:
                        return render(request, 'take_attendance.html', {'form': form, 'error_message': "Audio not clear, please try again."})
                    except sr.RequestError:
                        return render(request, 'take_attendance.html', {'form': form, 'error_message': "Could not process audio."})

                    # Define paths for saving audio and text files
                    dataSet_dir = os.path.join("capture_audio", trade, str(roll_number), capture_type)
                    if not os.path.exists(dataSet_dir):
                        os.makedirs(dataSet_dir)

                    # Save the audio file
                    audio_file_path = os.path.join(dataSet_dir, 'audio_recording.wav')
                    with open(audio_file_path, 'wb') as f:
                        f.write(audio_data.get_wav_data())

                    # Save the transcribed text to a file
                    audio_text_file_path = os.path.join(dataSet_dir, 'audio_text.txt')
                    with open(audio_text_file_path, 'w') as f:
                        f.write(text_from_audio)

                    # Define path for the comparison text file
                    stored_images_dir = os.path.join("dataSet", trade, str(roll_number), capture_type)

                    try:
                        # Automatically detect a .txt file in the comparison directory
                        comparison_text_file = None
                        for file in os.listdir(stored_images_dir):
                            if file.endswith(".txt"):
                                comparison_text_file = os.path.join(stored_images_dir, file)
                                break

                        if comparison_text_file:
                            # Read the comparison file content
                            with open(comparison_text_file, 'r') as f:
                                comparison_text = f.read()

                            # Compare the two texts
                            if text_from_audio.strip() == comparison_text.strip():
                                voice_points = '1'
                                message = "Congrats You are Present ! Your Face, Eye and Voice Credential is Successfully Recorded."
                                print("Your Voice matches in our database.")
                               
                                # Get or create the Attendance object
                                attendance, created = Attendance.objects.get_or_create(
                                    trade_name=trade,
                                    roll_number=roll_number,
                                    
                                    
                                )
                            
                                # Update voice points
                                
                               
                                attendance.voice_points = voice_points
                                attendance.attendance_status = 'Present'
                                attendance.save()
                            else:
                                message = "Both text files are different."
                                print("Your Voice is Not match in our database.")
                        else:
                            form = AttendanceForm()
                            message = "Comparison file not found. Please make sure it exists."
                            print(message)
                            
                    except FileNotFoundError:
                        message = "You are not registered. Please register first and get back to you."
                        print(message)

                    # Return context
                    context = {
                        'form': form,
                        'message': message,
                        'audio_text': text_from_audio,
                        'audio_file_path': audio_file_path,
                        'success': True if message == "Both text files are the same." else False,
                    }
                    return render(request, 'take_attendance.html', context)
                print("hy capcture data is **********************************************",capture_type)

                # Present and absent condition where all three point should be 1
                
                # Get the current date and time               
                now = datetime.now()
                attendance_date = now.strftime("%Y-%m-%d")

                # Call the function to capture images for attendance
                captured_image_path = capture_and_compare(trade, roll_number, capture_type)

                if captured_image_path is None:
                    error_message = "No faces detected. Please try again."
                    context = {'form': form, 'error_message': error_message}
                    return render(request, 'take_attendance.html', context)

                captured_image_path_data = os.path.join("capture_image", trade, str(roll_number))

                stored_images_dir = os.path.join("dataSet", trade, str(roll_number),capture_type)

                try:
                    # Check if the directory exists
                    if not os.path.exists(stored_images_dir):
                        raise FileNotFoundError(f'The system cannot find the path specified: {stored_images_dir}')

                    # List all files in the directory
                    stored_images = [f for f in os.listdir(stored_images_dir) if
                                     os.path.isfile(os.path.join(stored_images_dir, f))]

                    # Create a list to store matching results
                    matching_results = []

                    # Counters for "Match: Yes" and "Match: No"
                    match_yes_count = 0
                    match_no_count = 0

                    # Iterate through stored images and compare with the captured image
                    for stored_image in stored_images:
                        dataset_image_path = os.path.join(stored_images_dir, stored_image)

                        # Call the function to compare the captured and stored images
                        matching_result, ssim_index, mse = image_matching(dataset_image_path, captured_image_path_data)

                        # Append the matching result and image paths to the list
                        matching_results.append({
                            'image_path': dataset_image_path,
                            'result': matching_result,
                            'ssi': ssim_index,
                            'mse': mse,
                        })

                        # Update the counters based on matching result
                        if matching_result:
                            match_yes_count += 1
                        else:
                            match_no_count += 1
                    # point count here 
                    # Determine attendance status based on match_yes_count
                    attendance_status = "Present" if match_yes_count > 2 else "Absent"
                    
                    # if attendance.face_points=='1' and attendance.eye_points=='1' and attendance.voice_points=='1':
                    #     attendance.attendance_status='Present'
                    #     attendance_entry.save()
                    # else:
                    #     attendance.attendance_status='Absent'
                    #     attendance_entry.save()
                    # attendance_date = now.strftime("%Y-%m-%d")

                    # Check if the status is "Present" before adding or updating data in the CSV file
                    if attendance_status == "Present":
                        try:

                            # registration = Registration.objects.get(trade=trade, roll_number=roll_number)
                            registration = Registration.objects.filter(roll_number=roll_number, trade=trade).first()
                            full_name = registration.full_name

                            # Get public IP address, handle None case 
                            public_ip_address = request.META.get('HTTP_X_FORWARDED_FOR') 
                            if not public_ip_address: 
                                public_ip_address = "Unknown" 
        
                            # Save system information to the database 
                            SystemInfo.objects.create(mac_address=mac_address, public_ip_address=public_ip_address, 
                                                    local_ip_address=local_ip_address, trade=trade, roll_number=roll_number) 
                            # Process form data here
                            
                           # Try to retrieve an existing attendance entry for the current date, trade, and roll number
                            attendance_entry = Attendance.objects.get(attendance_date=attendance_date, trade_name=trade, roll_number=roll_number)
                            attendance_status = "Absent"
                            # Update existing attendance entry
                            attendance_entry.full_name = full_name 
                            attendance_entry.attendance_status = attendance_status
                            # attendance_entry.InTime = timezone.now()  # Assuming you want to update the time as well
                            attendance_entry.OutTime = timezone.now()  # Assuming you want to update the time as well
                            attendance_entry.save()


                        except Attendance.DoesNotExist:
                            # If no entry exists for the current date, create a new attendance entry
                            attendance_entry = Attendance(
                                trade_name=trade,
                                roll_number=roll_number,
                                full_name='',  # Update this with the actual full name
                                attendance_status=attendance_status,
                                attendance_date=attendance_date,
                                InTime=timezone.now(),  # Assuming you want to set the current time
                                OutTime=timezone.now(),  # Assuming you want to set the current time
                                # Populate other fields as needed
                            )
                            attendance_entry.save()
                        # ------logic for images store if user is present ----
                        date_folder = now.strftime("%d-%m-%Y")
                        attendance_img_folder = os.path.join("attand_img", trade, str(roll_number), date_folder)
                        if not os.path.exists(attendance_img_folder):
                            os.makedirs(attendance_img_folder)

                        # Count the number of times the user has taken images
                        image_count = len([f for f in os.listdir(attendance_img_folder) if f.startswith("Intime.")])

                        # Determine if it's the first, second, or subsequent time
                        if image_count == 0:
                            # First time, use Intime.rollnumber.jpg
                            image_type = "Intime"
                        else:
                            # Subsequent times, use Outtime.rollnumber.jpg
                            image_type = "Outtime"

                        # Save the captured image to the attendance_img folder
                        timestamp_for_filename = re.sub(r'[^a-zA-Z0-9]', '_', attendance_date)
                        destination_filename = f"{image_type}.{str(roll_number)}.{timestamp_for_filename}.jpg"
                        destination_path = os.path.join(attendance_img_folder, destination_filename)

                        # Copy the captured image to the attendance_img folder
                        shutil.copy(captured_image_path, destination_path)
                        # ---logic over image store
                        # --logic for same images store in  dataset folder
                        # Save the captured image to the dataSet folder
                        stored_images_dir = os.path.join("dataSet", trade, str(roll_number),capture_type)
                        if not os.path.exists(stored_images_dir):
                            os.makedirs(stored_images_dir)

                        destination_path_dataset = os.path.join(stored_images_dir, destination_filename)

                        # Copy the captured image to the dataSet folder
                        shutil.copy(captured_image_path, destination_path_dataset)
                        # logic is over to store image in dataset ----

                        


                        # --code for store data in database ----

                        # Prepare data for CSV file
                        csv_file_path = 'attendance_data.csv'
                        fieldnames = ['S.no.', 'Trade_name', 'Roll_number', 'Full_Name', 'Attendance_Status',
                                      'Attendance_date', 'Attendance_Take', 'InTime', 'OutTime']

                        # Check if the CSV file exists
                        if os.path.exists(csv_file_path):
                            # If the file exists, read the existing data to determine the next serial number
                            with open(csv_file_path, mode='r', newline='') as csv_file:
                                reader = csv.DictReader(csv_file)
                                existing_data = list(reader)

                                # Check if an entry already exists for the same trade, roll number, and date
                                existing_entry_index = next((index for index, entry in enumerate(existing_data) if
                                                             entry['Trade_name'] == trade and
                                                             entry['Roll_number'] == roll_number and
                                                             entry['Attendance_date'].split()[0] ==
                                                             attendance_date.split()[
                                                                 0]),
                                                            None)

                                if existing_entry_index is not None:
                                    # Update the existing entry with OutTime
                                    existing_data[existing_entry_index]['OutTime'] = attendance_date
                                else:
                                    # Increment the serial number based on the number of existing entries
                                    new_serial_number = len(existing_data) + 1

                                    # Add a new entry
                                    new_data = {
                                        'S.no.': new_serial_number,
                                        'Trade_name': trade,
                                        'Roll_number': roll_number,
                                        'Full_Name': '',  # Update this with the actual full name
                                        'Attendance_Status': attendance_status,
                                        'Attendance_date': attendance_date,
                                        'Attendance_Take': attendance_date,
                                        'InTime': attendance_date,
                                        'OutTime': '',
                                    }

                                    existing_data.append(new_data)

                            # Write back to the CSV file
                            with open(csv_file_path, mode='w', newline='') as csv_file:
                                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                                writer.writeheader()
                                writer.writerows(existing_data)
                        else:
                            # If the file doesn't exist, create a new file and write the header and the new entry
                            with open(csv_file_path, mode='w', newline='') as csv_file:
                                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                                writer.writeheader()

                                # Add a new entry
                                new_data = {
                                    'S.no.': 1,
                                    'Trade_name': trade,
                                    'Roll_number': roll_number,
                                    'Full_Name': '',  # Update this with the actual full name
                                    'Attendance_Status': attendance_status,
                                    'Attendance_date': attendance_date,
                                    'Attendance_Take': attendance_date,
                                    'InTime': attendance_date,
                                    'OutTime': '',
                                }

                                writer.writerow(new_data)
                    else:
                        absent_message = f"Please don't move your face while capturing. Please try again."
                        print(absent_message)
                        context = {
                            'form': form,
                            'absent_message': absent_message,
                        }
                        # If the student is Absent, redirect to the same page
                        return render(request, 'take_attendance.html', context)

                    # Pass the matching results, counts, attendance status, branch, and roll number to the success page
                    context = {
                        'captured_image_path_data': captured_image_path_data,
                        'stored_images_dir': stored_images_dir,
                        'matching_results': matching_results,
                        'match_yes_count': match_yes_count,
                        'match_no_count': match_no_count,
                        'attendance_status': attendance_status,
                        'branch_name': trade,
                        'roll_number': roll_number,
                        'Attendance_date': attendance_date,
                        'capture_type': capture_type,
                        
                    }
                    return render(request, 'take_attendance.html', context)
                    # return render(request, 'success_page.html', context)



                except FileNotFoundError as e:

                    error_message = "You are not registered. First register and then get back."

                    context = {'form': form, 'error_message': error_message}

                    return render(request, 'take_attendance.html', context)

                except TypeError as e:

                    error_message = f"No faces detected Soo Don't Move your faces and make sure your camera is open . Please try again."

                    context = {'form': form, 'error_message': error_message}

                    return render(request, 'take_attendance.html', context)


        
        return render(request, 'take_attendance.html',
                      {'form': form, 'mac_address': mac_address, 'local_ip_address': local_ip_address})
    else:
        # Redirect to the success_page.html
        return redirect('success_page')







@login_required
def show_attendance_view(request):
    mac_address = get_mac_address()
    local_ip_address = socket.gethostbyname(socket.gethostname())

    if mac_address in ALLOWED_MAC_ADDRESSES:
        print("Welcome to the attendance system")
        # Render the index.html template
        if request.method == 'POST':
            form = ShowAttendanceForm(request.POST)
            if form.is_valid():
                trade = form.cleaned_data['trade']
                roll_number = form.cleaned_data['rollNumber']

                # Read data from the CSV file
                csv_file_path = 'attendance_data.csv'
                data = []

                with open(csv_file_path, mode='r', newline='') as csv_file:
                    reader = csv.DictReader(csv_file)
                    for row in reader:
                        data.append(row)

                # Filter data based on trade and roll_number
                matching_entries = [entry for entry in data if
                                    entry['Trade_name'] == trade and entry['Roll_number'] == roll_number]

                # Render the response with the matching data
                context = {
                    'matching_entries': matching_entries,
                    'mac_address': mac_address,
                    'local_ip_address': local_ip_address,
                }
                return render(request, 'show_attendance.html', context)

        else:
            form = ShowAttendanceForm()

        context = {
            'form': form,
            'mac_address': mac_address,
            'local_ip_address': local_ip_address,
        }
        return render(request, 'show_attendance.html', context)
    else:
        # Redirect to the success_page.html or handle unauthorized access differently
        return redirect('success_page')


def success_page(request):
    return render(request, 'success_page.html')


# -----new code is here ----
@login_required
def admin_register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'admin_register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('admin_dashboard')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'admin_login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('index')


def success(request):
    return render(request, 'success_page.html')


@login_required
def admin_dashboard(request):
    # Path to the CSV file
    csv_file = 'attendance_data.csv'

    # Dictionary to store counts per trade
    trade_user_counts = defaultdict(set)

    # Open the CSV file and iterate through each row
    with open(csv_file, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if 'Attendance_Status' in row and row['Attendance_Status'] == 'Present':
                trade = row.get('Trade_name', '')
                roll_number = row.get('Roll_number', '')

                if trade and roll_number:
                    trade_user_counts[trade].add(roll_number)

                    # Convert the set of roll numbers to count the registered users
    for trade, roll_numbers in trade_user_counts.items():
        trade_user_counts[trade] = len(roll_numbers)

        # Convert the defaultdict to a list of dictionaries for template rendering
    trade_user_counts_list = [{'Trade_name': trade, 'Registered_Users': users}
                              for trade, users in trade_user_counts.items()]
    user_authenticated = request.user.is_authenticated
    username = request.user.username if user_authenticated else None
    # Pass data to template
    context = {'trade_user_counts': trade_user_counts_list,
               'username': username,
               }
    return render(request, 'admin_dashboard.html', context)


def login_redirect(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        return redirect(request.GET.get('next', 'login'))


def internet_failure(request):
    return render(request, 'internet_failure.html')


def reconnect(request):
    # Here you can add any logic to try to reconnect to the internet
    # For demonstration, let's redirect back to the index page
    return redirect('index')


def custom_page_not_found(request, exception):
    return render(request, '404.html', status=404)

def custom_permission_denied_view(request, exception):
    return render(request, '403.html', status=403)

def no_location_access(request):
    return render(request, 'no_location_access.html')

