# Data Integrations

To Setup data connection via API

- [ ] JDBC Connection
- [ ] Kafka Connection
- [ ] SFTP Connection
- [ ] Rest API Connection

## Diagram
The following diagram shows how data integration works

[diagram](../app/wireframe.drawio)

## How to Test Connection

- Docker Desktop
- Pip Installation requirements from [requirements](../app/requirements.txt)
- Source Installation
  - PostgreSQL Database for testing JDBC Connection
  - Kafka Instance for testing Kafka Connection
  - SFTP Server for testing SFTP Connection
  - Postman Server for testing Rest API Connection
- Run API application [here](./api.py)

- Using CLI or Postman Client 