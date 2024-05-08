> <picture>
>   <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Mqxx/GitHub-Markdown/main/blockquotes/badge/light-theme/info.svg">
>   <img alt="Info" src="https://raw.githubusercontent.com/Mqxx/GitHub-Markdown/main/blockquotes/badge/dark-theme/info.svg">
> </picture><br>
>
> All these steps would be removed after our project's integration with Docker and Amazon Simple Storage Service (Amazon S3)

## Download and Configure Ollama locally
Ollama seamlessly works on Windows, Mac, and Linux. Please follow the below steps to download Ollama:

### Installation

* Navigate to [Ollama](https://ollama.com/)
* Download Ollama on basis of your Operating System (Linux, MacOS, Windows)
* Execute the Ollama Setup Application
* Default model save path i.e `C:\Users\your_user\.ollama`

### Running Ollama (cmd)
Once Ollama is set up, you can open your cmd (command line) and pull some models locally.

* To check which models are locally available, type in cmd `ollama list`
* To server models `ollama serve`
* Ollama local dashboard (type the url in your webbrowser) `http://localhost:11434/`
* On the [Ollama Library](https://ollama.com/library), you’ll find numerous models ready for download, available in various parameter sizes.
* To pull a particular model `ollama pull model_name`
* To run a downloaded model `ollama run model_name`

## Download and run Mistral using Ollama
To install a Mistral AI model, first, you need to find the model you want to install. If you're interested in the Mistral:instruct version, you can install it directly or pull it if it's not already on your machine.

### Installation using Ollama (cmd)
* To directly run (and download if necessary) `ollama run mistral:instruct`
* To pre-download the model `ollama pull mistral:instruct`

### Running Mistral AI using Ollama (cmd)
Once the model is installed, you can interact with it in interactive mode or by passing inputs directly.

* For interactive mode `ollama run mistral --verbose`
* For non-interactive mode `ollama run mistral --verbose "Please can you explain npm:"`

Replace `"Please can you explain npm:"` with any prompt relevant to your task.

## Download and run Angular CLI

### Installation using npm (cmd)
* To install Angular CLI `npm install -g @angular/cli@12`
* To ensure the installation was successful `ng version`

### Running Angular CLI
* Creating workspace with Angular CLI `ng new my-first-angular-app`
* The above command will ask some initialization questions used to configure the workspace
```Javascript
? Would you like to add Angular routing? (y/N) N
? Which stylesheet format would you like to use?
❯ CSS
 SCSS   [ https://sass-lang.com/documentation/syntax#scss                ]
 Sass   [ https://sass-lang.com/documentation/syntax#the-indented-syntax ]
 Less   [ http://lesscss.org
```
* For the first question, type in `N` as you won’t use Angular routing for this project. Press `ENTER` key.
* In the second question, select `CSS` as the stylesheet format.
* Press `ENTER` key to initialize your project.
* Ensure you’re in the **my-first-angular-app** directory `cd my-first-angular-app`
* Next, start the web server `ng serve -o`
* At last, Angular will build your development application and expose it on a local web server at [my-first-angular-app](http://localhost:4200)

## Download and run Node.js

### Installation
* Visit [Node.js](https://nodejs.org/en/download) official download page
* Download and execute the setup application
* Verify Node.js installation `Node --version`
* And to check npm version `npm --version`

### Running Application.js using Node.js
* If your main Node.js application file is Application.js, you can call it by typing `node app.js`
* There is also a built-in option to automatically restart the application when a file changes `node --watch app.js
`
## Install all packages using requirements.txt

### Installation
* Run the following command where the requirements.txt file is present `pip install -r requirements.txt`
* [PIP](https://www.geeksforgeeks.org/how-to-install-pip-on-windows/) will download and install all packages present in that file.

## Make the following change in the package
```Python
.venv -> lib > python3.10 -> site-packages -> pytube -> cipher.py:line 30 -> regex change - r"^\$*\w+\W"
```
