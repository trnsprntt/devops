# Best practices for writing Dockerfiles

* **Use explicit and deterministic Docker base image tags**
  
  It is done to prevent unexpected behaviour and security issues. Use the Docker image digest, which is the static SHA256 hash of the image. This ensures that you are getting deterministic Docker image builds from the base image.

* **Don’t run containers as root**
  
  In this case I skipped it, since it added much overhead to the size of image (and there're no potential threat to providing extra privileges for showing time)

* **Use multi-stage builds**
  
  To avoid leaking sensitive information and reduce production image size.

* **Keeping unnecessary files out of  Docker images**

  Use ```.dockerignore``` files

* **Mind the order of instructions**

  First execute the ones that are less likely to change, then others

* **Use images scanning by Snyk**
  
  This is the oficial recommendation on <docker.com>
