# ML Basics 101

---

## Environment configuration

### Console

1. cat
2. head
3. tail
4. grep (buscador regular expresion)
5. history
6. cd, mkdir, l, rm
7. vim (abre editor de texto en consola)

### Repository

1. Add ssh key
2. Clone repository
3. Review .gitignore
4. Create a branch

### Virtual environment

1. Create virtualenv
    - ```python3 -m pip install virtualenv```
    - ```virtualenv .env```
2. Activate virtualenv
    - ```source .env/bin/activate``` 

### Libraries

1. Explore libraries
    - ```pip freeze```
2. Explore Makefile
    - ```make install```
    - ```make format```
    - ```make lint```
3. Add requirements file
    ```txt
    pandas
    sklearn
    ```
4. Install dependencies

### Docker

#### Create Dockerfile

```bash
touch Dockerfile
```

#### Create an image

1. Pull image from docker hub:

```Dockerfile
FROM <IMAGE>
```
i.e.

```Dockerfile
FROM python:3.8-slim
```

2. Define a work directory:


```Dockerfile
WORKDIR <NAME_DIRECTORY_WORK>
```
i.e.

```Dockerfile
WORKDIR /work
```

3. Update and install dependencies

```Dockerfile
RUN <COMAND>
```
i.e.

```Dockerfile
RUN apt update && apt install make -y
```

4. Copy requirements file and Makefile

```Dockerfile
COPY <FILES/DIRECTORIES> <TO_LOCATION>
```
i.e.

```Dockerfile
COPY requirements.txt Makefile /work/
```

5. Install libraries

```Dockerfile
RUN <COMAND>
```
i.e.

```Dockerfile
RUN make install
```

6. Expose port

```Dockerfile
EXPOSE <PORT>
```
i.e.

```Dockerfile
EXPOSE 8050
```

7. Define entrypoint and command

```Dockerfile
ENTRYPOINT [<COMMAND>]

CMD [<COMMAND_1>, <COMMAND_2>, <COMMAND_3>, ...]
```
i.e.

```Dockerfile
ENTRYPOINT ["jupyter"]

CMD ["notebook", "--ip", "0.0.0.0", "--port", "8050", "--allow-root", "--no-browser"]
```

#### Build image

```bash
docker build -t <IMAGE_NAME> .
```

i.e.

```bash
docker build -t mymlimage .
```

#### Run a container from previous image

```bash
docker run -it -p <PORT_LOCAL>:<PORT_CONTAINER> --name <CONTAINER_NAME> <ID_IMAGE>
```

```bash
docker run -it -p 8888:8050 --name pycaretcontainer mymlimage
```



---

## Data

### House Rent Prediction Dataset

```https://storage.googleapis.com/kagglesdsdata/datasets/2355600/4097760/House_Rent_Dataset.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20220907%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20220907T042446Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=71cd3808468948c2227bdd2f3cc7c20a129704c8e85a3f9270f89c30974fc1b68a7c6072e7d787265b84517d23b1d6e9be5d85de0bbade97f51f951301f53614dd8c0e2ff4e9c1f114de99e5737aff7eb48e6ead6d8e905a9051abf584f8cc94af8ac797d0e9333b79eceb42638e64f3468ed1b314c177866e020f5adf18b2d50a62f557b9ec1db024a048c8dece3ffa9038e25e18fe12a46d56bcb4f538ccc11081de3f0f1a0545a7b7583a7e7947e8020f41abb3be1338dabcccc72383cd368cceb32fedfe01ab1386fbfe4acc3550d6df214af073b5116e8e17b1d50fb6a3e8ac20adba6226f869deb5a02020c64928d6ef7c39373540ec4bc017de41023d```
