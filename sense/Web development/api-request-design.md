# Designing API request mechanisms

## Purpose

Explore methods for designing methods for generating and handling asynchronous API request in Javascript.

## Possibilities

Command pattern
- [Command Pattern for Invoking REST API with Spring boot Java](https://medium.com/javarevisited/command-pattern-for-invoking-rest-api-with-spring-boot-java-39ef4eb2f568)



## Command pattern

> encapsulates everythig required to take any action and allows loosely coupled execution of the action


### Spring boot Java article

ServiceCommand
- PostServiceCommand
- GetServiceCommand

All with sync and aync execution methods

Doesn't clearly show nice way of handling async