# Python Utilities Repository

Welcome to the Python Utilities Repository. This repository contains various Python utility scripts designed to perform specific tasks efficiently. Each utility is organized into its own directory with a `main.py` script and a corresponding `parameters.yaml` file for configuration.

## Table of Contents

- [Getting Started](#getting-started)
- [Available Utilities](#available-utilities)
- [Running Utilities](#running-utilities)
- [Configuration](#configuration)
- [Adding a New Utility](#adding-a-new-utility)
- [Contributing](#contributing)
- [License](#license)
- [Support](#support)

## Getting Started

To get started with the Python Utilities Repository, you'll need to clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/python-utils.git
cd python-utils
```

Ensure you have Python 3.x installed on your system. You can verify this by running:

```bash
python3 --version
```

Additionally, you’ll need yq to parse YAML files. You can install yq via Homebrew:

```bash
brew install yq
```

## Available Utilities

### 1. Replace Space Folders
- Description: This utility removes spaces in folder names and optionally replaces them with a specified character.
- Location: `replace_space_folders/`
- Usage: See [Running Utilities](#running-utilities) for instructions.

## Running Utilities

To run a utility, you can use the provided shell script `run.sh`, which dynamically loads the parameters needed for the chosen utility. Follow these steps:

1. Make the script executable:
```bash
chmod +x run.sh
```
2. Run the script:

```bash
./run.sh
```
or
```bash
sh run.sh
```

3. Follow the on-screen instructions to select a utility and provide the required parameters.

The script performs the following:
- **Lists Available** Utilities: Scans directories to list utilities that have a `main.py` script.
- **Prompts for Parameters**: Reads the `parameters.yaml` file in the chosen utility's directory to prompt the user for necessary inputs.
- **Executes the Utility**: Runs the `main.py` script with the user-provided parameters as command-line arguments.

### Example Output
The shell script will display available utilities and request input as follows:

```plaintext
Available utilities:
1. replace_space_folders
2. second_util_test
Enter the number of the utility you want to use: 
```

## Configuration

Each utility requires specific parameters defined in its `parameters.yaml` file. The script `run.sh` automatically reads these parameters and prompts the user for input.\
Here's an example configuration file:

```yaml
parameters:
  folder_route:
    description: An absolute route to the folder you want to remove the spaces
  replace_char:
    description: The default is an empty string, but you can provide any char to replace the spaces
```

## Adding a New Utility

To add a new utility:

1. **Create a New Directory**: Make a new directory for your utility.

```bash
mkdir new_utility_name
cd new_utility_name
```

2. **Add a `main.py` Script**: Implement your utility's functionality in a main.py script. Ensure it accepts command-line arguments for parameters.

3. **Create `parameters.yaml`**: Define the parameters required by your utility in a `parameters.yaml` file.

```yaml
parameters:
  new_param:
    description: Description of what the parameter does
```

4. **Verify and Test**: Make sure your utility works as expected by testing it using the `run.sh` script.

## Contributing

Contributions are welcome! Please follow these guidelines:

1. **Fork the Repository**: Click the "Fork" button at the top right of the GitHub page.

2. **Create a Branch**: Create a new branch for your feature or bug fix.

```bash
git checkout -b feature/your-feature-name
```

3. **Commit Your Changes**: Make and commit your changes with a clear commit message.

```bash
git commit -m 'Add your feature or fix'
```

4. **Push to the Branch**: Push your changes to your forked repository.

```bash
git push origin feature/your-feature-name
```

5. **Open a Pull Request**: Go to the original repository on GitHub and open a pull request.

Please ensure all new code includes appropriate tests and documentation. Follow the coding style and conventions used in the existing codebase.

## License

This repository is licensed under the MIT License. See the LICENSE file for details. (no actual license)

## Support

If you have any questions or encounter issues, please open an issue in the repository.


## Explanation of Best Practices Included

- **Clear Structure:** The document is organized into sections that users commonly look for, such as installation instructions, usage, configuration, contribution guidelines, and support information.

- **Detailed Instructions:** Step-by-step instructions are provided for getting started, running utilities, and adding new utilities, making it easy for users to follow.

- **Code Examples:** Code snippets are included to demonstrate commands and file structures, which help users understand how to use the utilities and configure them properly.

- **Contribution Guidelines:** Clear steps are provided for contributing, encouraging community involvement and ensuring contributions align with the project's standards.

- **Contact Information:** Users are informed on how to get support or report issues, fostering a helpful and responsive community around the project. 

Feel free to adjust the content according to your specific needs and update sections like URLs, contact emails, or any other specific details related to your repository.