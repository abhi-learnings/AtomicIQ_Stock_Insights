FROM python

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt
EXPOSE 8502

ENTRYPOINT ["streamlit","run"]
CMD ["AtomicIQ_Stock_Insights.py"]
