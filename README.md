# DataSaS Project

## Description

This is project for starting up my practices when kick-off the new data project, the system will be built from fundamental stacks/services as the central of system, be connected by satellites which are modern stack via HUB that it components/API.

Some Components and RoadMap here:

1. Service Availability
Connect and Integrate to multi services
2. Pipeline Orchestration
Applying Data Processing Frameworks
3. Ontology Application
Generate Ontology and Application to end-users

System Design Principle:

- Technology Independent
- Data Security
- Requirement–Based Changes
- Data Accessible and Centralized

## System Design Components

Services Components are can be deployed to Docker and K8s

### Airbyte

Various Support Connectivity

### SuperSet

Reporting and Visualization with powered with Web Application Support

### Loki

Built with Grafana/Minio/Promtail/nginx
**Reference** [Reference](./assets/loki.png)

### Dagter/Prefect/Beam

Transformation layer with data processing frameworks and pipeline orchestration

### MinIO

MinIO is a high performance object storage solution that provides an Amazon Web Services S3-compatible API and supports all core S3 features.

MinIO is built to deploy anywhere - public or private cloud, baremetal infrastructure, orchestrated environments, and edge infrastructure.

- The MinIO Pod uses a hostPath volume for storing data. This path must correspond to a local drive or folder on the Kubernetes worker node.

- Users familiar with Kubernetes scheduling and volume provisioning may modify the spec.nodeSelector, volumeMounts.name, and volumes fields to meet more specific requirements.
- Apply the MinIO Object Definition
- applies the minio-dev.yaml configuration and deploys the objects > kubectl apply -f minio-dev.yaml
- verify the state of the pod by running > kubectl get pods -n minio-dev
- Connect your Browser to the MinIO Server: http://127.0.0.1:9090 with credentials minioadmin | minioadmin


#### Access

- Port-forward if deploy on K8s
  > kubectl port-forward minio-59fbbb4469-c8xj8 7001:9090 --namespace default
- Login to 9000 if using Docker
  Authen: minio/minio123

### KrakenD

Notes: When builds Images and links K8s Registry using > eval $(minikube docker-env)

> Setup: > install.sh
> Manual: > docker run -p 8080:8080 k8s.krakend:0.0.1 run -dc krakend.json

### Grafana

#### Access

- Port-forward if deploy on K8s
- Login to 3000 if using Docker
  Authen: admin/admin

### DataHub

### Helm

Helm is a package manager. Package managers automate the process of installing, configuring, upgrading, and removing computer programs. Examples include the Red Hat® Package Manager (RPM), Homebrew, and Windows® PackageManagement.
Helm has two elements, a client (Helm) and a server (Tiller). The server element runs inside a Kubernetes cluster and manages the installation of charts

#### Components

- Helm: A command-line interface (CLI) that installs charts into Kubernetes, creating a release for each installation. To find new charts, you search Helm chart repositories.

- Chart: An application package that contains templates for a set of resources that are necessary to run the application. A template uses variables that are substituted with values when the manifest is created. The chart includes a values file that describes how to configure the resources.

- Repository: Storage for Helm charts. The namespace of the hub for official charts is stable.

- Release: An instance of a chart that is running in a Kubernetes cluster. You can install the same chart multiple times to create many releases.

- Tiller: The Helm server-side templating engine, which runs in a pod in a Kubernetes cluster. Tiller processes a chart to generate Kubernetes resource manifests, which are YAML-formatted files that describe a resource. YAML is a human-readable structured data format. Tiller then installs the release into the cluster. Tiller stores each release as a Kubernetes ConfigMap.

### NiFi

Apache NiFi is one of the most used tools data processing tools. With a great web base GUI you can design and deploy complex datapath workflows easily.

The core package includes a lot of operators (connectors). You can get tweets for a specific hashtag, load file from S3, call a HTTP API Rest service or send a email, for example.

- cert-manager.io/cluster-issuer: “letsencrypt-prod” => We use a cert-manager cluster issuer called “letsencrypt-prod”
- nginx.ingress.kubernetes.io/backend-protocol: “HTTPS” => To indicate to nginx that the undergoing protocol is HTTPS and not HTTP by default.
- nginx.ingress.kubernetes.io/upstream-vhost: “localhost:8443” => It’s necessary to override the “Host” HTTP header to localhost:8443. In other case, Apache NiFi doesn’t reply well.
- nginx.ingress.kubernetes.io/proxy-redirect-from: “https://localhost:8443" and nginx.ingress.kubernetes.io/proxy-redirect-to: “https://nifi.example.com" => This tow rules are one in reality. It indicates to nginx that is necessary rewrite “Location” or “Refresh” header to front-end domain. If not, you’ll be redirect to “https://localhost:8443/nifi” where login is success instead of “https://nifi.example.com”


## Notes/Highlight
Deploy on Local with MiniKube
Enbale ingress service
> minikube addons enable ingress