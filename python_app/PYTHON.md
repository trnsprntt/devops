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

## Testing Best practices

* **One Assertion in One Test Method**
  
  Fundamentally, every test asserts a hypothesis – assuming that a certain action can be undertaken by the software. To keep unit tests simple, it is best to include a single assertion in one test method.

* **Minimize Test Interdependence**

  Ensure that every test has its own setup and teardown mechanism. Test runners don’t follow a single particular order in which they run tests.

* **Automate Unit Tests**

  Testing every component of a complex, layered modern-day website or app cannot be a manual process. Tests need to be automated to run daily or even multiple times a day as part of a CI/CD pipeline. 

* **Use a Consistent Naming Convention**

  Unit tests need to be appropriately named to maintain code readability. Tests must be reasonable so that, in case of a test failure, QAs can quickly understand which particular module is malfunctioning. 

* **Ensure tests are deterministic**

  Deterministic tests are ones that exhibit the same behaviour as long as their code is unchanged.

* **Avoid Logic in Tests**

  Unit tests should be written with minimal to zero manual strings concatenation and logical conditions like while, if, switch, for, etc. Doing so reduces the chance of introducing bugs into the test. 

* **Write tests during development, not after it**
  
  Set up tests are early as possible in the sprint development cycle. This helps save time in the later stages by identifying bugs early on.

* **Group the test body into logical sections**

  A test with no logical grouping essentially is more difficult to read, therefore, it is less-maintainable.


##### Sources
###### https://www.browserstack.com/guide/unit-testing-best-practices
###### https://betterprogramming.pub/unit-testing-best-practices-9bceeafe6edf
  