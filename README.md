# 🎥 AutoSaveMediaUser – Automatically Save Telegram Media  

A **simple and efficient** Telegram script built with **Pyrogram**.  
🚀 Designed to **automatically save all received photos and videos** in private chats to your **Saved Messages** for quick and easy access.  

---

## 🌟 Features  
🔹 **Auto-Save Media** – Instantly saves all received photos and videos.  
🔹 **Works in Private Chats** – Automatically handles media sent by users.  
🔹 **Runs on Your Account** – No need for a bot, uses your personal Telegram account.  
🔹 **Lightweight & Fast** – Optimized for minimal resource usage.  
🔹 **Easy to Set Up** – Just configure your API details and run the script.  

---

## 🛠 Deployment Options  

### 🚀 **1- Click Deploy on Heroku**  
Deploy instantly on **Heroku** by clicking the button below:  

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/STKR2/AutoSaveMediaUser)  

🔗 **Visit Heroku:** [https://www.heroku.com](https://www.heroku.com)  

---

### 🖥 **Manual Deployment (VPS or Local Machine)**  

#### **Step 1: Install Dependencies**  
Make sure you have **Python 3.8+** installed, then run:  
```sh
git clone https://github.com/STKR2/AutoSaveMediaUser.git
cd AutoSaveMediaUser
pip install -r requirements.txt
```

#### **Step 2: Configure API Credentials**  
Edit `bot.py` and replace these values with your own:  
```python
api_id = "YOUR_API_ID"
api_hash = "YOUR_API_HASH"
session_string = "YOUR_SESSION_STRING"
```

#### **Step 3: Run the Script**  
```sh
python3 bot.py
```

---

## **🛡 Security Notice**  
🚨 **Use this script responsibly**. It runs on your personal Telegram account, so keep your API credentials private.  
