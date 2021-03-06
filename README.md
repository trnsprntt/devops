# DevOps course at Innopolis University F21

![ci_workflow](https://github.com/trnsprntt/devops/actions/workflows/ci.yml/badge.svg)

## Description

This is a web-application to show current time in Moscow (GMT+3).

![](https://i.imgur.com/nWlB99g.png)

### Built With

* Flask

## Getting Started

To get the application up and running (locally or in Docker) follow these simple steps.

### Locally

1. Clone the repo

   ```sh
   git clone https://github.com/trnsprntt/devops.git
   ```

2. Install packages

   ```sh
   pip install requirements.txt
   ```

3. Go to the application directory

   ```sh
   cd current_time_app
   ```

4. Export the necessary variables

   ```sh
   #for Mac and Linux users
   export FLASK_APP=current_time_app
   export FLASK_ENV=development

   #for Windows users
   set FLASK_APP=current_time_app
   set FLASK_ENV=development
   ```

5. Launch the application

   ```sh
   flask run
   ```

6. Go to ```http://localhost:5000/``` and see it's working :)

### In Docker

1. Pull the image from DockerHub

   ```sh
   docker pull trnsprntt/current_time_app:latest
   ```

2. Run the container

   ```sh
   docker container run -p 5000:5000  -v static:/home/python_app/static trnsprntt/current_time_app:latest
   ```

3. Go to ```http://localhost:5000/``` and see it's working :)

## Testing

1. Prerequisites
   ```
   pytest
   ```

2. Go to the project directory
   ```
   cd devops/python_app
   ```

3. Run unit tests
   ```
   pytest tests
   ```

## Usage

Refresh the ```localhost:5000/``` to update the time

Go to ```localhost:5000/visits``` to see the journal of base endpoint accesses

## Roadmap

Hopefully by the end of the course this application 

1. Would be in AWS
2. Would have CI pipeline set
3. Will be monitored

## Contributing

If for some reason you are willing to complete my labs instead of me :)

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## Contact

Telegram - @trnsprntt

