FROM pycaret/full

WORKDIR /work 

#RUN apt update && apt install make -y

COPY . /work/

#RUN make install

#EXPOSE 8050

