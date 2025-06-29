# Deployment Log – `v1.0.0`
**Project**: START – Effortless App Launcher for Windows  
**Version**: `v1.0.0`  
**Date**: 17-04-2025  
**Developer**: Subhradip Majumder  

## Summary
The first stable release of **START**, a Windows desktop application that helps users create and run custom `.bat` files to launch multiple programs with a single click. This tool is designed for productivity-focused users like developers, students, and professionals.


**🚀 Deployed and Live: START v1.0.0 is now available to make your daily setup effortless.**


## Features Implemented
- Login and authentication system for personalized usage  
- GUI to add and save custom application paths  
- Automatic `.bat` file generator for launching selected apps  
- Clean, beginner-friendly UI  
- Lightweight EXE for quick deployment 
-  Remember user sessions


## 🛠️ Development and Deployment Steps
1. Built the application using **Python + CustomTkinter**
2. Converted the script to `.exe` using `PyInstaller`
   ```bash
   pyinstaller --onefile --windowed start.py
   ```
3. Created a clean interface with icon assets and form validation
4. Added `.bat` script generation logic to dynamically build launch scripts
5. Packaged assets and installer as a `.zip` for GitHub
6. Uploaded to GitHub under [Releases V1.0.0](https://github.com/subhradip32/Custom_StartUp/releases/tag/V1.0)


## 🧪 Testing Notes
- ✅ Tested on Windows 10 and Windows 11
- ✅ Launches multiple apps via generated `.bat` script
- ✅ Login and UI functionality confirmed working
- 🧩 No known critical bugs in this version
- ⚠️ Minor UI improvements planned for future release (resizing, theming)


## 📂 File Structure Snapshot
```
/Custom_StartUp/
│
├── START.exe
├── assets/
├── README.md
├── LICENSE
├── start.py
├── utils/
├── login_module/
├── scripts/
└── docs/
    └── DEPLOYMENT_LOG_v1.0.0.md
```


## 📦 Installation Guide
1. Download from GitHub [here](https://github.com/subhradip32/Custom_StartUp/releases/tag/V1.0)
2. Run the `.exe` or extract `.zip` file
3. Launch `START.exe`
4. Login and configure your script
5. Save and double-click the generated `.bat` to launch your set of programs


## 📝 Next Steps (For v1.1.0)
-  Add drag-and-drop app selection
-  Implement theme (dark/light mode)
-  Add feature to auto-run on Windows startup
-  Improve UI responsiveness for different screen sizes



## 📬 Contact
Subhradip Majumder  
📧 subhradipmajumder309@gmail.com  

