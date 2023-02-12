# Use an official Vault image as the base image
FROM vault:1.5.0

# Add the necessary environment variables
ENV VAULT_ADDR=http://0.0.0.0:8200

# Create a new directory and copy the configuration file
RUN mkdir /vault/config
COPY config.hcl /vault/config/

# Expose the port
EXPOSE 8200

# Start Vault in server mode using the configuration file
CMD vault server -config=/vault/config/config.hcl
