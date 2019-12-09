# Depedia
[![Build Status](https://travis-ci.org/sigmaproit/depedia.svg?branch=master)](https://travis-ci.org/sigmaproit/depedia)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/270a3222bdb549d494d7797afe1cc8f4)](https://www.codacy.com/gh/sigmaproit/depedia?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=sigmaproit/depedia&amp;utm_campaign=Badge_Grade)   


**Manage your dependency**
---

## What?
Depedia is an open source tool to track/manage your dependency, we follow each dependency in your project and you will register an API to call when each dependency has a new version.  
This tool also tracks project parts, if project has many components each component has its own container and these parts are related to each other, this tool can track this type of dependency.

It also gives you a dependency graph to see your full dependency picture.   

## Why?
The motivation for this tool is the hassle of managing the local dependency for project parts, we found it would be better if there's a tool to tell us that project dependency has a new version (automatically) would save us alot of time.  
Dependency graph will give you an overall view for your project.  

## How?
This tool is a standalone tool, you will lunch it as described in [usage section](#usage). Now we support integration with [GitHub](https://github.com/) users only.    
Once you give our tool the permission it will find out all your repositories and check its dependencies.  
When any dependency has a new version our tool will send this info through the API you configured in [configuration section](#configuration).  

---

## Usage

  - **Docker-compose**:  
first of all docker-compose must be installed on deployment machine 
```bash
git clone git@github.com:sigmaproit/depedia.git
cd depedia
set -o allexport
source .env
set +o allexport
docker-compose up -d

```
depedia now is available throw port 80 (if you want to change it, change `EXPOSE_PORT` in `.env`) you can choose how to serve it.  

  - **Helm chart**:  
you must install helm client and configure it to link it with your cluster
```bash
git clone git@github.com:sigmaproit/depedia.git
cd depedia
helm install --name depedia ./depedia

```
Depedia is running right now on your cluster and ready to export frontend service with name: `frontend` using ingress.  


## Configuration  
After running depedia, now you have to configure it to start managing your dependency   
- Login with your github user and give depedia permissions to access your repositories  
- From repos page you can manage your repositories and find all dependencies for each repo, for each dependency you can set the API you want to call when it has a new version  
- Be aware of the default API if you don't want to repeat yourself, you have a default one for single repo and another one for all repos  
**Repo dependency file**
 Every repo must have a dependency file with name `DM.yml` and this's an example for this file:   
 ```
 github:
- sigmaproit/foo
- sigmaproit/bar
 ```
 put your local dependencies in this file like the example.



## Contributing
All contributions, bug reports, bug fixes, enhancements and ideas are welcome.  
To run this system locally using docker-compose you have to add this for `docker-compose.yml`
```yaml
network_mode: 'host'
```
for `backend` and `frontend` services
