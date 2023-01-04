helm repo add superset http://apache.github.io/superset/
helm install my-superset superset/superset

echo "Need to expose port"
# kubectl port-forward superset-xxxx-yyyy :8088