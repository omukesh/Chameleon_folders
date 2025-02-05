# Chameleon_folders

## 📌 Overview
This project automates **folder creation** and **dynamic renaming** for standard organization workflows.

✅ **Features:**
- **`folder_creator.py`**: Creates a structured project folder template with subdirectories.
- **`RT_rename.py`**: Monitors folder renaming and updates all nested subfolders dynamically.

## 🛠 Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/omukesh/Chameleon_folders
   cd Chameleon_folders
2. Install Requirements:
   ```bash
    pip install -r requirements.txt
3. Before Rename

         MVS_ACME/
         │── MVS_ACME_Data/
         │   ├── MVS_ACME_Data_Input/
         │   ├── MVS_ACME_Data_Logs/
         │   ├── MVS_ACME_Data_Output/
         │── MVS_ACME_Reports/
         │   ├── MVS_ACME_Finance/
         │   ├── MVS_ACME_Revenues/
         │   ├── MVS_ACME_Expenditure/
         │── MVS_ACME_Scripts/
         │   ├── MVS_ACME_Robots/
         │   ├── MVS_ACME_PLC/
         │   ├── MVS_ACME_Vision/
         │── MVS_ACME_Resources/
         │   ├── MVS_ACME_Logs/
         │   ├── MVS_ACME_Materials/
         │   ├── MVS_ACME_Business_Cards/

4. After Rename to **Dr_reddys** on the window itself while running RT_rename.py in background

         Dr_reddys/
         │── Dr_reddys_Data/
         │   ├── Dr_reddys_Data_Input/
         │   ├── Dr_reddys_Data_Logs/
         │   ├── Dr_reddys_Data_Output/
         │── Dr_reddys_Reports/
         │   ├── Dr_reddys_Finance/
         │   ├── Dr_reddys_Revenues/
         │   ├── Dr_reddys_Expenditure/
         │── Dr_reddys_Scripts/
         │   ├── Dr_reddys_Robots/
         │   ├── Dr_reddys_PLC/
         │   ├── Dr_reddys_Vision/
         │── Dr_reddys_Resources/
         │   ├── Dr_reddys_Logs/
         │   ├── Dr_reddys_Materials/
         │   ├── Dr_reddys_Business_Cards/
