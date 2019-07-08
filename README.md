# PRM

## Communication

The communication format that is used between the server and the client
is based on utf-8 encoded JSON or pickled python objects.  The first
part of a message is 4 bytes that signify the size of the following
message.  utf-8 strings are then separated by the "|" character.
The first string is the type of command from the table of command types,
including responses to commands.

### Commands

The command is communicated using the following format:

utf-8(command type)|utf-8(command)|utf-8(json(args))

#### Examples

Run the python command "import this"

`b'run-command|python|"import this"'`

Create a text file name 'test.txt' with content 'hello world'

`b'file-system|create-file|["test.txt", "hello world"]'`

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
| cwd | Get the current working directory on the client | None |

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
| move-file | Move a file to a new location | Tuple of (old_filepath, new_filepath) |
| rename-file | Rename a file | Tuple of (old_filepath, new_filename) |
| list-files | List files in a directory or cwd if None | String of directory or None |

