
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/KaiserRuben/DeepQ/master/public/logo.png" width="100" />
<br>DeepQ
</h1>
<h3>◦ Unleash the power of DeepQ!</h3>
<h3>◦ Developed with the software and tools listed below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/HTML5-E34F26.svg?style&logo=HTML5&logoColor=white" alt="HTML5" />
<img src="https://img.shields.io/badge/Chai-A30701.svg?style&logo=Chai&logoColor=white" alt="Chai" />
<img src="https://img.shields.io/badge/Vitest-6E9F18.svg?style&logo=Vitest&logoColor=white" alt="Vitest" />
<img src="https://img.shields.io/badge/Vite-646CFF.svg?style&logo=Vite&logoColor=white" alt="Vite" />
<img src="https://img.shields.io/badge/Vue.js-4FC08D.svg?style&logo=vuedotjs&logoColor=white" alt="Vue.js" />
<img src="https://img.shields.io/badge/ESLint-4B32C3.svg?style&logo=ESLint&logoColor=white" alt="ESLint" />

<img src="https://img.shields.io/badge/SemVer-3F4551.svg?style&logo=SemVer&logoColor=white" alt="SemVer" />
<img src="https://img.shields.io/badge/Python-3776AB.svg?style&logo=Python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/TypeScript-3178C6.svg?style&logo=TypeScript&logoColor=white" alt="TypeScript" />
<img src="https://img.shields.io/badge/Cypress-17202C.svg?style&logo=Cypress&logoColor=white" alt="Cypress" />
<img src="https://img.shields.io/badge/JSON-000000.svg?style&logo=JSON&logoColor=white" alt="JSON" />
</p>
<img src="https://img.shields.io/github/languages/top/KaiserRuben/DeepQ?style&color=5D6D7E" alt="GitHub top language" />
<img src="https://img.shields.io/github/languages/code-size/KaiserRuben/DeepQ?style&color=5D6D7E" alt="GitHub code size in bytes" />
<img src="https://img.shields.io/github/commit-activity/m/KaiserRuben/DeepQ?style&color=5D6D7E" alt="GitHub commit activity" />
<img src="https://img.shields.io/github/license/KaiserRuben/DeepQ?style&color=5D6D7E" alt="GitHub license" />
</div>

---

