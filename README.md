# Banking Application

This is a simple banking application built using Django, allowing users to perform account-related activities such as transferring funds, paying bills, and viewing transaction history. The application supports basic account management and displays relevant financial information to users.

## Features

- **Account Summary**: View account details including balance and transaction history.
- **Transfer Funds**: Transfer funds from one account to another.
- **Pay Bills**: Pay bills using the available balance in the account.
- **Transaction History**: View a list of all transactions made with an account.
  
## Installation

To set up the project locally, follow these steps:

### Prerequisites

Ensure you have the following installed:
- Python (>=3.8)
- Django (>=5.0)
- MySQL or another database of your choice.

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/banking-app.git
   cd banking-app
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Set up the database:

   - Create a MySQL database and update the `DATABASES` setting in `settings.py` with your database details.
   - Run migrations to set up the database schema:

     ```bash
     python manage.py migrate
     ```

6. Create a superuser to access the admin panel:

   ```bash
   python manage.py createsuperuser
   ```

7. Start the development server:

   ```bash
   python manage.py runserver
   ```

8. Visit `http://127.0.0.1:8000/` to access the application.

## Application Structure

- `accounts/`: Contains the app that handles all banking-related functionalities such as transferring funds, bill payments, and viewing transaction history.
- `templates/accounts/`: Contains the HTML files for rendering the UI.
- `static/accounts/css/`: Contains the CSS files for styling the frontend.

## Database Models

### Account

- `account_number`: A unique identifier for each account.
- `account_type`: Type of the account (e.g., Checking, Savings).
- `balance`: The current balance of the account.

### Transaction

- `account`: The account making the transaction.
- `recipient_account`: The account receiving the transfer.
- `amount`: The transaction amount.
- `transaction_type`: The type of transaction (e.g., Transfer, Withdrawal).

### BillPayment

- `account`: The account making the payment.
- `biller_name`: The name of the company or individual to whom the payment is made.
- `amount`: The amount being paid.
- `due_date`: The due date for the bill.

## Usage

1. **Account Summary**: View the details of a user's account, including the balance and recent transactions.
2. **Transfer Funds**: Transfer money from your account to another user's account. Specify the recipient's account number and the amount.
3. **Pay Bill**: Pay bills by entering the biller's name and the amount. Ensure there is enough balance in your account.
4. **Transaction History**: View all transactions related to your account, including transfers and bill payments.

## Future Enhancements

- **User Authentication**: Implement user registration and login functionality.
- **Security**: Add proper validation and security features such as encryption for sensitive data (e.g., account numbers).
- **APIs**: Develop APIs for mobile and other third-party integrations.

