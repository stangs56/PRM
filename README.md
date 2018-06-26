# PRM

## Communication

The communication format that is used between the server and the client
is based on base64 encoded JSON or pickled python objects.  The first
part of a message is 4 bytes that signify the size of the following
message.  Base64 strings are then separated by the "|" character.
The first string is the type of command from the table of command types,
including responses to commands.

### Commands

The command is communicated using the following format:

base64(command type)|base64(command)|base64(json(args))

#### Command types

| Command type | Description |
| ------------ | ----------- |
| get-info | Used for commands that request information about the client |
| run-command | Used to run commands on the remote server |


#### Commands
