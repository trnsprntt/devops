# Best practices for building CI

## Github Actions

* **Keep your Actions minimal**
  
  Actions’ virtual machines have high bandwidth and are reasonably fast, but the longer an action takes to set up and run, the more time you spend waiting.

* **Don’t install dependencies unnecessarily**
  
  First, if you’re publishing a standalone Action (and working on a Node-based project), publish the entire node_modules folder in it. Second, make sure to take advantage of GitHub’s caching mechanism wherever you can. 

* **Never hardcode secrets**
  
  Set them manually in the repository settings and access them using environment variables or step inputs.

* **Limit environment variables to the narrowest possible scope**

    This becomes essential when using workflows that combine a number of Actions, jobs, and steps, as the number of environment variables can rise quickly. 

* **Store authors in Action metadata to promote code ownership**

    Metadata about actions is stored within the YML file that defines it.

* **Don’t use self-hosted runners in a public repository**

    Somebody could fork it and submit a pull request for a workflow containing malicious code.

* **Using an action instead of an inline script**
  
  To reduce attack surface.

## Jenkins

* **Always Backup The “JENKINS_HOME” Directory**
  
  Jenkins home directory contains lots of data, including job configurations, build logs, plugin configs, etc. that we cannot afford to lose. This can be accomplished through plugins offered by Jenkins or configuring a job to take backup.

* **Setup A Different Job/Project For Each Maintenance Or Development Branch Created**

  Setting up different jobs/projects for each branch helps you support parallel development efforts and maximize the advantage of sleuthing issues, thereby reducing risk and allowing developers to be more productive.

* **Prevent Resource Collisions In Jobs That Are Running In Parallel**
  
  Multiple jobs running simultaneously can cause collisions if they create a service or need exclusive access, which can bleed out your Jenkins pipeline.

* **Build A Scalable Jenkins Pipeline**
  
  Shared Libraries are perhaps the single most talked about tool to pop up across enterprises and are the pinnacle of applying DRY principles (Don’t Repeat Yourself) to DevOps. 

* **Maintain Higher Test Code Coverage & Run Unit Tests As Part Of Your Pipeline**

  Maintaining 90% of code coverage ensures better ROI by reducing UAT and product defects. Although higher coverage alone does not guarantee code quality, surfacing code coverage numbers help ensure your developers and QA defect prevention at an early stage of the life cycle.


##### Sources
###### https://www.datree.io/resources/github-actions-best-practices
###### https://docs.github.com/en/actions/learn-github-actions/security-hardening-for-github-actions
###### https://www.lambdatest.com/blog/jenkins-best-practices/
  
