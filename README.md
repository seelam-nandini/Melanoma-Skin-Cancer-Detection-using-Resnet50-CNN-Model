# Melanoma Skin Cancer Detection using ResNet50 CNN Model
## Introduction
### Overview
The **Melanoma Skin Cancer Detection** project is an advanced machine learning application designed to accurately identify melanoma from skin lesion images. This project leverages state-of-the-art deep learning models, including ResNet50, VGG16, InceptionV3, and MobileNetV2, to achieve high precision in skin cancer detection. The application is deployed using Flask, providing a user-friendly web interface for uploading images and receiving real-time predictions.
### Why ResNet50?
ResNet50 stands out as the optimal model for melanoma skin cancer detection owing to its exceptional performance and efficiency. Achieving an accuracy of **93.17%**, ResNet50 excels in identifying subtle features in skin lesions, which is crucial for distinguishing between benign and malignant conditions.

The model’s deep residual learning architecture effectively addresses the vanishing gradient problem, allowing for the training of deeper networks without performance degradation. Additionally, ResNet50’s computational efficiency makes it well-suited for real-world applications. Its proven track record in medical imaging further underscores its reliability and effectiveness, making it an ideal choice for accurate and dependable melanoma detection.
## Key Features
- **High Accuracy**: Achieved **93.17%** accuracy using ResNet50 Model, ensuring high precision in melanoma detection.
- **Deep Residual Learning**: Utilized residual neural networks to train the model to handle complex image patterns and features.
- **Efficient Computation**: Featured a streamlined architecture for fast and efficient processing.
- **Flask Integration**: Deployed with Flask for an intuitive web interface allowing real-time image uploads and predictions.
- **Comparative Analysis**: Includes performance evaluations of VGG16, InceptionV3, and MobileNetV2 to benchmark ResNet50.

## Data Processing and Model Optimization
- **Data Set**: Utilized a comprehensive dataset from Kaggle, featuring 10,000 diverse images of skin lesions, to ensure extensive coverage of various melanoma types and conditions. The dataset is available at: https://www.kaggle.com/datasets/hasnainjaved/melanoma-skin-cancer-dataset-of-10000-images/data?select=melanoma_cancer_dataset
- **Data Preprocessing**:
  - **Image Resizing**: 
     Resized all images to a standard dimension of 224x224 pixels to ensure uniform input size for the ResNet50 model.
  - **Normalization**:  Scaled pixel values to a range of 0 to 1. 
  - **Augmentation**: Applied techniques such as rotation, flipping, and scaling to enhance the diversity of the training dataset and improve model robustness.
  - **Data Splitting**: Divide the dataset into training (70%), validation (15%), and testing (15%) subsets to evaluate model performance and avoid overfitting.
  - **Batch Processing**: Used batch processing with a batch size of 32 images during training to efficiently handle large datasets and optimize memory usage.
- **Model Optimization**: Utilized advanced techniques such as transfer learning and fine-tuning to enhance ResNet50’s performance and adapt it to the specific task of melanoma detection.

## Model Evaluation
The performance of the ResNet50 model in the melanoma skin cancer detection project was evaluated using the key metrics: accuracy, precision, recall and F1 Score.

These metrics were calculated to assess and compare ResNet50’s performance against other models like VGG16, InceptionV3, and MobileNetV2. This evaluation ensures that ResNet50’s superior accuracy and balanced performance are well-documented, highlighting its effectiveness and reliability in real-world melanoma detection scenarios.

# Deployment with Flask
The melanoma skin cancer detection model has been deployed using Flask, a lightweight WSGI web application framework. The Flask application provides a user-friendly web interface where users can upload skin lesion images and receive real-time predictions from the ResNet50 model.

**Accessing the Flask Application:** 
- Start the Flask server locally by running the command:
  ```bash
  python app.py
- Open your web browser and navigate to http://localhost:5000 to interact with the deployed model.
- Below is a screenshot of the Flask application interface, which allows users to upload skin lesion images for melanoma detection.
