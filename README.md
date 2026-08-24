# Plant Disease Detection
In this project, I have made a web application named PlantGuard AI using python and streamlit.  
It is a plant disease detection application that uses a deep learning model to identify diseases from images of plant leaves.  
The user can upload an image of a plant leaf, and the trained model analyzes the image and predicts the most likely disease.  
The goal of this project is to demonstrate how computer vision and deep learning can be applied to agriculture to assist with early plant disease identification.  

## Dataset Used
The model was trained using the New Plant Disease Dataset(available on Kaggle), which contains RGB images of healthy and diseased plant leaves. 
This dataset contains 3 folders:
1. Train
2. Valid
3. Test  
There are 38 different classes present in this dataset.

## Note
This model is trained on the dataset mentioned above so if user uploads any image which is not a leaf or
does not belongs to a class present in the dataset, it will give random output.  
For eaxmple: User enters an image of a person and the model may say it's healthy corn leaf or something like that.

## Model Evaluation
Training Accuracy achieved: 96.06%  
Validation Accuracy achieved: 91.07%

# Screenshots
1.Home Page
<img width="1907" height="888" alt="Screenshot 2026-08-24 064516" src="https://github.com/user-attachments/assets/21a57102-564c-4515-b381-9d77dfe69c01" />

2. About Page
<img width="1906" height="880" alt="Screenshot 2026-08-24 064603" src="https://github.com/user-attachments/assets/a12d61a8-1345-4e12-a701-dbc07def31a4" />

3. Disease Detection Page
<img width="1917" height="877" alt="Screenshot 2026-08-24 064620" src="https://github.com/user-attachments/assets/68caae3d-d1e0-4d5b-8d41-3f29dc500cc0" />
<img width="1912" height="898" alt="Screenshot 2026-08-24 064656" src="https://github.com/user-attachments/assets/5e76cca1-771d-4f67-97b5-7c60b898b24b" />
<img width="1911" height="878" alt="Screenshot 2026-08-24 064715" src="https://github.com/user-attachments/assets/7b43287e-ab79-4931-8f23-e4406fd10365" />

Try yourself at https://plant-disease-detection-by-nishant-devlal.streamlit.app/
