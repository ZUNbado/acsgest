FROM python:2-onbuild
EXPOSE 8000
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
