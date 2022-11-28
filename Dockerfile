FROM python:3.10.0
WORKDIR /app
EXPOSE 8501
COPY ./ app
ENTRYPOINT ["streamlit", "run"]

CMD ["./prediction.py"]

