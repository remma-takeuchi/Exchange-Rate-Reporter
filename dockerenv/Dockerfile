FROM ubuntu:20.04

# docker
RUN apt update && \
    apt -qy full-upgrade && \
    apt install -qy curl

# Python
RUN apt install -y python3 pip
RUN pip install requests oauth2client gspread python-daemon schedule

# Timezone
ENV DEBIAN_FRONTEND=noninteractive
RUN apt install tzdata
ENV TZ Asia/Tokyo

CMD ["/bin/bash"]

