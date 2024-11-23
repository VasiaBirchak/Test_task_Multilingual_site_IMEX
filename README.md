# Test_task_Multilingual_site_IMEX

### Setup

#### Clone the Repository:

```bash
git clone https://github.com/VasiaBirchak/Test_task_Multilingual_site_IMEX.git
```
### Create and Activate a Virtual Environment:
```bash
python3 -m venv venv
source venv/bin/activate
```
Install the Required Packages:

```bash
pip install -r requirements.txt
```
Apply Migrations:

```bash
python manage.py migrate
```
Create a Superuser:

```bash
python manage.py createsuperuser
```
Configuration Files:
.env: Stores sensitive data such as environment variables for connecting to the database.

## How to Use

Example .env File:

```bash
DB_NAME=multilingual_site
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=localhost
DB_POSRT=5432
```
Run the Development Server:
```bash
python manage.py runserver
```


### Launching:
Use Django to run a local server.
Go to the web interface and use the functionality.
### Development and Testing

Install the Development Dependencies:

```bash
pip install -r requirements.txt
```
Run the Tests:

```bash
pytest
```