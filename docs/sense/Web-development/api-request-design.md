---
backlinks:
- title: Web development
  url: /memex/sense/Web-development/web-development.html
title: Designing API request mechanisms
---
## Purpose

Explore methods for designing methods for generating and handling asynchronous API request in Javascript.

## Possibilities

- [Javascript async patterns quick guide](https://www.imaginarycloud.com/blog/async-javascript-patterns-guide/) - overview not that useful, no detail for implementation except high level description
- [introducing async Javascript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous/Introducing) - mozilla
Command pattern
- [Command Pattern for Invoking REST API with Spring boot Java](https://medium.com/javarevisited/command-pattern-for-invoking-rest-api-with-spring-boot-java-39ef4eb2f568)


## Javascript async patterns quick guide

### Callbacks

### Promises

### Generators

### Async/Await asynchronous functions

- the return of an async function is a Promise
- 

## introducing async Javascript

Collection of more detailed examples.  Looking to two tasks
1. Using a promise-based API
2. Implementing a promise-based API

### Applied to Canvas APIs

CanvasAPI class which implements the promise based api
- Need to use resolve

The calling class uses promises to handle the result - doesn't know the detail.  Could this be a command?



## Command pattern

> encapsulates everythig required to take any action and allows loosely coupled execution of the action


### Spring boot Java article

ServiceCommand
- PostServiceCommand
- GetServiceCommand

All with sync and aync execution methods

Doesn't clearly show nice way of handling async



## The Plan

- Use the Command pattern, or a variation thereof - this will be an async command pattern
- constructor takes three Callbacks
    - successCallback
    - failureCallback
    - updateCallBack
- execute method is aync and will use the callbacks as required
- the execute method can figure out whether it also needs to use async or promises etc depending on the nature of the request
    - e.g. fetch would use promises and then use the callsBacks
- commands could nest sequence of commands e.g. createModuleAndItems
- specific command classes can implement additional methods to allow external folk to query the status of the command(s)

```javascript
const todaysAlarms = new MorningAlarmCommand( "David", success, failure, update);
todaysAlarms.execute();

function success() {
}

class MorningAlarmCommand {
	constructor(person, success, failure, update) {
		this.person = person;
		this.success = success;
		this.failure = failure;
		this.update = update;

	    this.alarms = []
		this.alarmsFinished = 0;
		this.alarmErrors = 0;
		this.createAlarmCommands();

		// set a timeout for when the failure should happen?
	}

    /**
	 * Create the sequence of Alarms to be set for the MorningAlarmCommand
	 */ 
	createAlarmCommands() {
		this.alarms.push( new AlarmCommand(0, this.person, 500, 
		              this.alarmWentOff(), this.alarmError())
		this.alarms.push( new AlarmCommand(1, this.person, 750, 
		              this.alarmWentOff(), this.alarmError())
		this.alarms.push( new AlarmCommand(2, this.person, 1500,
		              this.alarmWentOff(), this.alarmError())
	}

	execute() {
		this.alarms.forEach( alarm => alarm.execute() );
	}

	alarmWentOff(id) {
		this.alarms[id].alarmWentOff();
		this.alarmsFinished+=1;
		if (this.alarmsFinished===this.alarms.length) {
			this.success();
		}
		if ( (this.alarmErrors + this.alarmsFinished)===this.alarms.length) {
			this.failure();
		}
	}

	alarmError(id) {
		this.alarms[id].alarmError();
		this.alarmErrors +=1;
		if ( (this.alarmErrors + this.alarmsFinished)===this.alarms.length) {
			this.failure();
		}
	}
}
```