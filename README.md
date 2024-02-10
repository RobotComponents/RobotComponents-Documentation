# Robot Components Documentation

[![License](https://img.shields.io/github/license/RobotComponents/RobotComponents-Documentation)]()
<a href="https://doi.org/10.5281/zenodo.5773814"><img src="https://zenodo.org/badge/DOI/10.5281/zenodo.5773814.svg" alt="DOI"></a>

This repo contains the content of [robotcomponents.github.io/RobotComponents-Documentation/](https://robotcomponents.github.io/RobotComponents-Documentation/). The documentation page is built on [Just The Docs](https://github.com/pmarsceill/just-the-docs). 

Pull requests are welcome. If you want to build the site yourself, to test your changes before opening a pull request, then please check out the getting started guide below. 

## Getting started
### Installation

1) Install Ruby (Ruby+Devkit 2.6.6-1 (x64)) from [here](https://rubyinstaller.org/downloads/).
2) Install [Bundler](https://bundler.io/) and [Jekyll](https://jekyllrb.com/).
3) Open your cmd and type in:

    ```
    $ gem install jekyll bundler
    ```
4) Navigate to your project folder and type in for installing the right bundler version:

    ```
    $ gem install bundler --version '2.0.1'
    $ bundler
    ```
5) To start the local server and create some special jekyll files when the _config.yml is changed type in:

    ```
    $ bundler exec jekyll serve
    ```
Now you can open [http://localhost:4000/](http://localhost:4000/) in your browser and test the documentation.

### Usage

[View the documentation](https://pmarsceill.github.io/just-the-docs/) of [Just The Docs](https://github.com/pmarsceill/just-the-docs) for usage information.

## Credits
![EDEK_logo](https://github.com/RobotComponents/RobotComponents-Documentation/blob/master/181101_EDEK-LOGO-01.png)

Robot Components is an open-source project that was initiated by the chair of [Experimental and Digital Design and Construction of the University of Kassel](https://www.uni-kassel.de/fb06/institute/architektur/fachgebiete/experimentelles-und-digitales-entwerfen-und-konstruieren/home). The technical development is executed by the developers and contributors who are listed [here](https://github.com/RobotComponents/RobotComponents-Documentation/blob/master/AUTHORS.md).

We forked the theme from [Just The Docs](https://github.com/pmarsceill/just-the-docs). The theme is available as open source under the terms of the [MIT License](http://opensource.org/licenses/MIT). See below for the license of the content of the documentation website. 

## License
Copyright (c) 2018-2024 [The Robot Components authors and/or their affiliations](https://github.com/RobotComponents/RobotComponents/blob/master/AUTHORS.md)

Robot Components is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License version 3.0 as published by the Free Software Foundation. 

Robot Components is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with Robot Components; If not, see <http://www.gnu.org/licenses/>.

@license GPL-3.0 <https://www.gnu.org/licenses/gpl-3.0.html>
