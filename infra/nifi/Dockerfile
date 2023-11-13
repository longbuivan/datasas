FROM centos
# MAINTAINER longbuivan longbuivan longbuivan95@gmail.com

#install yum repos

RUN cd /etc/yum.repos.d/
RUN sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-*
RUN sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-*

RUN yum -y install java

ENV JAVA_HOME /usr/lib/jvm/jre-1.8.0-openjdk
RUN export JAVA_HOME

ENV NIFI_VERSION=1.18.0 \
        NIFI_HOME=/opt/nifi \
        MIRROR_SITE=https://archive.apache.org/dist
        
# https://archive.apache.org/dist/nifi/1.18.0/nifi-1.18.0-bin.zip
# Picked the recommended mirror from Apache for the distribution.
# Import the Apache NiFi release keys, download the release, and set up a user to run NiFi.
RUN set -x \
    && curl -Lf https://dist.apache.org/repos/dist/release/nifi/KEYS -o /tmp/nifi-keys.txt \
    && gpg --import /tmp/nifi-keys.txt \
    && curl -Lf ${MIRROR_SITE}/nifi/${NIFI_VERSION}/nifi-${NIFI_VERSION}-bin.zip -o /tmp/nifi-bin.zip \
    && mkdir -p ${NIFI_HOME} \
    && tar -z -x -f /tmp/nifi-bin.zip -C ${NIFI_HOME} --strip-components=1 \
    && rm /tmp/nifi-keys.txt \
    && sed -i -e "s|^nifi.ui.banner.text=.*$$|nifi.ui.banner.text=Docker NiFi ${NIFI_VERSION}|" ${NIFI_HOME}/conf/nifi.properties \
    && groupadd nifi \
    && useradd -r -g nifi nifi \
    && bash -c "mkdir -p ${NIFI_HOME}/{database_repository,flowfile_repository,content_repository,provenance_repository}" \
    && chown nifi:nifi -R ${NIFI_HOME}
# RUN set -x \
#         && curl -Lf https://dist.apache.org/repos/dist/release/nifi/KEYS -o /tmp/nifi-keys.txt \
#         && gpg --import /tmp/nifi-keys.txt \
#         && curl -Lf ${MIRROR_SITE}/nifi/${NIFI_VERSION}/nifi-${NIFI_VERSION}-bin.tar.gz -o /tmp/nifi-bin.tar.gz \
#         && mkdir -p ${NIFI_HOME} \
#         && tar -z -x -f /tmp/nifi-bin.tar.gz -C ${NIFI_HOME} --strip-components=1 \
#         && rm /tmp/nifi-keys.txt \
#         && sed -i -e "s|^nifi.ui.banner.text=.*$$|nifi.ui.banner.text=Docker NiFi ${NIFI_VERSION}|" ${NIFI_HOME}/conf/nifi.properties \
#         && groupadd nifi \
#         && useradd -r -g nifi nifi \
#         && bash -c "mkdir -p ${NIFI_HOME}/{database_repository,flowfile_repository,content_repository,provenance_repository}" \
#         && chown nifi:nifi -R ${NIFI_HOME}

# These are the volumes (in order) for the following:
# 1) user access and flow controller history
# 2) FlowFile attributes and current state in the system
# 3) content for all the FlowFiles in the system
# 4) information related to Data Provenance
# You can find more information about the system properties here - https://nifi.apache.org/docs/nifi-docs/html/administration-guide.html#system_properties
VOLUME ["${NIFI_HOME}/database_repository", \
        "${NIFI_HOME}/flowfile_repository", \
        "${NIFI_HOME}/content_repository", \
        "${NIFI_HOME}/provenance_repository"]

# Open port 8081 for the HTTP listen
USER nifi
WORKDIR ${NIFI_HOME}
EXPOSE 8080 8081
CMD ["bin/nifi.sh", "run"]