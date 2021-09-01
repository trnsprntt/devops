# Best practices for building infrastructure with Terraform

* **Don’t commit the .tfstate file**
  
  Firstly, you could be exposing secrets from your application configuration, such as  passwords, database connection strings. And secondly, you risk executing Terraform against stale or old state that you forgot to pull down from version control.

* **Configure a backend**

  Backends broadly speaking have two main features: state locking and remote state storage. Locking prevents two executions happening at the same time. And remote state storage allows you to put your state in a remote, yet accessible location.

* **Back up your state files**
  
  As your state file is the engine that drives your configuration it makes sense to ensure that the location where you store your state is backed up. Backed up state makes it easier to revert to a previous state if you make a mistake.

* **Keep your backends small**
  
  Keeping all your configurations together introduces risk, as you have the ability to introduce unwanted changes to other infrastructure when you apply your changes. To break down your infrastructure simply create new Terraform projects (and therefore new state).

* **Use one state per environment**
  
  Breaking down by envioronment reduces risk when you apply changes.

* **Setup backend state locking**
  
  State locking prevents two mutating commands, such as terraform apply operating on the same state file at the same time.

* **Execute Terraform in an automated build**
  
  Running code in an automated build tool has many advantages, which includes having a repeatable process, and a history of changes. 

* **Manipulate state only through the commands**

  The Terraform CLI gives you commands that allow you to remove, or move (terraform state rm and terraform state mv)

* **Use variables**

  Be sure to go find any repeating values in your configuration, such as environment names, or prefixes and store them in variables.

* **Use modules (only where necessary)**

  Terraform modules allow you to break down infrastructure configurations into shared blothecks. 

* **Maintain a strict policy of reviewing terraform validate and plan outputs before allowing terraform changes to be applied to an environment.**

  This command will give you a chance to catch and resolve any issues in the code before you modify your cloud environment.

##### Sources
###### https://openupthecloud.com/terraform-best-practices/
###### https://www.xtivia.com/blog/cloud/terraform-best-practices/