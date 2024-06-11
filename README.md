## AI-powered Human Detection for Enhanced Workplace Safety

**Project Overview:**

This project tackles a critical safety challenge in industries: accidental human entry into restricted areas. It proposes a real-time human detection system using computer vision and artificial intelligence (AI).

**Problem Statement:**

Unintentional human presence in restricted zones poses a significant safety risk. These areas often contain hazardous machinery, electrical equipment, or other environmental dangers. Traditional methods like physical barriers, signage, and manual monitoring have limitations, and a more robust and automated approach is necessary.

**Solution:**

This project implements a real-time human detection system with the following functionalities:

* **Camera monitoring:** Designated restricted areas are continuously monitored by strategically positioned cameras.
* **User-defined ROI:** Users define the specific restricted zone (Region of Interest) within the camera frame.
* **AI-powered detection:** Pre-trained models and computer vision techniques analyze the video feed, focusing on the defined ROI, to detect human presence.
* **Alerts and actions:** Upon human detection, alerts like sirens or flashing lights warn personnel. In critical situations, the system can trigger safety measures like machine shutdowns to prevent accidents.

**Benefits:**

* **Enhanced safety:** Real-time detection and alerts significantly reduce the risk of accidents and injuries.
* **Improved efficiency:** Early detection minimizes downtime and potential damage caused by accidents.
* **Promotes safety culture:** The system's presence fosters a safety-conscious environment.
* **Cost-effective:** Compared to traditional methods, this AI-based solution is relatively inexpensive to set up and maintain.
* **Scalable and adaptable:** The system can be easily scaled to cover multiple restricted areas and adapted to different environments.

**Getting Started:**

This repository contains the source code for the human detection system. To run the project, ensure you have the following:

* Python 3.x
* OpenCV library (install using `pip install opencv-python`)
* A pre-trained human detection model (e.g., HOG + SVM)

**Instructions:**

1. Clone this repository.
2. Install required libraries (`pip install -r requirements.txt`).
3. Download a pre-trained human detection model and place it in the project directory (refer to the chosen model's documentation for download instructions).
4. Modify the code (if needed) to specify the path to the pre-trained model file.
5. Run the program using `python main.py`.

**Further Development:**

* Explore integrating the system with hardware components like cameras and buzzer systems.
* Investigate the use of deep learning models for potentially higher detection accuracy.
* Consider incorporating audio or thermal cameras for handling challenging lighting conditions.

**Disclaimer:**

This project is for educational purposes only. It is recommended to consult with safety professionals and integrate the system with appropriate safety measures in real-world deployments.

We welcome contributions and improvements to this project!
