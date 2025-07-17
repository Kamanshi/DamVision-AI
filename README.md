💧 DamVision AI
"DamVision AI" is an intelligent dam water management system built using Machine Learning and Streamlit.  

➡️It aims to assist dam authorities in managing water release decisions based on rainfall and reservoir levels, ensuring efficient and safe operation of dams. It intelligently predicts water release based on real-time rainfall and reservoir data, simulates dam gate operations, alerts on high-risk conditions, and visualizes historical trends—all in one beautiful dashboard.
1. Enter rainfall amount and how full the dam is (called reservoir capacity).
2. The AI predicts how much water should be released from the dam (in cusec).

3. Based on that, it suggests:
**whether to keep the gates closed.
**or open partially.
**or open fully.

🚀 Features

- 🌧 *Live Rainfall Animation* – Real-time visual feedback on rainfall intensity.
- 🚢 *Dam Gate Simulation* – Simulated gate levels based on predicted water release.
- 🤖 *AI-Based Predictions* – Uses a trained ML model to predict water release (in cusec) from rainfall and reservoir capacity.
- 📊 *Rainfall vs Release Chart* – Bar chart comparison between input rainfall and predicted release.
- 📈 *Historical Data Visualization* – Shows past trends of rainfall, water level, and release using interactive graphs.
- 🔔 *Risk Alert Audio* – Plays an alert sound when dam gate opening exceeds 80% (indicating high risk).
- 🎛 *Simulation Controls* – User-controlled rainfall and reservoir capacity inputs.

🛠 Technologies Used

- *Python 3*
- *Streamlit* – for web app UI
- *scikit-learn* – ML model training (Linear Regression)
- *Plotly* – Interactive charts and visualizations
- *pandas* – Data handling and processing
- *joblib* – Model serialization
- *pyttsx3* – Text-to-speech for alert 
- *VS Code* – Development Environment

⚙ How It Works

1. *Model Training*  
   The ML model is trained on historical rainfall, reservoir, and release data using linear regression.

2. *Prediction Logic*  
   Based on user input (rainfall + capacity), the app predicts water release and gives a dam gate control decision.

3. *Visualization*  
   Interactive charts and animations help users understand trends and real-time effects of decisions.

4. *Alert System*  
   If the predicted gate opening is above 80%, an audio alert notifies users of high-risk scenarios.

5. *Smart Decision Engine* 
   Suggests dam gate control levels to manage water efficiently and prevent flooding.

6. *Historical Data Visualization* 
   Plots trends of rainfall, water release, and reservoir levels over time.

7. *Simulation Controls* 
   Easy-to-use sliders for setting rainfall and capacity levels during simulation. 

🛠 How to Run

* Clone the repository:
   ```bash
   git clone https://github.com/your-username/damvision-ai.git
   cd damvision-ai     

👩‍💻 Developed By

Kamanshi Saini
B.Tech – Artificial Intelligence & Machine Learning (2nd Year)  
Intern | DAM Internship Project 2025

🔗 Connect with Me

- [🔗 LinkedIn](https://www.linkedin.com/in/your-profile)
- [💻 GitHub](https://github.com/your-username)
- 📧 Email: your.email@example.com

🎓 Project submitted as part of internship under the theme of "Water Resource Management using AI".