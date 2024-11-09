# 🚀 **Recon-AI** 🚀  
### Developed in Alignment with IBM Guidelines

![Recon-AI Logo](https://github.com/user-attachments/assets/72e035a4-62da-4a27-91d2-7e4bca470511)

![Python](https://img.shields.io/badge/Python-3.6%2B-blue)
![Django](https://img.shields.io/badge/Django-3.2%2B-green)
![API](https://img.shields.io/badge/API-REST-orange)
![Deep Learning](https://img.shields.io/badge/Deep%20Learning-TensorFlow-lightgrey)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Scikit%20Learn-lightblue)
![Computer Vision](https://img.shields.io/badge/Computer%20Vision-OpenCV-brightgreen)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange)
![Keras](https://img.shields.io/badge/Keras-2.x-red)
![SciPy](https://img.shields.io/badge/SciPy-1.5%2B-blue)
![Socket.io](https://img.shields.io/badge/Socket.io-4.x-black)
![HTML](https://img.shields.io/badge/HTML-5-orange)
![CSS](https://img.shields.io/badge/CSS-3-blue)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6%2B-yellow)
![jQuery](https://img.shields.io/badge/jQuery-3.5.1-blue)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.1-purple)
![Anti Spoofing](https://img.shields.io/badge/Anti%20Spoofing-Face%20Liveness-red)
![Ultralytics](https://img.shields.io/badge/Ultralytics-YOLOv5-lightgrey)


## 📖 Project Overview

**The Recon AI System** is an innovative solution in biometric authentication, integrating advanced technologies for face, voice, and iris recognition. In response to the ever-evolving landscape of security threats, this multi-modal approach provides a robust and highly secure authentication method. By combining multiple biometric modalities, the system achieves a high degree of accuracy and reliability, essential for safeguarding sensitive information and ensuring that access is restricted to authorized users only.    

In addition to biometric authentication, the Recon AI System utilizes location-based security measures, including MAC address, IP address, and geographical data (longitude and latitude), further enhancing its protective capabilities. These additional security layers ensure that system access is limited to pre-approved locations, adding an extra safeguard against unauthorized access.

![recognition-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/81c623a6-65da-4e0e-b9f0-663ef5c7c428)

Reviewed literature underscores the importance of multi-modal biometric systems like the Recon AI System in addressing modern security challenges. With enhanced precision and resilience, this system represents a significant step forward in biometric authentication technology, offering a powerful solution for both individuals and organizations seeking to protect valuable data and assets.


### 🔑 Key Features of Multi Layered Authentication

- **Face Recognition Layer**: Reads machine data every 10 seconds.
- **Iris Identification Layer**: Fetch processed data and update machine status.
- **Voice Identification**: Provides insights like average, max, min, and anomaly detection.

---

<div align="center">
    <img src="https://user-images.githubusercontent.com/your_username/machine-data-gif.gif" width="600" alt="Machine Data Monitoring in Action" />
    <p>Complete Project Workflow and Demo</p>
</div>

---

## 🛠️ Project Structure

```plaintext
ATTANDSYSTEM/
├── attand_img
├── attandSystem
├── capture_audio
├── capture_image
├── dataSet
├── deepakenv
├── deepakenv2
├── recon-ai-logo-file
├── systemApp
│   ├── __pycache__
│   ├── middleware
│   ├── migrations
│   ├── static
│   ├── templates
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── haarcascade_eye.xml
│   ├── haarcascade_frontalface_default.xml
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── attendance_data.csv
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md
```

## Design Implementation

- ER Model
 ![image](https://github.com/user-attachments/assets/6d4f2913-0c8b-40a0-bfed-2737fda66b75)

- Facial Recognition
 ![image](https://github.com/user-attachments/assets/fc75fa54-fcd7-4a63-8a9a-2eb1b141fd87)

- Voice Recognition
 ![image](https://github.com/user-attachments/assets/8478972c-e951-4906-b606-a5120ea937fe)

- Iris Recognition
 ![image](https://github.com/user-attachments/assets/b6fa0323-8ee2-4680-afac-e889eec7c58e)

## 📝 Project Implementation

### 🛠️ Task 1: Face Identification Security Layer

#### Task Description:
Develop a Python script to simulate real-time face identification using a security layer. The script should process data continuously, identifying faces through live data feeds (simulated with JSON data or a mocked endpoint). The system will analyze and identify faces at intervals.
![take_attandance](https://github.com/user-attachments/assets/6bfc570c-cd4d-4097-8944-df5f5598a22f)

#### Key Features:
- **Face Data Processing**: Processes and identifies face data at specified intervals.
- **Identification Accuracy**: Uses algorithms to ensure accurate identification of faces in each frame.
- **Output Format**: Outputs face identification results in JSON format, optimized for further processing.

#### Evaluation Criteria:
- **Code Clarity**: Code should be organized and easily understandable for maintenance and scalability.
- **Identification Accuracy**: Algorithms must be optimized to ensure precise face recognition.
- **Performance Optimization**: Efficient handling of live data processing for minimal delay.

---

### 🌐 Task 2: Iris Identification Security Layer

#### Task Description:
Develop a Python program to simulate iris identification as part of a security layer. The program will process iris data and provide functionality for retrieving and updating iris recognition status, ensuring secure and accurate access control.

![eye-scanner](https://github.com/user-attachments/assets/d7a4c8ac-4cf3-4fee-8424-1261869cd846)

#### Key Features:
- **Data Retrieval**: Retrieves processed iris data in JSON format for further processing.
- **Status Update**: Allows for updating the identification status (e.g., “MATCHED,” “NOT MATCHED”) to monitor security status in real-time.
- **Data Security**: Ensures secure handling of sensitive iris data.

#### Evaluation Criteria:
- **Program Structure**: Well-organized code for clarity and maintainability.
- **Data Security**: Handles iris data securely, preserving privacy and accuracy.
- **Robustness**: Effective input validation and error handling for dependable performance.

---

### 📈 Task 3: Voice Identification Security Layer

#### Task Description:
Create a Python program to simulate voice identification as part of a security layer. The program will analyze voice data to perform identification and calculate various metrics to ensure secure and accurate voice recognition.

![voice-gif](https://github.com/user-attachments/assets/c8972cca-162c-4767-8246-f1c06c1106ba)

#### Key Features:
- **Voice Data Processing**: Processes and analyzes voice data to identify individuals accurately.
- **Metric Calculations**: Computes metrics such as frequency analysis, average pitch, and amplitude to support identification accuracy.
- **Output Format**: Provides processed voice identification results in JSON format for efficient data handling.

#### Evaluation Criteria:
- **Program Structure**: Code should be organized and easy to maintain.
- **Identification Accuracy**: Ensures that voice recognition metrics are accurately calculated.
- **Performance Optimization**: Efficient handling of voice data for real-time identification with minimal delay.


## Implementation Details

#### Home Page
The Home Page serves as the initial point of interaction for users visiting the Recon AI System. It is designed to provide an overview of the system's features and guide users to other sections of the website. The page is built using Django, which handles routing and rendering of the content. HTML and CSS are used to create a visually appealing and user-friendly interface, showcasing key features and offering navigation links to other pages. The design ensures that users can quickly understand the purpose of the system and find their way to more detailed information.

![image](https://github.com/user-attachments/assets/6e12f554-45a8-4c7d-acb1-4663b1d6e23a)

 
#### About Our System
The About Our System Page provides a detailed description of the Recon AI System, including its features and underlying technology. It explains how the system integrates face, voice, and iris recognition technologies to enhance security. The content is presented with the aid of diagrams or illustrations to simplify complex technical concepts. This page is crucial for educating users about the system’s capabilities and how it operates.

![image](https://github.com/user-attachments/assets/0ce1ef6b-6fff-4e23-8b25-e2aeff7025a0)

 
#### Notify Me
The Notify Us provides a mechanism for users to report issues or provide feedback about the Recon AI System. Similar to the Contact Page, it features a form managed by Django to collect user submissions. The form is designed to capture specific details about issues or feedback and stores this information securely. Notifications can be configured to alert the development team when new reports are submitted. This page helps in gathering user feedback and improving the system based on real-world usage.

![image](https://github.com/user-attachments/assets/1c59ef97-2eac-4e41-8243-7acefc244621)

 
#### About Me 
The About Us Page offers information about the team or organization behind the Recon AI System. It includes details about team members, their roles, and the mission of the project. This page is crafted using HTML and CSS to present the information in an engaging and structured format. It helps users understand who is behind the system and provides context about the project's goals and vision.

![image](https://github.com/user-attachments/assets/1d680887-171f-40e5-9ce3-3c4d4559cdb3)


 
#### Access Authentication
Implementing access authentication using face, eye, and voice recognition involves capturing and processing biometric data, extracting unique features, and matching them against stored profiles. Each method has its strengths and applications, making them suitable for different security requirements.

![image](https://github.com/user-attachments/assets/f1580c0f-edd6-46b9-b22b-10f8141c4156)

![image](https://github.com/user-attachments/assets/3260c850-5d09-4bba-8d0c-2763a08a6d85)

#### Contact Us
The Contact Page allows users to get in touch with the development team or support staff. This page includes a contact form created with Django, which captures user input such as name, email, and message. Server-side validation is implemented to ensure that the form data is complete and correctly formatted. Once submitted, the contact information can be sent to a designated email address or stored in a database for further follow-up. This page is essential for maintaining communication with users and addressing their inquiries or feedback.

 ![image](https://github.com/user-attachments/assets/8693e1c8-ab66-497b-a1ee-16e7842e7ea8)
 ![image](https://github.com/user-attachments/assets/c5174004-437f-4eb3-bad7-589d1c2cbd74)


#### Admin Panel
The Admin Panel of Recon-Al is a robust, user-friendly interface that centralizes control and management of the biometric security system. It enables administrators to efficiently handle user accounts, including adding, modifying, and removing users, as well as managing biometric data such as facial images, voice samples, and iris scans. The panel offers real-time monitoring of system performance and user activity, customizable reporting and analytics, and alert management for immediate responses to security events. Additionally, it facilitates seamless integration with other security systems, maintains comprehensive audit trails for transparency, and supports routine maintenance and updates. Designed for both efficiency and flexibility, the Admin Panel ensures effective oversight and operational control of the Recon-Al system.

##### Admin Registration and Login Page 
![image1](https://github.com/user-attachments/assets/449d6fd6-599c-4416-b761-a2947d1e7c7d)
![image2](https://github.com/user-attachments/assets/bec2185a-7837-444a-bb1d-f6075fad48ab)


- Client Side Admin Dashboard
![image](https://github.com/user-attachments/assets/6f36a51a-26f1-4cbf-961a-42e4b1724474)

 
- Server Side Admin Dashboard
![image](https://github.com/user-attachments/assets/85a620c8-a6db-459b-85ca-f90849ff77f8)


## Testing
Step 1:- First, you need to fill out the registration form
![image](https://github.com/user-attachments/assets/23074d19-a956-46a1-bdcd-488f8a53e674)

 
Step 2:- First, you need to fill out the form details and look at the camera Do move your face too much for the face recognition registration
![image](https://github.com/user-attachments/assets/bb260fc3-e5bc-4462-bf47-977137df4bd9)
![image](https://github.com/user-attachments/assets/71fc46e1-9f51-4759-aabc-6e0ba5d86de5)


 
Step 3:- Now, for eye recognition, you need to bring your eyes close to the camera and wait until the system shows that the submission was successful
 ![image](https://github.com/user-attachments/assets/1f5a3d38-900c-43ca-a137-232fefe6e25e)

Step 4:- Now, for voice recognition, click on the third step for voice. When the pop-up appears for recording, speak clearly and a bit louder. At the end, the system will show that your voice registration is successful
![image](https://github.com/user-attachments/assets/a701a297-217b-477e-b7a7-a25cdcf171f0)
![image](https://github.com/user-attachments/assets/5a4a3e82-be5e-43bc-9a8f-c9ab50a1e540)

 
Step 5:- Your registration is complete It was done step by step: first, face recognition; then, eye recognition; and finally, voice recognition. Now, you can enter your attendance with just one click using any recognition system by filling out the form details
![image](https://github.com/user-attachments/assets/602c56cf-e7eb-4822-b200-242e504f5dc7)

 
Step 6:- Now the registered user can mark him present for the day.
![image](https://github.com/user-attachments/assets/d8095e3d-7fbe-47f0-8c19-d941af47a0b7)
![image](https://github.com/user-attachments/assets/34474c32-0c2d-47c8-b014-7bb5840f94a1)

 
Step 7:- Face scan is done now registered user has to complete second layer of security which iris scan and eye scan.
![image](https://github.com/user-attachments/assets/f773c980-e7c9-4bfa-899a-1df4a7783275)
![image](https://github.com/user-attachments/assets/2f2864df-ee2a-4bb5-ae72-d322f1400844)

 
Step 8:- Eye scan is done now registered user has to complete third layer of security which voice scan.
![image](https://github.com/user-attachments/assets/a208339a-2a87-49b9-b24b-ea43ab246b09)
![image](https://github.com/user-attachments/assets/964b684f-1bbd-44d3-ad79-496e6e0dbbd8)

 
Step 9:-After scanning all three layer the registered user check in status will be updated to present for the current date.
 
![image](https://github.com/user-attachments/assets/26f55ef9-249f-498a-a0a2-e59fd9d12041)
![image](https://github.com/user-attachments/assets/a48dd8ff-c1f1-4423-9d52-a68d1f4a2ca5)

Step 10:- Your attendance and all the data will be stored in your admin panel with a secure database
![image1](https://github.com/user-attachments/assets/48e29b50-b369-45e1-855d-1f68e2bfe04d)
![image2](https://github.com/user-attachments/assets/39902d16-28de-4940-a289-9abe82153d33)
![image3](https://github.com/user-attachments/assets/d60bf137-8043-4c89-8cb3-46a95f403d24)
![image4](https://github.com/user-attachments/assets/e56cc22e-a20e-4476-80ad-0325215234d9)
![image5](https://github.com/user-attachments/assets/12d26227-9097-458c-9cc4-ce95ea5f2ea4)
![image6](https://github.com/user-attachments/assets/65e9816c-ce5b-42d6-9619-d617aadc6cdc)
![image7](https://github.com/user-attachments/assets/0adbbcf0-3727-4317-b61e-d835971d191f)
![image8](https://github.com/user-attachments/assets/8ae4aad3-06ea-4fa6-8076-ec1e721f4d32)
![image9](https://github.com/user-attachments/assets/956fcc04-e237-4379-bafa-1786d9cbe978)


## Run The Project App Using Poetry Package Manager

1. **Install dependencies**:
```
   poetry install
```
2. Run the application:

```
poetry run python main.py
```

3. Add new dependencies:
```
poetry add flask requests statistics
```

4. Activate the environment:
```
poetry shell
```

5. Exit the environment:
```
exit
```

---
yaml

### Finalize and Test
1. Confirm everything works by cloning the repository on a separate machine or environment.
2. Run `poetry install` to check if all dependencies and configurations are set up correctly.

--- 
#### This setup allows anyone who clones the project to use Poetry for dependency management easily, ensuring a consistent environment across all development setups. Let me know if you need any further help!

## Conclusion 🛡️
**The Recon AI System** represents a significant advancement in biometric authentication technologies, incorporating sophisticated face, voice, and iris recognition capabilities. As security threats continue to evolve, the integration of these advanced biometric modalities offers a robust solution for protecting sensitive information and ensuring secure access. Additionally, the system’s use of MAC address, IP address, longitude, and latitude for security purposes enhances its protective measures, ensuring that only authorized users can access the system from predefined locations. The reviewed literature highlights those multi-modal biometric systems, such as the Recon AI System, mark a pivotal development in addressing contemporary security challenges with enhanced accuracy and reliability.

## Contributing 🤝
We welcome contributions from the community! Your input helps make this project better for everyone. To contribute, please follow these steps:
- Create a Pull Request: Go to the original repository and click the “New Pull Request” button. 
- Provide a detailed description of your changes and submit your pull request.

Thank you for considering contributing to this project! Your efforts are greatly appreciated! 🌟

## License 📄
This project is licensed under the MIT License. This means you are free to use, modify, and distribute the project as long as you include the original license and copyright notice.

## Support 🙋‍♂️
If you have any questions, issues, or suggestions regarding this project, feel free to reach out!

- Open an Issue: If you encounter bugs or have feature requests, please open an issue in the GitHub repository.
- Discussion Forum: Join our Discussion Forum to engage with the community and share ideas.
- Contact Us: You can also reach me directly at deepakgangwani512@gmail.com for any specific inquiries.
  
#### Your feedback is valuable and helps us improve! Thank you for your support! ❤️
