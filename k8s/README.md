## Minikube

###### To make LoadBalancer run locally (my system is not attached to any cloud provider with LB service available) I ran `minikube tunnel` 

#### Output before configuration files creation:

```
kubectl get pods

kubectl get svc
```

![](https://i.imgur.com/nTtuzZi.png)


#### Output after configuration files creation:

```
kubectl get pods

kubectl get svc
```

![](https://i.imgur.com/tN0DaDU.png)


### Bonus

![](https://i.imgur.com/sgb7iHR.png)


**Ingress** is an API object that makes it possible to manage all the routing rules from a single resource. The request from outside the cluster at first comes to the ingress controller and only after that, according to a routing rule defined in ingress, reaches Kubernetes services.

**Ingress controller** is the resource in a Kubernetes cluster that is responsible for fulfilling the ingress routing protocols.

**StatefulSet** controls stateful applications. It manages the deployment and scaling of a set of Pods, and also guarantees uniqueness of these Pods. Every replica of a stateful set will have its own state, and each of the pods creates its own Persistent Volume Claim. 

**DaemonSet** is a controller that ensures that the pod runs on all the nodes of the cluster. If a node is added or removed from a cluster, DaemonSet automatically manages the same atste on all the other nodes.

**Persistent Volume Claim** is like a virtual Persistent Volume. PVC is capable of requesting a specific type of resources in a Persistent Volume such as a particular size or permissions.

## Helm

![](https://i.imgur.com/WjkjVF7.png)

### Bonus

![](https://i.imgur.com/dTK6Axj.png)

Helm charts were originally invented to reduce the need to repeat yourself while dealing with Kubernetes manifests. So **Library Charts** went even further and intend to help developers follow DRY principle in Helm charts. Code snippets could be shared along using Library charts. 