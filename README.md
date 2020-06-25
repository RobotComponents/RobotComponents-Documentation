# Robot Components Documentation

[![License](https://img.shields.io/github/license/EDEK-UniKassel/RobotComponents-Documentation?style=flat-square)]()

This repo contains the content of [robotcomponents.github.io/RobotComponents-Documentation/](https://robotcomponents.github.io/RobotComponents-Documentation/). The documentation page is built on [Just The Docs](https://github.com/pmarsceill/just-the-docs). 

Pull request are welcome. If you want to build the site yourself, to test your changes before opening a pull request, then please check out the getting started guide below. 

## Getting started
### Installation

Install Ruby (Ruby+Devkit 2.6.6-1 (x64)) from [here](https://rubyinstaller.org/downloads/).

Install [Bundler](https://bundler.io/) and [Jekyll](https://jekyllrb.com/).

Open your cmd and type in:
```
$ gem install jekyll bundler
```
Navigate to your project folder and type in for installing the right bundler version:
```
$ gem install bundler --version '2.0.1'
$ bundler
```
To start the local server and create some special jekyll files when the _config.yml is changed type in:
```
$ bundler exec jekyll serve
```
Now you can open [http://localhost:4000/](http://localhost:4000/) in your browser and test the documentation.

### Usage

[View the documentation](https://pmarsceill.github.io/just-the-docs/) of [Just The Docs](https://github.com/pmarsceill/just-the-docs) for usage information.

## Credits
![EDEK_logo](https://github.com/RobotComponents/RobotComponents-Documentation/blob/master/181101_EDEK-LOGO-01.png)

The project is a development from the [Department of Experimental and Digital Design and Construction of the University of Kassel](https://edek.uni-kassel.de/). Supervised by the head of the department Prof. Eversmann. The technical development is initiated and executed by the research associates and student assistants which are listed [here](https://github.com/RobotComponents/RobotComponents-Documentation/blob/master/AUTHORS.md).

## License

We forked the theme from [Just The Docs](https://github.com/pmarsceill/just-the-docs). The theme is available as open source under the terms of the [MIT License](http://opensource.org/licenses/MIT).
