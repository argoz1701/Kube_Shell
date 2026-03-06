# Kubernets Kubectl Shell

This is a simple shell written in python to run custome kubectl commands. 

## How To

To run save the kube_shell.py file and open a terminal form that direcroty and run the below
```
pyhton kube_shell.py --shell
```
You can run the current list of commands or simply pass a regular kubectl <command> through the shell as well.

Current wrapped comands available
```
  ?            - Current cluster
  clusters     - List configured kubectl clusters
  cpu          - List cpu usage
  dep          - List deployments across all namespaces
  dev-cluster  - Switch to Development cluster
  nodes        - List nodes
  nodes-more   - List nodes - more information
  plf-cluster  - Switch to Platform cluster
  pods         - List pods (current namespace)
```
