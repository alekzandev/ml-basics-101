FROM python:3.8-slim

WORKDIR /work 

RUN apt update \
    && apt install gcc -y\
    && apt install g++ -y\
    && apt install make -y\
    && pip install --upgrade pip\
    && pip install wheel\
    && pip install --upgrade setuptools

COPY . /work/

RUN make install

EXPOSE 8050

ENTRYPOINT ["jupyter"]

CMD ["notebook", "--ip", "0.0.0.0", "--port", "8050", "--no-browser", "--allow-root"]

