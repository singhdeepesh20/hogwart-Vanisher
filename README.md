# 🧙‍♂️ Hogwart-Vanisher — Real-Life Invisibility Cloak

> Tur your camera into a magical invisibility cloak using Computer Vision.

Hogwart-Vanisher is a fun and interactive AI-powered application that simulates an invisibility cloak effect using OpenCV and Streamlit. Inspired by the Harry Potter universe, the app detects a specific cloak color and replaces it with the captured background — making it appear invisible in real time.

---

## 📌 Overview

This project demonstrates the power of computer vision by transforming a simple webcam feed into an augmented reality experience. By leveraging color detection and background subtraction, Hogwart-Vanisher creates the illusion of invisibility.

It is ideal for learning OpenCV concepts, image masking, and real-time video processing while building a visually engaging project.

---

## ✨ Features

* 🎥 **Background Capture**
  Capture a clean background frame without the subject.

* 🧥 **Cloak-Based Invisibility**
  Replace selected cloak colors with the background.

* 🎨 **Multi-Color Support**
  Works with white, black, red, and blue cloaks.

* ⚡ **Real-Time Processing**
  Instant invisibility effect using live camera feed.

* 🖥️ **Interactive UI**
  Built with Streamlit for an easy-to-use web interface.

---

## 🖥️ How to Use

1. Run the application locally
2. Open in browser:

   ```
   http://localhost:8501
   ```
3. Stand out of the frame and click **Capture Background**
4. Step into the frame holding your cloak
5. Watch the cloak disappear ✨

### Supported Cloak Colors

* ⚪ White (cloth/paper)
* ⚫ Black
* 🔴 Red
* 🔵 Blue

---

## 🛠️ Tech Stack

| Category        | Technology Used |
| --------------- | --------------- |
| Language        | Python          |
| Framework       | Streamlit       |
| Computer Vision | OpenCV          |
| Processing      | NumPy           |
| Imaging         | PIL             |

---

## 📂 Project Structure

```
hogwart-vanisher/
│
├── app.py                # Main Streamlit application
├── utils/                # Image processing utilities
├── assets/               # Sample images (optional)
├── requirements.txt      # Dependencies
└── README.md             # Documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/hogwart-vanisher.git
cd hogwart-vanisher
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\\Scripts\\activate    # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 🧠 How It Works

1. 📸 Capture background frame (without subject)
2. 🎨 Detect cloak color using HSV masking
3. 🧩 Create mask for cloak region
4. 🔄 Replace cloak pixels with background
5. 🎥 Render final output in real time

---

## 📸 Screenshots

*(Add your project screenshots or GIFs here for better engagement)*

---

## 🎯 Use Cases

* 🎓 Learning OpenCV & Computer Vision
* 🧪 Experimenting with AR-like effects
* 🎥 Fun demo projects & hackathons
* 📚 Educational visualization

---

## 🔮 Future Improvements

* 🎬 Real-time video streaming optimization
* 🧠 Adaptive color detection (lighting-aware)
* 🎨 Custom cloak color picker
* 📱 Mobile/web deployment
* 🎥 GIF/video export feature

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a branch (`feature/your-feature`)
3. Commit changes
4. Push to branch
5. Open a Pull Request

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 👤 Author

**Deepesh Singh**
🔗 LinkedIn: [https://www.linkedin.com/in/contactdeepesh](https://www.linkedin.com/in/contactdeepesh)

---

## ⭐ Support

If you like this project, consider giving it a ⭐



