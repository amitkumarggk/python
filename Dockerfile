FROM python:latest
WORKDIR /usr/local/bin
COPY pom-parse-edit.py .
COPY pom-parse-edit-Test.py .
COPY pom.xml .
CMD ["pom-parse-edit.py", "-OPTIONAL_FLAG"]
CMD ["pom-parse-edit-Test.py", "-OPTIONAL_FLAG"]
