# Linux Homework Reminder & Manager ⏰

A lightweight, local homework manager built for Linux desktop environments. It provides a simple, distraction-free web GUI to manage assignments and uses a background Bash script connected to `cron` to send hourly desktop notifications for incomplete tasks.

## ✨ Features
* **Web Dashboard:** Simple black-and-white local web interface to add, view, and manage homework.
* **Smart Organization:** Categorize assignments by subject (pre-defined or custom).
* **Task Archiving:** Mark tasks as "Done" to remove them from active alerts and save them to an archive page.
* **Automated Alerts:** Sends native Linux desktop pop-ups (`notify-send`) every hour with a formatted list of pending tasks.
* **Boot Support:** Automatically starts the web server and triggers a desktop reminder 60 seconds after system boot.

## 🛠️ Technologies Used
* **Python (Flask):** Handles the local web server and JSON data processing.
* **HTML/CSS:** Renders the frontend dashboard.
* **Bash:** Parses data and triggers native Linux UI notifications.
* **Cron:** Schedules the automated hourly pop-ups.
* **PM2:** Manages the Python web server as a permanent background service.

---

## 🚀 Installation & Setup

### 1. Prerequisites
Ensure you have Python 3, Node.js, and PM2 installed on your Linux system. The installation commands depend on your Linux distribution:

**For Debian / Ubuntu / Linux Mint:**
```bash
sudo apt update
sudo apt install python3-pip nodejs npm libnotify-bin -y
sudo npm install -g pm2
```

**For Fedora / RHEL:**
```bash
sudo dnf install python3-pip nodejs npm -y
sudo npm install -g pm2
```

### 2. Clone the Repository
```bash
git clone https://github.com/razulD/Remind_Homework.git
cd Remind_Homework
```

### 3. Install Python Dependencies
The web server requires the Flask framework to run:
```bash
pip3 install flask
```

### 4. Configure the Bash Script
Make the reminder script executable:
```bash
chmod +x remind.sh
```
*Note: If you move this project to a different folder or user account, ensure the absolute paths inside `remind.sh` point to your new directory.*

### 5. Start the Background Web Server
Use PM2 to run the web interface silently in the background so it survives terminal closures:
```bash
pm2 start hw.py --name "homework-gui" --interpreter python3
pm2 save
pm2 startup
```
*(Note: The `pm2 startup` command will print a final command in your terminal that you must copy and paste to link PM2 to your system's boot process).*

### 6. Setup the Hourly Notifications
Open your cron scheduler:
```bash
crontab -e
```
Add these two lines at the bottom of the file (make sure to update the path if your username is not `xqzm`):
```bash
# Run exactly on the hour, every hour
0 * * * * /home/xqzm/Remind_Homework/remind.sh

# Run 60 seconds after boot
@reboot sleep 60 && /home/xqzm/Remind_Homework/remind.sh
```

---

## 💻 How to Use It

### Accessing the App
Open any web browser on your machine and navigate to:
**`http://localhost:5000`**

From this dashboard, you can:
1. **Add Homework:** Select a subject, type the assignment, and hit submit.
2. **Mark as Done:** Click "Mark Done" to archive a task. It will instantly be removed from your hourly pop-up alerts.
3. **View Archive:** Check your history of completed assignments.

### Triggering a Manual Reminder
You do not have to wait for the next hour to see your tasks. You can force the desktop notification to appear instantly by running the script in your terminal:
```bash
./remind.sh
```
*(Note: The pop-up will only trigger if you have active tasks on your dashboard).*
