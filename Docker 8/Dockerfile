FROM tomcat:latest

RUN cd /usr/local/tomcat && \
    mv webapps webapps2 && \
    mv webapps.dist webapps

EXPOSE 8080

CMD ["catalina.sh", "run"]
