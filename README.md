# 🐍 Ubuntu-Inspired Image Fetcher  

## 📌 Description  
This project is part of the **Python Libraries Assignment** for the PLP Software Development course.  
It embodies the Ubuntu philosophy of **community**, **sharing**, and **respect** by connecting to the wider internet to fetch and organize images for later appreciation.  

The program:  
- ✅ Prompts the user for an image URL  
- ✅ Creates a **Fetched_Images** directory (if it doesn’t exist)  
- ✅ Downloads the image and saves it with an appropriate filename  
- ✅ Handles network and file errors gracefully  
- ✅ Strengthens connection to the global community through mindful resource sharing  

---

## 🚀 How It Works  
1. **Run the program**:  
   ```bash
   python fetch_images.py 

2. **Enter an image URL when prompted. Example working URLs**:
   - https://picsum.photos/600/400
   - https://picsum.photos/400/300
  
3. **The script will**:
   - Fetch and save the image inside the Fetched_Images directory.
   - Display a success message:  
     ✓ Successfully fetched: 600.jpg  
     ✓ Image saved to Fetched_Images/600.jpg  

---

## 🌐 Features Inspired by Ubuntu Philosophy
- Community: Connects to shared online resources.
- Respect: Gracefully handles errors instead of crashing.
- Sharing: Organizes downloaded images for easy access.
- Practicality: Simple, useful tool for everyday tasks.
  
---

## 🧪 Challenge Extensions (Optional)
- 📥 Support for multiple URLs in one run.
- 🛡 Precautions for downloading from unknown sources.
- 🔄 Avoid downloading duplicate images.
- 📝 Check important HTTP headers (e.g., Content-Type, Content-Length) before saving files.

---

## 📂 Repository Structure
 ```
Ubuntu_Requests/ # Main project folder
├── fetch_images.py # Python script for fetching images
├── Fetched_Images/ # Folder storing downloaded images
│ ├── 300.jpg # Example downloaded image
│ └── 400.jpg # Example downloaded image
└── README.md # Project documentation
```

---

## 💡 Example Output
**Welcome to the Ubuntu Image Fetcher**
A tool for mindfully collecting images from the web  

Please enter the image URL: https://picsum.photos/600/400  
✓ Successfully fetched: 600.jpg  
✓ Image saved to Fetched_Images/600.jpg  

Connection strengthened. Community enriched.  


## Built with Python 🐍