## 📒 Table of Contents
- [📒 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [⚙️ Features](#-features)
- [📂 Project Structure](#project-structure)
- [🧩 Modules](#modules)
- [🚀 Getting Started](#-getting-started)
- [🗺 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---


## 📍 Overview

The project is a game that generates and translates questions using the OpenAI GPT-3.5 Turbo model and the DeepL API. Its core functionalities include appending existing questions, generating new questions in German, translating questions to English, and saving the questions in JSON format. The purpose of the project is to provide an interactive and engaging game experience while leveraging advanced language generation and translation technologies. Its value proposition lies in the seamless integration of cutting-edge AI capabilities into a user-friendly game interface.

---

## ⚙️ Features

| Feature                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **⚙️ Architecture**     | The codebase follows a modular architecture where different files are organized based on their functionalities. It utilizes the Vue.js framework along with Ionic for building cross-platform applications. The architecture seems to be mainly based on the single-page application (SPA) concept where the UI components are built using Vue.js and Ionic components. The codebase also integrates with Capacitor, allowing the application to be built as a native iOS or Android app. The overall architecture is well-structured and follows best practices for Vue.js and Ionic development.                                                                                                                                            |
| **📖 Documentation**    | The codebase includes some comments in the code files, but there is no specific documentation file or comprehensive documentation available for the project as a whole. The comments provide basic explanations of the code structure and usage of certain components, but it would be beneficial to have more detailed documentation, especially for developers who are new to the codebase. Documenting the overall architecture, key design patterns used, and providing explanations for complex code sections would greatly improve the understanding and maintainability of the project.                                                                                        |
| **🔗 Dependencies**    | The codebase relies on several external libraries and systems. It utilizes Vue.js as the main JavaScript framework along with Ionic for building cross-platform applications. The project also uses Vite.js as the bundler and build tool. Other dependencies include `@vitejs/plugin-vue` for Vue.js support in Vite, `@vitejs/plugin-legacy` for legacy browser support, and Capacitor for cross-platform app development. Additionally, the codebase uses OpenAI GPT-3.5 Turbo model for generating questions and the DeepL API for translation purposes. These libraries and services greatly enhance the functionalities and capabilities of the project. |
| **🧩 Modularity**      | The codebase is organized into different files based on their functionalities. Each file represents a specific component or module of the application. The use of Vue.js and Ionic allows for the creation of reusable and interchangeable components, making it easier to maintain and extend the application. The codebase follows the principle of separation of concerns, with different files handling specific tasks such as routing, UI components, configuration, and data manipulation. This modularity enhances code reusability, maintainability, and testability.                                                                                                                                  |
| **✔️ Testing**          | The codebase includes a testing configuration file `cypress.config.ts` that sets up Cypress for end-to-end (e2e) testing. The configuration specifies the support file, test file pattern, folders for videos and screenshots, and the base URL for the tests. Cypress offers a powerful and comprehensive testing framework for e2e testing, allowing developers to write test cases to verify the functionality of the application. However, the provided codebase does not include actual test

---


## 📂 Project Structure




---

## 🧩 Modules

<details closed><summary>Root</summary>

| File                                                                                      | Summary                                                                                                                                                                                                                                                                                                                    |
| ---                                                                                       | ---                                                                                                                                                                                                                                                                                                                        |
| [index.html](https://github.com/KaiserRuben/DeepQ/blob/main/index.html)                   | The provided code snippet is an HTML document that sets up the structure and configuration of a web page. It includes meta tags for description, keywords, viewport settings, and iOS app integration. It also includes a link to a favicon image and a script tag to import the main TypeScript file for the application. |
| [vite.config.ts](https://github.com/KaiserRuben/DeepQ/blob/main/vite.config.ts)           | This code snippet is a Vite configuration file that uses two plugins:-`@vitejs/plugin-vue` for Vue.js support,-`@vitejs/plugin-legacy` for legacy browser support. It also sets an alias for the `@` symbol to the `./src` directory.                                                                                      |
| [capacitor.config.ts](https://github.com/KaiserRuben/DeepQ/blob/main/capacitor.config.ts) | The provided code snippet exports a configuration object for Capacitor, a cross-platform app development framework. It sets the app ID and name, the web directory, and specifies an HTTPS scheme for Android.                                                                                                             |
| [cypress.config.ts](https://github.com/KaiserRuben/DeepQ/blob/main/cypress.config.ts)     | This code snippet configures Cypress for end-to-end (e2e) testing. It specifies the support file, test file pattern, folders for videos and screenshots, and the base URL for the tests. It also allows the implementation of node event listeners.                                                                        |

</details>

<details closed><summary>Python</summary>

| File                                                                     | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ---                                                                      | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [main.py](https://github.com/KaiserRuben/DeepQ/blob/main/python/main.py) | The provided code snippet is a script that generates and translates questions for a game. It utilizes the OpenAI GPT-3.5 Turbo model to generate questions and the DeepL API to translate them. The core functionalities include appending existing questions from a JSON file, generating new questions in German, translating the questions to English, and saving the questions in JSON format. The script can be executed with different options for appending, generating, and translating questions. |

</details>

<details closed><summary>Src</summary>

| File                                                                              | Summary                                                                                                                                                                                                                                                                                                                                                                                   |
| ---                                                                               | ---                                                                                                                                                                                                                                                                                                                                                                                       |
| [App.vue](https://github.com/KaiserRuben/DeepQ/blob/main/src/App.vue)             | The code snippet is a Vue component that sets up the basic structure for an Ionic application. It includes a template with an ion-app component and an ion-router-outlet component, which serves as the container for rendering different pages/routes. The script section imports necessary Ionic components, while the style section provides basic styling for links and active links. |
| [main.ts](https://github.com/KaiserRuben/DeepQ/blob/main/src/main.ts)             | The code imports necessary dependencies and sets up an Ionic Vue app with a router. It also imports and applies CSS styles for Ionic components. The app is created and mounted to the'#app' element when the router is ready.                                                                                                                                                            |
| [vite-env.d.ts](https://github.com/KaiserRuben/DeepQ/blob/main/src/vite-env.d.ts) | The code snippet includes a reference to the Vite client types.                                                                                                                                                                                                                                                                                                                           |

</details>

<details closed><summary>Views</summary>

| File                                                                                  | Summary                                                                                                                                                                                                                                                                                                                                                                                         |
| ---                                                                                   | ---                                                                                                                                                                                                                                                                                                                                                                                             |
| [HomePage.vue](https://github.com/KaiserRuben/DeepQ/blob/main/src/views/HomePage.vue) | The code snippet is a Vue component that displays a random question and allows the user to switch between English and German languages. It fetches the questions from JSON files based on the selected language and updates the question displayed on the screen. The component also includes a helper text that appears when the user clicks on the screen, guiding them to the next question. |

</details>

<details closed><summary>Router</summary>

| File                                                                           | Summary                                                                                                                                                                                                                                                                                                                                                                                                           |
| ---                                                                            | ---                                                                                                                                                                                                                                                                                                                                                                                                               |
| [index.ts](https://github.com/KaiserRuben/DeepQ/blob/main/src/router/index.ts) | This code snippet sets up the router for an Ionic/Vue application. It imports the necessary modules, defines the routes, and creates the router object. The routes include a redirect from the root path to'/de' and a dynamic route using a language parameter. The router uses web history and the base URL provided in the environment configuration. This router is then exported for use in the application. |

</details>

---

## 🚀 Getting Started

### 📦 Installation

1. Clone the DeepQ repository:
```sh
git clone https://github.com/KaiserRuben/DeepQ
```

2. Change to the project directory:
```sh
cd DeepQ
```

3. Install the dependencies:
```sh
npm install
```

### 🎮 Using DeepQ

```sh
npm run build && node dist/main.js
```

---

## 🤝 Contributing

Contributions are always welcome! Please follow these steps:
1. Fork the project repository. This creates a copy of the project on your account that you can modify without affecting the original project.
2. Clone the forked repository to your local machine using a Git client like Git or GitHub Desktop.
3. Create a new branch with a descriptive name (e.g., `new-feature-branch` or `bugfix-issue-123`).
```sh
git checkout -b new-feature-branch
```
4. Make changes to the project's codebase.
5. Commit your changes to your local branch with a clear commit message that explains the changes you've made.
```sh
git commit -m 'Implemented new feature.'
```
6. Push your changes to your forked repository on GitHub using the following command
```sh
git push origin new-feature-branch
```
7. Create a new pull request to the original project repository. In the pull request, describe the changes you've made and why they're necessary.
The project maintainers will review your changes and provide feedback or merge them into the main branch.

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/KaiserRuben/DeepQ/blob/master/LICENSE) file for additional info.

---

