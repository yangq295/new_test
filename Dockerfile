FROM python:3.7.3

WORKDIR .

ADD . .

RUN pip install -r requirements.txt

CMD ["pytest","test_cases/*","--alluredir","allure-results"]