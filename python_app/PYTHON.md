# Best practices for Python web-applications

## Methodology for building efficient applications

* **It could be found on <https://12factor.net/>**

## Python-related practices

* **Choose the appropriate framework**
  
  A good guideline is here <https://www.monocubed.com/top-python-frameworks/>

  Taking into consideration the nature of application and its performance expectations, I chose Flask

* **Code-quality tools**
  
  Style formatting - PEP, static analyzers - SonarCube

* **Collect all the required packages in a single file**
  
  And make sure each dependency in ```requirements.txt``` solves one major problem. If there're too many dependencies, the requirements file needs to be updated too often, otherwise, the app would not work after quite a while without updating the versions of packages.

* **Design desicions**

  ```sh
  import this
  ```

  The Zen of Python

* **Here is some more implementation-specific tips**
  
  <https://www.toptal.com/python/tips-and-practices>

## Some (a little) obvious stuff

* **Create readable documentation**

* **Use virtual environments**

* **Use ```.gitignore``` file**
  