FROM python
RUN python -m pip install telebot && python -m pip install telegram
COPY main.py /
COPY secrets.py /
COPY ./photos ./photos
ENTRYPOINT [ "python", "./main.py" ]