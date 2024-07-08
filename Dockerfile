FROM python:3.9.0

#It creates a working directory(app) for the Docker image and container
WORKDIR /app

#It copies the framework and the dependencies for the FastAPI application into the working directory
#COPY main.py .

#It will install the framework and the dependencies in the `requirements.txt` file in our Docker image and container.
#RUN pip install -r requirements.txt

#It will copy the remaining files and the source code from the host `fast-api` folder to the `app` container working directory
#COPY my-script.sh .
COPY . .
#RUN chmod +x my-script.sh
#It will expose the FastAPI application on port `8000` inside the container
EXPOSE 8888
#ENTRYPOINT /bin/bash
#It is the command that will start and run the FastAPI application container
#CMD ["python","-u","main.py"]
#CMD ./my-script.sh

CMD ["python","-u","main.py"]