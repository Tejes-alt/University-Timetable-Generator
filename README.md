# University Timetable Generator

A web-based University Timetable Generator developed using **Python**, **Flask**, and **SQLAlchemy**. The application provides an efficient way to generate and manage academic timetables through a structured web interface.

---

## 📌 Overview

Timetable scheduling is one of the most challenging administrative tasks in educational institutions. This project aims to simplify the process by providing a centralized platform that helps generate and organize university timetables while reducing manual effort.

The application follows a modular Flask architecture, making it easy to maintain, extend, and deploy.

---

## ✨ Features

* Academic timetable generation
* Modular Flask application structure
* Database integration with SQLAlchemy
* HTML template rendering using Jinja2
* Static resource management (CSS, JavaScript, Images)
* Database migration support
* Organized project architecture
* Easy cloud deployment

---

## 🛠️ Technologies Used

* Python
* Flask
* Flask-SQLAlchemy
* SQLAlchemy
* Jinja2
* HTML5
* CSS3
* JavaScript
* Gunicorn

---

## 📁 Project Structure

```
University timetable generator/
│
├── app/
│   ├── algorithms/
│   ├── engine/
│   ├── pipeline/
│   ├── routes/
│   ├── static/
│   └── templates/
│
├── migrations/
├── instance/
│
├── requirements.txt
├── run.py
├── seed.py
├── run_test.py
└── test_gen.py
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/University-Timetable-Generator.git
```

### 2. Navigate to the project

```bash
cd University-Timetable-Generator
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
python run.py
```

The application will be available at:

```
http://127.0.0.1:5000
```

---

## 🚀 Deployment

This project is ready to be deployed on platforms such as **Render**, **Railway**, or **PythonAnywhere**.

### Build Command

```bash
pip install -r requirements.txt
```

### Start Command

```bash
gunicorn run:app
```

---

## 📦 Dependencies

* Flask
* Flask-SQLAlchemy
* SQLAlchemy
* Werkzeug
* Jinja2
* Gunicorn

---

## 📈 Future Enhancements

* Faculty availability management
* Classroom allocation optimization
* Conflict detection and visualization
* Authentication and user roles
* Timetable export to PDF
* Timetable export to Excel
* Dashboard analytics
* Responsive user interface

---

## 🤝 Contributing

Contributions are welcome. Feel free to fork this repository, improve the project, and submit a pull request.

---

## 📄 License

This project is intended for educational and learning purposes.

---

## 👨‍💻 Author

**Tejes**

If you found this project helpful, consider giving it a ⭐ on GitHub.
