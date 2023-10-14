FROM python:3.11


#-------------------------for dev---------------------------------------------#
ENV ENVIRONMENT="dev"

# set timezone
ENV TZ="America/Vancouver"

RUN pip install --upgrade pip

# install requirements
COPY requirements.txt /opt/pyspider/requirements.txt
RUN pip install -r /opt/pyspider/requirements.txt

# # add all repo
# ADD ./ /opt/pyspider

# # run test
# WORKDIR /opt/pyspider
# RUN pip install -e .[all]

#VOLUME ["/opt/pyspider"]
# ENTRYPOINT ["pyspider"]

# EXPOSE 5000 23333 24444 25555 22222
