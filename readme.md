# Create and activate a virtual environment
python -m venv venv

# To activate venv
source venv/bin/activate  # Unix/macOS
venv\Scripts\activate  # Windows

# Install required packages
pip install -r requirements.txt

# For migration run below command
alembic init alembic
uvicorn app.main:app --reload

# If we can also create a docker image 
docker build -t fastapi-addressbook .
docker run -d --name myfastapiapp -p 8000:8000 fastapi-addressbook
