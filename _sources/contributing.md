# Contributing

This guide describes how to contribute to the HoloViz tutorial.

If you have any problems with the steps here, please reach out in the `dev` channel on [Discord](https://discord.gg/rb6gPXbdAr) or on [Discourse](https://discourse.holoviz.org/).

## TL;DR

0. Open an [issue on Github](https://github.com/holoviz/tutorial/issues) if needed
1. Fork and clone [tutorial's Github repository](https://github.com/holoviz/tutorial)
2. Install [`pixi`](https://pixi.sh)
3. Run `pixi run lint-install` to set up `pre-commit`
4. Run `pixi run lab` (for Jupyter Lab) or `pixi run notebook` (for Jupyter Notebook) to create the working environment and launch Jupyter.
5. Make some changes and run:
  - `pixi run test-example` if you updated the notebooks to run them
  - `pixi run docs-build` if you need to build the website locally
6. Open a Pull Request

## Preliminaries

### Basic understanding of how to contribute to Open Source

If this is your first open-source contribution, please study one
or more of the below resources.

- [How to Get Started with Contributing to Open Source | Video](https://youtu.be/RGd5cOXpCQw)
- [Contributing to Open-Source Projects as a New Python Developer | Video](https://youtu.be/jTTf4oLkvaM)
- [How to Contribute to an Open Source Python Project | Blog post](https://www.educative.io/blog/contribue-open-source-python-project)

### Git

The Tutorial source code is stored in a [Git](https://git-scm.com) source control repository. The first step to working on the Tutorial is to install Git onto your system. There are different ways to do this, depending on whether you use Windows, Mac, or Linux.

To install Git on any platform, refer to the [Installing Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) section of the [Pro Git Book](https://git-scm.com/book/en/v2).

To contribute to the Tutorial, you will also need [Github account](https://github.com/join) and knowledge of the [_fork and pull request workflow_](https://docs.github.com/en/get-started/quickstart/contributing-to-projects).

### Pixi

Developing all aspects of the Tutorial requires a wide range of packages in different environments, but for new contributors the `default` environment will be more than enough.

To make this more manageable, Pixi manages the developer experience. To install Pixi, follow [this guide](https://pixi.sh/latest/#installation).

## Detailed workflow

### Cloning the Project

The source code for the Tutorial is hosted on [GitHub](https://github.com/holoviz/tutorial). The first thing you need to do is clone the repository.

1. Go to [github.com/holoviz/tutorial](https://github.com/holoviz/tutorial)
2. [Fork the repository](https://docs.github.com/en/get-started/quickstart/contributing-to-projects)
3. Run in your terminal: `git clone https://github.com/<Your Username Here>/tutorial`

The instructions for cloning above created a `tutorial` directory at your file system location.
This `tutorial` directory is the _source checkout_ for the remainder of this document, and your current working directory is this directory.

### Install pixi

Install [`pixi`](https://pixi.sh).

## Linting

The Tutorial uses [`pre-commit`](https://pre-commit.com/) to lint and format the source code. `pre-commit` is installed when running `pixi run lint-install`.
`pre-commit` runs all the linters when a commit is made locally. Linting can be forced to run for all the files with:

```bash
pixi run lint
```

:::{admonition} Note
:class: info

Alternatively, if you have `pre-commit` installed elsewhere you can run:

```bash
pre-commit install  # To install
pre-commit run --all-files  # To run on all files
```

:::

## Jupyter

Open the notebooks with Jupyter by running:
- `pixi run lab` for Jupyter Lab
- `pixi run notebook` for Jupyter Notebook

These tasks run in the `default` environment.

## Testing

The Tutorial's documentation consists mainly of Jupyter Notebooks. Testing is implemented on the Tutorial by running the notebooks with pytest and [nbval](https://nbval.readthedocs.io/). The tests pass if all the notebooks run without error. These tests can be run with the following command:

```bash
pixi run test-example
```

## Documentation

The documentation can be built with the command:

```bash
pixi run docs-build
```

A development version of the Tutorial can be found [here](https://holoviz-dev.github.io/tutorial/).

## Continuous Integration

Every push to the `main` branch or any PR branch on GitHub automatically triggers a test build with [GitHub Actions](https://github.com/features/actions). This also triggers a docs build of the [development site](https://holoviz-dev.github.io/tutorial/).

You can see the list of all current and previous builds at [this URL](https://github.com/holoviz/tutorial/actions)

### Etiquette

GitHub Actions provides free build workers for open-source projects. A few considerations will help you be considerate of others needing these limited resources:

- Run the tests locally before opening or pushing to an opened PR.

- Group commits to meaningful chunks of work before pushing to GitHub (i.e., don't push on every commit).
