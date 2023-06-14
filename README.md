# LazyDev: Automating Coding Projects

```
Lazyness is the mother of invention 😉
```

LazyDev is a Python module that utilizes GPT models to create entire coding projects for you. With just a few simple commands, LazyDev can generate a project file tree, write the necessary code, and even test the project for you. Say goodbye to the hassle of setting up projects from scratch and let LazyDev do the heavy lifting for you.

## Features

- **Effortless project initialization**: Simply use the `lazydev develop -r "I want to develop a game"` command to kickstart the project generation process.
- **Interactive question-based approach**: LazyDev asks relevant questions to gather essential information before starting the coding process, ensuring that the generated project meets your specific requirements.
- **Complete project planning**: LazyDev plans the entire project structure based on the gathered information, setting up the necessary directories and files for you.
- **Automated code generation**: The module automatically generates the code based on the project plan, saving you time and effort.
- **Built-in testing functionality**: LazyDev even includes an automated testing phase to ensure that the generated code performs as expected.

## Installation

LazyDev requires Python 3.6 or above.
```shell
pip install lazydev
```
### setup environment 

first setup your shell with openai api key in the environment. I would recommend  adding it to your ~/.bashrc
```bash
echo 'export OPENAI_API_KEY="your_openai_key"' >> ~/.bashrc && source ~/.bashrc
```

### for zsh users:
```zsh
echo 'export OPENAI_API_KEY="your_openai_key"' >> ~/.zshrc && source ~/.zshrc
```

Replace `your_openai_key` with your openai api key 
 

## Usage

Using LazyDev is as simple as running a single command. Once installed, you can initiate the project generation process by executing the following command:

### Sample

```shell
lazydev develop --requirement REQUIREMENT
```

Replace `REQUIREMENT` with a brief description of your project's purpose or objective. LazyDev will then prompt you with a series of questions to gather the necessary information for project generation.

After answering the questions, LazyDev will proceed to plan the project structure, create the appropriate file tree, generate the required code files, and even run tests to verify the functionality.


### Flags
you can use the following flags :

*options:*

* `-h`, `--help`            show this help message and exit

* `--requirement REQUIREMENT`, `-r REQUIREMENT` # The initial requirement

* `--directory DIRECTORY`, `-d DIRECTORY` # The directory path to put generated files default is `./code`

* `--model MODEL`, `-m MODEL` # GPT Mode to use. options: gpt-3.5-turbo, gpt-3.5-turbo-16k, gpt-4. default: gpt-3.5-turbo-16k


## Example

Let's say you want to create a Python web application for managing a book library. You can use LazyDev to automate the project setup. Here's an example command:

```shell
lazydev develop -r "Book Library Web App"
```

LazyDev will ask you questions like:

- What database system would you like to use?
- What features would you like to include in your web app?
- Are there any specific libraries or frameworks you want to use?

Based on your responses, LazyDev will generate the project structure, code templates, and even a basic test suite for your book library web app.

## Contributing

Contributions are welcome! If you encounter any issues, have ideas for new features, or want to improve the existing ones, feel free to open an issue or submit a pull request on the [GitHub repository](https://github.com//thecodacus/lazy-dev).

## License

This project is licensed under the Apache-2.0 License. See the [LICENSE](https://github.com/thecodacus/lazy-dev/blob/master/LICENSE) file for more details.

## Acknowledgements

LazyDev was inspired by the desire to automate the initial setup and coding process for various projects. The underlying GPT models used in this module were developed by OpenAI.

It is inspired by the project [smol-ai/developer](https://github.com/smol-ai/developer), and the principle `Build the thing that builds all the things`

## Contact

If you have any questions or suggestions, feel free to reach out to us at thecodacus@gmail.com.

Happy coding with LazyDev!
