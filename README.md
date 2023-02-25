# EwCode
The most disgusting programming language!
## Usage
1. Write some code
2. Save the code as a `.ecr` file
3. Compile and run the code using `ewcode "<your ecr file>"` . Replace `<your ecr file>` with the name of the file you stored the your code in. This should generate a file with the same name, but with the `.ewc` extension. **Example:** `ewcode "test.ecr"` -> `test.ewc`

## Docker Usage
1. Pull the latest docker image with `docker pull ghcr.io/pythonsnake5036/ewcode:latest`
2. Run it with `docker run --rm -v $(pwd):/src ghcr.io/pythonsnake5036/ewcode:latest ${NAME_FILE}`
As an example, if you have a file named `test.ecr` in your working directory, run `docker run --rm -v $(pwd):/src ghcr.io/pythonsnake5036/ewcode:latest test.ecr`. This should create a file named `test.ecw` and run it.

Command breakdown:

|   Command   |   Purpose   |
| ----------- | ----------- |
| `docker run`| Starts docker to run the container |
|    `--rm`   | Removes the container after running |
| `-v $(pwd):/src`| Bind mounts your current directory to the `/src` directory on the contaainer. If you are on windows, type the full path of your current working directory |
| `ghcr.io/pythonsnake5036/ewcode:latest` | The name of the container to run |
| `${NAME_FILE}` | The name of the `.ecr` file to run |

<br /><br /><br />
**[Documentation](https://github.com/EnderixMC/EwCode/wiki)**
