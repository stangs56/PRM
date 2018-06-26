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

utf-8(command type)|utf-8(command)|utf-8(json(args))

#### Command types

| Command type | Description |
| ------------ | ----------- |
| get-info | Used for commands that request information about the client |
| run-command | Used to run commands on the remote server |
| file-system | Used to perform operations with the file system on the client |


#### Commands

##### Get Info

| Command | Description | Arguments |
| ------- | ----------- | --------- |
| uname | Python's platform.uname() which returns a named tuple (this is also the default option) | None |

##### Run Commmand

| Command | Description | Arguments |
| ------- | ----------- | --------- |
| python | Run sent text as python code | String of python code |
| cmd | Execute sent text in the command prompt | String of CMD commands |
| powershell | Execute sent text in powershell | String of powershell commands |
| bash | Execute sent text in bash | String of bash commands |
| dash | Execute sent text in dash | String of dash commands |
| default | Execute sent text in the default system shell | String of comands |

##### File System

| Command | Description | Arguments |
| ------- | ----------- | --------- |
| create-file | Create a file with a given filename and a given content | Tuple of (filename, content) |
| read-file | Send back the content of a specified file | String of filename |

