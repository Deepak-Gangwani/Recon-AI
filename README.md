# Recon-AI: Developed in Alignment with IBM Guidelines ![image](https://github.com/user-attachments/assets/72e035a4-62da-4a27-91d2-7e4bca470511)

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

Reviewed literature underscores the importance of multi-modal biometric systems like the Recon AI System in addressing modern security challenges. With enhanced precision and resilience, this system represents a significant step forward in biometric authentication technology, offering a powerful solution for both individuals and organizations seeking to protect valuable data and assets.



![fc71635c7f1b09ed30413f59bb749582](https://github.com/user-attachments/assets/3f9ca90e-187e-456a-8d66-d63b51aff854)

### 🔑 Key Features

- **Simulated Data Ingestion**: Reads machine data every 10 seconds.
- **REST API Endpoints**: Fetch processed data and update machine status.
- **Data Analytics**: Provides insights like average, max, min, and anomaly detection.

---

<div align="center">
    <img src="https://user-images.githubusercontent.com/your_username/machine-data-gif.gif" width="600" alt="Machine Data Monitoring in Action" />
    <p>Machine Data Monitoring - Ingestion & Analytics Workflow</p>
</div>

---

## 🛠️ Project Structure

```plaintext
Ingestion-Api-Analytics-Task/
├── app.py                # Flask API server
├── data.json             # Sample json file
├── ingestion.py          # Data ingestion and processing
├── analytics.py          # Data analytics functions
├── README.md             # Project documentation
├── requirements.txt      # Dependencies
└── templates/            # Folder for HTML templates
    └── index.html        # Main HTML template file
```

## 📝 Project Implementation

### 🛠️ Task 1: Data Ingestion & Processing

#### Description:
In this task, a Python script is developed to simulate the continuous stream of machine data (including parameters such as temperature, speed, and status). The script is designed to read this data every 10 seconds from a specified JSON file or a mocked endpoint.

![1_ebmDMPXU9xqgwqdob0XbKQ-ezgif com-crop](https://github.com/user-attachments/assets/b0ff241a-9e49-4a05-b4ad-26a294fb7125)

###### Key Features:
- Data Reading: The script reads machine data at regular intervals (every 10 seconds).
- Data Transformation: It calculates a moving average for each parameter over the last five readings, providing insights into the machine's performance.
- Output Format: The transformed data is printed in JSON format for easy readability and further processing.
  
##### Evaluation Criteria:
- Code clarity and simplicity to ensure maintainability.
- Correct implementation of moving average calculation to ensure accuracy.
- Efficient use of Python’s standard libraries to optimize performance.

### 🌐 Task 2: Basic REST API Development
#### Description:
This task involves building a simple REST API using Flask that exposes two key endpoints.

![RESTAPI](https://github.com/user-attachments/assets/78448e0b-d8ac-411b-98c5-2776d4b7f58e)

##### Endpoints:
- [GET] /data: Returns the processed machine data as JSON, allowing clients to retrieve the latest calculated metrics.
- [POST] /status: Enables updating the machine's job status (e.g., “STARTED”, “COMPLETED”). This helps keep track of the machine's operational state.
  
##### Requirements:
- Input validation for the /status endpoint to ensure only acceptable statuses are processed.
- Management of machine status updates in memory for quick access and manipulation.
  
##### Evaluation Criteria:
- Ability to set up a basic Flask API structure.
- Proper input validation and error handling to enhance robustness.
- Well-organized code to improve readability and maintainability.


### 🛠️ Procedure to Run the Project of Task-1 and Task-2
#### Prerequisites
Before you begin, ensure you have the following installed on your local machine:
- Python 3.x: Make sure you have Python installed. You can download it from the official Python website.
- pip: This package manager for Python should come with the Python installation.
- Flask: A web framework for building the REST API. You can install it using pip.

![Machine-Data-Dashboard-ezgif com-crop](https://github.com/user-attachments/assets/42ea5018-5cfa-4241-9ecd-3406ffe4b4dc)
  
#### Step-by-Step Instructions
- Clone the Repository: Clone this repository to your local machine using the following command:
```
git clone https://github.com/Deepak-Gangwani/Ingestion-Api-Analytics-Task.git

```

- Navigate to the Project Directory: Change your working directory to the project folder:
```
cd Ingestion-Api-Analytics-Task

```

- Install Required Packages: Use pip to install the necessary Python packages. Make sure you're in the project directory:
```
pip install -r requirements.txt

```
- Create the Sample Data File: Ensure you have a data.json file in the project directory. This file should contain the simulated machine data. You can create it with the following sample content:
```
[
    {"timestamp": "2024-10-27T12:00:00", "temperature": 70, "speed": 30, "status": "RUNNING"},
    {"timestamp": "2024-10-27T12:00:10", "temperature": 72, "speed": 32, "status": "RUNNING"},
    {"timestamp": "2024-10-27T12:00:20", "temperature": 75, "speed": 34, "status": "RUNNING"},
    {"timestamp": "2024-10-27T12:00:30", "temperature": 71, "speed": 29, "status": "RUNNING"},
    {"timestamp": "2024-10-27T12:00:40", "temperature": 74, "speed": 33, "status": "RUNNING"},
    {"timestamp": "2024-10-27T12:00:50", "temperature": 76, "speed": 35, "status": "RUNNING"},
    {"timestamp": "2024-10-27T12:01:00", "temperature": 78, "speed": 36, "status": "RUNNING"}
]

```

- Run the Flask API: Open a new terminal window and navigate to the project directory. Start the Flask server with the following command:

```
  python app.py
```
 (Replace app.py with the name of your Flask application file if it differs.)

- Run the Data Ingestion Script: In another terminal window (keeping the Flask server running), navigate to the project directory again and execute the ingestion script:
```
  python ingestion.py

```
- View the Output: As the ingestion script runs, it will read the data from the data.json file, compute the moving averages, and send the data to the Flask API. You should see the calculated moving averages printed in the terminal and the responses from the API.

#### Troubleshooting
- If you encounter any errors: Check that all dependencies are installed and that the data.json file is correctly formatted.
- Ensure Flask is running before executing the ingestion script to avoid connection errors.

```
http://127.0.0.1:5000/
http://127.0.0.1:5000/data
http://127.0.0.1:5000/status
```

#### Diagram Representation of deque
Here's a simple diagram to illustrate how deque operates in the context of this code:

```
Initial State: (maxlen=5)
---------------------------------
|   |   |   |   |   |    (empty)
---------------------------------
Add: 30, 32, 31, 29
---------------------------------
| 30| 32| 31| 29|   |    
---------------------------------
Add: 35 (exceeds maxlen, removes 30)
---------------------------------
| 32| 31| 29| 35|   |    
---------------------------------
Add: 36 (exceeds maxlen, removes 32)
---------------------------------
| 31| 29| 35| 36|   |    
---------------------------------

```
In this diagram:
- The deque can hold a maximum of 5 items.
- When a new item is added beyond this limit, the oldest item (leftmost) is removed automatically.
- This allows efficient management of the last window_size readings for calculations.
  
Summary
The deque in this code is crucial for managing the last few readings of temperature and speed efficiently, enabling quick calculations of moving averages while ensuring minimal memory overhead.


### 📈 Task 3: Simple Data Analytics

#### Description:
In this final task, a Python function is implemented to perform data analytics on the machine data. The function reads a list of timestamps and values (e.g., machine speed) and calculates various statistics.

![images](https://github.com/user-attachments/assets/63adfb89-9fde-4077-a2c8-66427d343b0e)

##### Calculations:
- Average Value: Computes the average of the collected data over the entire period.
- Maximum and Minimum Values: Identifies the peak and lowest readings for performance monitoring.
  
##### Bonus Feature:
If time permits, the candidate can extend the function to detect anomalies—specifically, any values that deviate by more than 20% from the calculated average. This enhances the functionality by providing early warning indicators for potential issues.

![outlier2](https://github.com/user-attachments/assets/040d077e-3939-4159-b9c9-59e1ef5e16df)

##### Evaluation Criteria:
- Accuracy of calculations to ensure reliable data analytics.
- Code efficiency and readability to facilitate future modifications.
- Bonus points awarded for implementing anomaly detection, adding extra value to the solution.


To guide users on how to run the analytics.py script to see anomalies, minimum, and maximum values from the sample machine data, you can add the following instructions to your README file:

### 📊 Running the Analytics Script of Task-3
After processing the machine data with the ingestion script, you can run the analytics.py script to analyze the data for anomalies, minimum, and maximum values. Follow the steps below to execute the analytics script:

##### Step-by-Step Instructions
- Run the Analytics Script: In the terminal, while still in the project directory, execute the analytics.py script using the following command:
- View the Output: After running the script, you will see the following results printed in the terminal:
    -- Average Value: The mean value calculated from all readings.
    -- Maximum Value: The highest value recorded in the dataset.
    -- Minimum Value: The lowest value recorded in the dataset.
    -- Anomalies: Any readings that deviate by more than 20% from the average value will be identified and displayed, based on the values you provide.

![Analytics-image](https://github.com/user-attachments/assets/a96ab195-5b11-47a8-a547-f9f939376679)
  
##### Example Output
You can expect the output to look something like this in terminal while running the file:
```
{
  "average": 32.4,
  "max": 50,
  "min": 29,
  "anomalies": [50]
}
```


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
### Step 7: Finalize and Test
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
