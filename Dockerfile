FROM python:3-onbuild
EXPOSE 8000
CMD ["uvicorn", "app:app", "--reload" ]