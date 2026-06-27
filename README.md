# Customer Management API

A simple yet professional customer management system built with **Django** and **Django REST Framework**.

---

## 📌 Overview

This project provides a REST API to manage customers and their notes. It supports customer registration, status tracking, and note management through a clean nested API structure.

---

## ⚙️ Tech Stack

| Package | Purpose |
|---------|---------|
| Django 5.2 | Web framework |
| Django REST Framework | REST API |
| drf-nested-routers | Nested URL routing |
| django-cors-headers | CORS handling |
| django-filter | Filtering support |
| drf-spectacular | Swagger API docs |

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/username/customer-management.git
cd customer-management
```

### 2. Create and activate virtual environment
```bash
# Create
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply migrations
```bash
python manage.py migrate
```

### 5. Create superuser
```bash
python manage.py createsuperuser
```

### 6. Run the server
```bash
python manage.py runserver
```

---

## 🗄️ Models

### Customer
| Field | Type | Description |
|-------|------|-------------|
| `name` | CharField | Full name |
| `email` | EmailField | Email address (optional) |
| `phone` | CharField | Phone number (max 11 digits) |
| `address` | TextField | Address |
| `status` | CharField | Customer status |
| `created_at` | DateTimeField | Record creation time |
| `updated_at` | DateTimeField | Last update time |

#### Customer Status Choices
| Value | Description |
|-------|-------------|
| `new` | Newly registered customer |
| `contacted` | Customer has been contacted |
| `customer` | Active customer |

### Note
| Field | Type | Description |
|-------|------|-------------|
| `customer` | ForeignKey | Related customer |
| `note` | TextField | Note content |
| `created_at` | DateTimeField | Note creation time |

---

## 🔌 API Endpoints

### 👤 Customers `/customers/`

#### List all customers
```http
GET /customers/
```
**Response:**
```json
[
  {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com",
    "phone": "09123456789",
    "address": "123 Main St",
    "status": "new",
    "notes": [
      {
        "id": 1,
        "note": "Interested in premium plan",
        "created_at": "2026-06-27T10:00:00Z"
      }
    ],
    "created_at": "2026-06-27T09:00:00Z",
    "updated_at": "2026-06-27T10:00:00Z"
  }
]
```

#### Create a customer
```http
POST /customers/
Content-Type: application/json

{
  "name": "John Doe",
  "email": "john@example.com",
  "phone": "09123456789",
  "address": "123 Main St"
}
```
**Response:** `201 Created`

#### Retrieve a customer
```http
GET /customers/{id}/
```

#### Full update
```http
PUT /customers/{id}/
Content-Type: application/json

{
  "name": "John Doe",
  "phone": "09123456789",
  "address": "123 Main St",
  "status": "contacted"
}
```

#### Partial update
```http
PATCH /customers/{id}/
Content-Type: application/json

{
  "status": "contacted"
}
```

#### Delete a customer
```http
DELETE /customers/{id}/
```
**Response:** `204 No Content`

#### Change customer status
```http
POST /customers/{id}/change_status/
Content-Type: application/json

{
  "status": "customer"
}
```
**Response:**
```json
{ "status": "updated" }
```

---

### 📝 Notes `/customers/{customer_id}/notes/`

Notes are nested under customers — each note belongs to a specific customer.

#### List customer notes
```http
GET /customers/1/notes/
```

#### Add a note
```http
POST /customers/1/notes/
Content-Type: application/json

{
  "note": "Customer is interested in a 20% discount"
}
```
**Response:** `201 Created`

#### Retrieve a note
```http
GET /customers/1/notes/{note_id}/
```

#### Update a note
```http
PATCH /customers/1/notes/{note_id}/
Content-Type: application/json

{
  "note": "Updated note content"
}
```

#### Delete a note
```http
DELETE /customers/1/notes/{note_id}/
```
**Response:** `204 No Content`

---

### 🔍 Filtering & Pagination

#### Filter by status
```http
GET /customers/?status=new
GET /customers/?status=contacted
GET /customers/?status=customer
```

#### Pagination
```http
GET /customers/?page=1
```
> Returns 20 customers per page

---

## 📁 Project Structure

```
customer-management/
├── customer/
│   ├── migrations/
│   ├── models.py        ← Customer & Note models
│   ├── serializers.py   ← Nested serializers
│   ├── views.py         ← ViewSets
│   ├── urls.py          ← Nested routers
│   └── admin.py         ← Admin with inline notes
├── customer-management/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── venv/
├── .gitignore
├── api.http
├── db.sqlite3
├── manage.py
├── README.md
└── requirements.txt
```

---

## 🛠️ Admin Panel

URL: `http://127.0.0.1:8000/admin`

Features:
- List customers with status filter
- Search customers by name or email
- View and manage notes inline within each customer

---

## 📖 API Documentation (Swagger)

URL: `http://127.0.0.1:8000/api/docs/`

Interactive Swagger UI powered by **drf-spectacular** — explore and test all endpoints directly from the browser.

---