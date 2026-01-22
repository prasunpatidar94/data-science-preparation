Verify:

python --version

🔹 2. Create Project Folder
mkdir ds-project
cd ds-project

🔹 3. Create Virtual Environment
python -m venv venv


Activate:

Windows

venv\Scripts\activate


macOS / Linux

source venv/bin/activate

🔹 4. Install Jupyter + Kernel
pip install notebook ipykernel

🔹 5. Register Kernel (IMPORTANT)
python -m ipykernel install --user --name ds-venv --display-name "Python (ds-venv)"

🔹 6. Start Jupyter Notebook
jupyter notebook


Select kernel:

Kernel → Change Kernel → Python (ds-venv)

✅ Verification (Must Do)

Run in notebook:

import sys
sys.executable


✔ Should point to ds-project/venv/...

🧠 Recommended Python Packages (Data Science)
pip install numpy pandas matplotlib seaborn scikit-learn jupyterlab
