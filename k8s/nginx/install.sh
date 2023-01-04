git clone https://github.com/nginxinc/kubernetes-ingress.git --branch v2.4.2
cd kubernetes-ingress/deployments

echo "Setup "
kubectl apply -f common/ns-and-sa.yaml
kubectl apply -f rbac/rbac.yaml
kubectl apply -f rbac/ap-rbac.yaml
kubectl apply -f rbac/apdos-rbac.yaml


kubectl apply -f common/default-server-secret.yaml
kubectl apply -f common/nginx-config.yaml
kubectl apply -f common/ingress-class.yaml


kubectl apply -f common/crds/k8s.nginx.org_virtualservers.yaml
kubectl apply -f common/crds/k8s.nginx.org_virtualserverroutes.yaml
kubectl apply -f common/crds/k8s.nginx.org_transportservers.yaml
kubectl apply -f common/crds/k8s.nginx.org_policies.yaml


kubectl apply -f deployment/nginx-ingress.yaml
kubectl get pods --namespace=nginx-ingress
kubectl create -f service/nodeport.yaml


echo "Delete"
kubectl delete namespace nginx-ingress
kubectl delete clusterrole nginx-ingress
kubectl delete clusterrolebinding nginx-ingress
kubectl delete -f common/crds/
