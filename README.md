# Real time social analysis
The project aims to perform some sentiment analysis on Twitter data. The dataset used is openly available and the main study area of [Twitter sentiment classification using distant supervision](https://www-cs.stanford.edu/people/alecmgo/papers/TwitterDistantSupervision09.pdf).
The initial idea was to fetch Twitter data in a streaming manner, but because [their platform no longer offers a free tier](https://developer.x.com/) a message producer will be used instead.
Additionally, some simple dashboards can be shown too.
In order to keep the project as open and freely available as possible, free or open data sources are used, along with open source projects. 

# Tech stack
This section briefly explains the technical details of the project.

## Infrastructure
In order to test several services, containerized applications are set up and used altogether to demonstrate their interoperability.
<img alt="architecture_diagram.png" src="docs/architecture_diagram.png" height="500" />

## Development
The project is developed using mainly DDD (Domain Drive Development) in order to ensure maintainability and robustness of the application.

| Scope        | Library     |
| -----------  | ----------- |
| Linter       | Ruff        |
| Typing       | MyPy        |
| Dependencies | uv      |

## Project structure
```
tweet-sentiment-analysis/
├── .github
│   └── GitHub Actions defined for CI/CD
├── docker
│   └── infrastructure services used in the project in a containerized environment
├── README.md
├── pyproject.toml
├── uv.lock
├── .gitignore
├── docs/
│   └── markdown files with documentation regarding the project
├── src/
│   └── services and code written in Python
└── tests/
    └── test cases
```

## CI/CD
Some GitHub Actions will be defined to check the typing, lint and formatting of the application.
The application is made to be run locally, however, checks on pull requests must be met to ensure we don't break any previous features.

# How to run?
In order to run the project, you must have Docker installed. Since the OS I used to develop it is a Windows machine, I created some helper batch scripts.
This will create several Docker containers with the different services of the application.
The main idea is that the project is auto-contained and that it can be run anywhere.

To run the project you can run in a terminal:
```batch
.\scripts\run_local.bat
```

To stop the project and drop all the containers, run in a terminal:
```batch
.\scripts\stop_local.bat
```
 