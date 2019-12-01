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
This tool is a standalone tool, you will lunch it as described in [usage section](). Now we support integration with [GitHub](https://github.com/) users only.    
Once you give our tool the permission it will find out all your repositories and check its dependencies.  
When any dependency has a new version our tool will send this info through the API you configured in [configuration section]().
