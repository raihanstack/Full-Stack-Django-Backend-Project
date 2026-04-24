# 🌲 raihanstack | Professional E-Commerce Backend

[![Django](https://img.shields.io/badge/Django-6.0+-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Django Rest Framework](https://img.shields.io/badge/DRF-3.17+-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.django-rest-framework.org/)
[![Python](https://img.shields.io/badge/Python-3.14+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)

A simple and powerful online store system built with **Django**. This project helps you manage users, products, and a shopping cart easily through a clean and secure interface.

---

## ✨ Key Features

- 👤 **User Management**: Custom User model (`SiteUser`) with roles (User, Admin, SuperAdmin).
- 📦 **Product Catalog**: Full CRUD for products with dynamic image uploads.
- 🛒 **Cart System**: Efficient shopping cart management with total price calculation.
- 🔐 **Secure Authentication**: Token-based authentication for API endpoints.
- 🎨 **Modern Architecture**: Clean separation of concerns with dedicated `user_api` and `product_api` apps.
- ⚙️ **Environment Config**: Secure configuration using `.env` files.

---

## 🛠️ Technology Stack

| Component | Technology |
| :--- | :--- |
| **Framework** | Django 6.0.4 |
| **API** | Django Rest Framework 3.17.1 |
| **Database** | SQLite (Development) / PostgreSQL (Ready) |
| **Auth** | Token Authentication |
| **Media** | Pillow (Image Processing) |
| **Environment** | python-dotenv |

---

## 🚀 Getting Started

### 1. Prerequisites
- Python 3.14+
- Virtual Environment tool (`venv`)

### 2. Installation

Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/raihanstack/Full-Stack-Django-Backend-Project.git
cd Full-Stack-Django-Backend-Project
```

### 3. Setup Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Environment Variables

Create a `.env` file in the `backend/` directory:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

### 6. Migrations and Database

```bash
cd backend
python manage.py makemigrations
python manage.py migrate
```

### 7. Run the Server

```bash
python manage.py runserver
```

---

## 📡 API Documentation

### Authentication
- `POST /api/auth/` - Obtain Authentication Token

### User API
- `GET /api/users/` - List users (Authenticated)
- `POST /api/users/` - Register new user (Public)

### Product API
- `GET /api/products/` - List products
- `POST /api/products/` - Create product (Admin)
- `GET /api/cart-items/` - List cart items (Authenticated)
- `POST /api/cart-items/` - Add to cart (Authenticated)

---

## 📂 Project Structure

```text
.
├── backend/
│   ├── backend/          # Project settings & root URLs
│   ├── product_api/      # Product & Cart logic
│   ├── user_api/         # User & Auth logic
│   ├── media/            # Uploaded product images
│   ├── manage.py         # Django management script
│   └── .env              # Environment variables (Internal)
├── .venv/                # Virtual environment
├── .gitignore            # Git ignore rules
└── requirements.txt      # Python dependencies
```

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

## 📄 License

This project is licensed under the MIT License.

---
Developed with ❤️ by [Raihan](https://github.com/raihanstack)
