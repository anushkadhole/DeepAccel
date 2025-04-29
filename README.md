# 📦 DeepAccel: Smart ML Graph Optimizer & Compiler

DeepAccel is a lightweight Python+Flask web app that allows users to upload PyTorch (`.pt`) or TensorFlow (`.pb`) models, optimize their compute graphs, and download faster, low-latency versions. Built to showcase real-world compiler techniques, this project demonstrates compute graph simplification, benchmarking, and user-centric model transformation.

---

## 🌟 Key Features

✅ Upload ML models (.pt or .pb) via web UI  
✅ PyTorch graph optimization using `torch.jit.optimize_for_inference`  
✅ Benchmark before vs. after inference speed  
✅ TensorFlow model compatibility (SavedModel format)  
✅ Optimized model download link  
✅ Deployed using Flask (locally or on Render)

---

## 🎯 Impact on Users
- **Researchers** can streamline model inference tests.
- **ML engineers** save time testing optimizations.
- **Students** explore compiler-like transformations.

---

## 📤 Upload and Test
1. Go to the site
2. Upload a PyTorch `.pt` file or TensorFlow `.pb` model (e.g. SavedModel folder zipped)
3. DeepAccel:
   - Optimizes the model
   - Benchmarks speedup
   - Lets you download the optimized version

---

## ☁️ Deploy on GitHub + Render (Live Hosting)

### Step 1: Push Project to GitHub
```bash
git init
git add .
git commit -m "Initial DeepAccel Commit"
git branch -M main
git remote add origin https://github.com/yourusername/DeepAccel.git
git push -u origin main
```

### Step 2: Deploy to [Render.com](https://render.com)
1. Sign in to [render.com](https://render.com)
2. Click **"New +" ➝ Web Service**
3. Connect your **GitHub repo**
4. Choose:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python app.py`
5. Set **Python version** in Render environment to `3.10`
6. Click **Deploy**

✅ In ~1 min, your DeepAccel app will be live with a public URL!

---

## 🧪 Sample Files to Test
- PyTorch `.pt`: [Download here](https://github.com/pytorch/examples/blob/main/mnist/model.pt?raw=true)
- TensorFlow `.pb`: [Download here](https://storage.googleapis.com/download.tensorflow.org/models/tflite_11_05_08/mobilenet_v2_1.0_224_savedmodel.zip)

---

## 👩‍💻 Built With
- Python 3.10
- Flask
- PyTorch
- TensorFlow
- Jinja2 (for HTML templates)

---

## 📄 License
MIT License. Fork freely and contribute!

---

## ✨ Contribute
Pull requests are welcome! For major changes, open an issue first.

---

## 🙌 Acknowledgments
This project was built to demonstrate ML compiler techniques in a beginner-friendly web app.

---
