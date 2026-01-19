# Django Delights - Inventory Management System

A robust Django-based web application for managing restaurant inventory, menu items, purchasing, and financial tracking.

## 🚀 Features

- **Inventory Management**: Track ingredients, quantities, and unit prices.
- **Menu Management**: Create and manage menu items with dynamic cost calculation based on recipes.
- **Recipe System**: Link ingredients to menu items to automatically calculate production costs.
- **Purchase Tracking**: Record sales of menu items and track transaction history.
- **Financial Dashboard**: View real-time Balance Sheet with Revenue, Cost, and Profit calculations.
- **Authentication**: Secure Login, Logout, and Registration system for staff access.
- **Responsive Design**: Clean, user-friendly interface with mobile-responsive forms and tables.

## 🛠️ Technology Stack

- **Backend**: Django 5.x (Python)
- **Database**: SQLite (Default)
- **Frontend**: HTML5, CSS3 (Custom styling)
- **Authentication**: Django Auth System

## 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd Django_Delights
   ```

2. **Create and activate a virtual environment (optional but recommended):**
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate

   # Mac/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install django
   ```

4. **Apply database migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (for Admin panel access):**
   ```bash
   python manage.py createsuperuser
   ```

## 🚦 Usage

1. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

2. **Access the application:**
   - Open your browser and go to `http://127.0.0.1:8000/`
   - You will be redirected to the **Login** page.

3. **Login / Register:**
   - Use the **Register** link to create a new staff account.
   - Or use the superuser account you created.

4. **Navigation:**
   - **Inventory**: View current stock of ingredients.
   - **Menu**: View menu items and prices.
   - **Purchases**: Record a new sale.
   - **History**: View log of all past purchases.
   - **Balance Sheet**: Check financial performance (Profit/Loss).

## 📂 Project Structure

```
Django_Delights/
├── inventory/              # Main application folder
│   ├── migrations/         # Database migrations
│   ├── static/             # CSS and static files
│   ├── templates/          # HTML Templates (inventory/...)
│   ├── admin.py            # Admin panel configuration
│   ├── forms.py            # Forms for CRUD operations
│   ├── models.py           # Database models (Ingredient, MenuItem, etc.)
│   ├── urls.py             # URL routing
│   └── views.py            # View logic (CBVs and FBVs)
├── delight_settings/       # Project settings
│   ├── settings.py         # Main configuration
│   └── urls.py             # Root URL config
├── db.sqlite3              # Database file
└── manage.py               # Django command-line utility
```

## 🛡️ License

This project is developed as part of the Codecademy Data Science/Web Development path.
