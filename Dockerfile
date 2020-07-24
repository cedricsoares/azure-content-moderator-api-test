FROM python:3.7.8-alpine

LABEL maintainer="Cedric Soares"


WORKDIR /app

COPY . /app

#install python packages & create specific user 
RUN \
    pip install pip --upgrade --no-cache-dir \
    pip install --no-cache-dir -r requirements.txt \
    && rm -rf ~/.cache/pip \
    && addgroup -S appgroup \
    && adduser -S appuser -G appgroup \
    && chown -R appuser ./ 

USER appuser

ENTRYPOINT [ "python" ]
CMD [ "app.py" ]