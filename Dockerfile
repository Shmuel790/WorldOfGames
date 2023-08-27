FROM python
COPY requierments.txt .
RUN pip install --upgrade pip && pip install -r requierments.txt
RUN mkdir /app
WORKDIR /app
CMD ["python", "/maingame.py"]