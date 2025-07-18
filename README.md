# GadiPark

## Table of Contents

- [About GaddiPark](#about-gaddipark)
- [Features](#features)
- [User Roles](#user-roles)
- [Folder Structure](#folder-structure)
- [Technology Used](#technology-used)
- [Database Schema](#database-schema)
- [License](#license)

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

A visual representation of the database schema will be added here.

![Database Schema](db_schema.png)

## Folder Structure



## License

This project is licensed under the MIT License.
