I mean that the process for launching a task should be external to a script so that the operator has a choice of using GNU Parallel, Nomad, AWS Batch, or whatever they want without having to change any files which contain business logic.

This might mean one script that acts as an interface to manage fan-out and one script that acts as an interface to process a single chunk. These are almost always best tackled as separate concerns.
