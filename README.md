# Kubernetes Kubectl Shell

This is a simple shell written in python to run custome kubectl commands. This is a project for myself to try and git better at python and is most used for my own specific use case while working with Kubernetes.

## Install
```
pip install https://github.com/danswest/Kube_Shell.git
```
### Required Dependencies 
- Python version 3.9 or newer

- Pip

- Git

- kubectl

## How To

To run the script after the installation do the below:
```
kubesh # to start the script
kubesh --help # to open the help menu 
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
