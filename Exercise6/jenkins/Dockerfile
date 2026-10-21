FROM jenkins/jenkins:lts-jdk17
USER root
RUN ARCH=$(uname -m) && curl -fsSL https://download.docker.com/linux/static/stable/${ARCH}/docker-27.3.1.tgz | tar -xz --strip-components=1 -C /usr/local/bin docker/docker
RUN jenkins-plugin-cli --plugins workflow-aggregator
ENV JAVA_OPTS="-Djenkins.install.runSetupWizard=false"
COPY create-job.groovy /usr/share/jenkins/ref/init.groovy.d/create-job.groovy
