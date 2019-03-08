### STAGE 2: Setup ###
FROM python:3.6

# Set env variables used in this Dockerfile (add a unique prefix, such as DOCKYARD)
# Local directory with project source
ENV AI_CORE_SRC=.
# Directory in container for all project files
ENV AI_CORE_SRVHOME=/srv
# Directory in container for project source files
ENV AI_CORE_SRVPROJ=/srv/ai-core

# Create application subdirectories
WORKDIR $AI_CORE_SRVPROJ

# Copy application source code to SRCDIR
COPY $AI_CORE_SRC $AI_CORE_SRVPROJ

# Install Python dependencies
RUN python ./setup.py install

# Copy entrypoint script into the image
WORKDIR $AI_CORE_SRVPROJ
