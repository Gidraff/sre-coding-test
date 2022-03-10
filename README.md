# sre-coding-test

Flask app with monitoring

<i>Note: This guide assumes you are a macOsx user. If you are on a different OS, follow the necessary installation guide for your platform
</i>

### Prerequisites

To get the application up and running, you need to have following installed locally.

- Postgres `version 13 or greater`
- Redis
- Python3.9 and Pip (python package manage)
- [Prometheus](https://github.com/prometheus/prometheus/releases/download/v2.33.5/prometheus-2.33.5.darwin-amd64.tar.gz) and [Alert Manager](https://github.com/prometheus/alertmanager/releases/download/v0.23.0/alertmanager-0.23.0.darwin-amd64.tar.gz)
- [Redis exporter](https://github.com/oliver006/redis_exporter) and [Postgres exporter](https://github.com/prometheus-community/postgres_exporter)

### Setup:

To get a copy of this repository on your environment, run:

```
git clone https://github.com/Gidraff/sre-coding-test.git

python3 -m venv venv #creates a virtualenv

cd sre-coding-test
```

Once inside the root directory of the project, the next step is to install the dependencies listed on the `requirements.txt`

```
pip install -r requirements.txt
```

Create a `.env` to hold the environment variables. These variables are required at runtime. Type this command on your terminal

```
cp .env.sample .env
```

After the file is created, edit the file with the correct values for you environment.

To make the environment available, execute the following commands:

```
source .env
```

Before you run the application, make sure that postgres and redis services are running. To check, execute:

```
brew services list
```

If the services are not running, you need start them by executing the command below:

```
brew services start postgresql

brew services start redis
```

Create a database with your preferred name and edit the value `SQLALCHEMY_DATABASE_URI` in the `.env` file

### Run the application

Hopefully you've managed to execute preceding steps successfully. If everything went well, the next step will be to spin up the application. Execute the following command to start the application server.

```
flask run
```

Check if the application is up by opening http://localhost:5000/status or http://localhost:5000/helloworld on a REST client. You should get a status 200. This shows the applications is running ok.

### Monitoring

Next step is to run the prometheus using the prometheus.yaml configuration file found in the root of this repository.

Execute this command

```
prometheus --config.file=prometheus.yaml
```

To view the prometheus GUI, point you browser to http://localhost:9090. This should open an interactive graphical interface where you can check status of the application.

## Explanation of the metrics that should be watched

#### API

For the backend service:

- Request per second and Errors per second
- CPU and Memory Usage
- Uptime
- Request duration
- Latency (Average and Maximum latency)

#### Cache (REDIS)

For the caching service:

- The rate of hit or/and miss
- Disk I/O (Read/writes)
- CPU and Memory Usage

#### Database (Postgresql)

For the database:

- Database file I/O (Read/Writes)
- Hit or/and miss ration
- Open and closed connections
- Locks and blocks
- Memory and CPU usage
