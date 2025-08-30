<h1 align="center" style="font-size:40px; font-weight: bold;">GaadiPark</h1>

[![image.png](https://i.postimg.cc/BbH8d6c7/image.png)](https://postimg.cc/7JPYzqRS)


## About GaddiPark

GaddiPark is a comprehensive vehicle parking management system designed for multiple users and administrators. It supports efficient parking lot management, vehicle tracking, and electric vehicle (EV) regulation. Both users and admins can view summary charts for parking analytics.

## Features

| Feature                     | Description                                                                 |
|-----------------------------|-----------------------------------------------------------------------------|
| Role-based access           | Separate functionality for users and admins                                 |
| Admin dashboard             | View and manage users, bookings, lots, and statistics                        |
| Parking lot management      | Create, update, and delete parking lots with full control                    |
| EV spot support             | Assign electric vehicle spots and define charging rates                      |
| Spot generation             | Auto-create spot numbers with labeling logic                                |
| Smart booking system        | Book and release spots with time tracking and billing                        |
| Booking history             | Full historical records of previous and current parkings                     |
| Real-time monitoring        | View current occupancy and availability status                               |
| Visual charts               | Graphical summary of usage, earnings, and traffic patterns                   |
| Search & filter             | Filter by booking ID, lot name, user ID, or spot number                      |
| Secure authentication       | User/admin login with session-based security                                 |


## User Roles

| Role    | Capabilities                                                                                 |
|---------|----------------------------------------------------------------------------------------------|
| User    | Register, log in, view lots, park vehicles, view parking history, view summary charts.       |
| Admin   | Manage lots, spots, users, vehicles, EV spots, view analytics, set policies, view charts.    |


## Technology Used

| Technology   | Purpose                                    |
|--------------|--------------------------------------------|
| HTML         | Structure of web pages                     |
| CSS          | Styling and layout                         |
| JavaScript   | Frontend logic and interactivity           |
| Python       | Backend server and logic                   |
| SQLite       | Database for storing records               |
| Chart.js     | Charts and data visualization (CDN)        |
| Font Awesome | Icons and fonts (CDN)                      |

## Database Schema

<img width="1045" height="956" alt="image" src="https://github.com/user-attachments/assets/77a9ba03-652a-490c-8b34-11bde73af87e" />


## Folder Structure

## 📁 Project Structure

```
📁 GadiPark/
│
├── app.py
├── config.py
├── README.md
├── requirements.txt
│
├── 📁 instance/
│   └── database.sqlite3
│
├── 📁 models/
│   ├── booking.py
│   ├── history.py
│   ├── parking_lot.py
│   ├── parking_spot.py
│   ├── payment.py
│   ├── user.py
│   ├── vehicle.py
│   └── __init__.py
│
├── 📁 routes/
│   ├── admin.py
│   ├── auth.py
│   ├── booking.py
│   ├── decorators.py
│   ├── parking.py
│   ├── payment.py
│   ├── profile.py
│   ├── search.py
│   ├── user.py
│   ├── user_activity.py
│   └── __init__.py
│
├── 📁 static/
│   ├── 📁 css/
│   │   ├── admin_charts.css
│   │   ├── admin_dashboard.css
│   │   ├── admin_sidebar.css
│   │   ├── base.css
│   │   ├── booking_confirmed.css
│   │   ├── find_parking.css
│   │   ├── history.css
│   │   ├── index.css
│   │   ├── login.css
│   │   ├── modal.css
│   │   ├── parking_lot_details.css
│   │   ├── payment.css
│   │   ├── profile.css
│   │   ├── receipt.css
│   │   ├── signup.css
│   │   ├── user_dashboard.css
│   │   ├── user_navbar.css
│   │   ├── user_summery.css
│   │   └── vehicle.css
│   │
│   ├── 📁 images/
│   │   ├── login_final.svg
│   │   └── signup_final.svg
│   │
│   └── 📁 js/
│       ├── admin_dashboard.js
│       ├── find_parking.js
│       ├── parking_lot_details.js
│       ├── profile.js
│       └── user_dashboard.js
│
└── 📁 templates/
    ├── admin_charts.html
    ├── admin_dashboard.html
    ├── admin_sidebar.html
    ├── base.html
    ├── booking_confirmed.html
    ├── find_parking.html
    ├── history.html
    ├── index.html
    ├── login.html
    ├── parking_lot_details.html
    ├── payment.html
    ├── profile.html
    ├── receipt.html
    ├── signup.html
    ├── users_summery.html
    ├── user_charts.html
    ├── user_dashboard.html
    ├── user_navbar.html
    └── vehicle.html
```
        

---

## How to Run the Application

Follow these steps to set up and run the GadiPark project locally:

### 1. Clone the Repository

```bash
_git clone https://github.com/24f2003468/vehicle-parking-app.git

```

### 2. Create a Virtual Environment (optional but recommended)

```
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 4.Run the App

```
python app.py
```

## Made with ❤️ by Litesh

## License

This project is licensed under the MIT License.
