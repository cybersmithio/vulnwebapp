# vulnwebapp
A vulnerable web application for demonstration purposes.


# Before running:
export FLASK_APP=vulnwebapp

# To run:
python3 -m flask run --host=0.0.0.0

# Building the docker image
docker build -t vulnwebapp ./

# Run the docker image
docker run -p 5000:5000 --rm --name vulnwebapp vulnwebapp
