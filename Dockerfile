FROM python:latest
WORKDIR /usr/local/bin
COPY pom-parse-edit.py .
CMD ["pom-parse-edit.py", "-OPTIONAL_FLAG"]
