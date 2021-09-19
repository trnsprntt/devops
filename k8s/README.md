#### Output before configuration files creation:

```
kubectl get pods

kubectl get svc
```

![](https://i.imgur.com/4EkLMyK.png)

#### Output after configuration files creation:

```
kubectl get pods

kubectl get svc
```

![](https://i.imgur.com/348bgsL.png)


### Bonus

![](https://i.imgur.com/IGcUJb1.png)



**Ingress** is an API object that makes it possible to manage all the routing rules from a single resource. The request from outside the cluster at first comes to the ingress controller and only after that, according to a routing rule defined in ingress, reaches Kubernetes services.

**Ingress controller** is the resource in a Kubernetes cluster that is responsible for fulfilling the ingress routing protocols.

**StatefulSet** controls stateful applications. It manages the deployment and scaling of a set of Pods, and also guarantees uniqueness of these Pods. Every replica of a stateful set will have its own state, and each of the pods creates its own Persistent Volume Claim. 

**DaemonSet** is a controller that ensures that the pod runs on all the nodes of the cluster. If a node is added or removed from a cluster, DaemonSet automatically manages the same atste on all the other nodes.

**Persistent Volume Claim** is like a virtual Persistent Volume. PVC is capable of requesting a specific type of resources in a Persistent Volume such as a particular size or permissions.