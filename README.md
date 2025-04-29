# 📦 DeepAccel: Smart ML Graph Optimizer & Compiler

DeepAccel is a lightweight Python+Flask web app that allows users to upload PyTorch or TensorFlow models, optimize their compute graphs, and download faster, low-latency versions. Built to showcase real-world compiler techniques, this project demonstrates compute graph simplification, benchmarking, and user-centric model transformation.

---

## 👩‍💻 Tech Stack used to build DeepAccel
- Python 3.10
- Flask
- PyTorch
- TensorFlow
- CSS
- HTML

![Screenshot (394)](https://github.com/user-attachments/assets/1763d26c-4daf-47a8-ae43-8b082c97d2d9)


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
