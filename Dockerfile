FROM kitware/paraview:pv-v5.7.1-osmesa-py3

USER root
RUN pip3 install docker
RUN mkdir "src"

COPY main.py ./src

CMD ["./bin/pvpython","./src/main.py"]