# Overview

This project contains the sources for **INSERT_TYPEFACE_FAMILY_NAME_HERE**.

# Repository Contents

- `Source` &ndash; all the source materials for the font and the build script
- `Release` &ndash; the current TTF release
- `Tests` &ndash; test scripts and HMTL files for testing the released font (expected to be in the `Release` directory)
- `Artifacts` &ndash; interesting and useful artifacts generated during the project
- `azure-pipelines` $ndash; scripts for automated cloud-based builds
- `project.yaml` &ndash; the configuration file for `msfl` and the build/test process

# Getting Started

1) Clone this repository (see [Cloning this repository](#cloning-this-repository) below).

2) Follow the instructions in [Setting up the build environment](#setting-up-the-build-enironment).

3) Read through Branches.md to understand our branch naming conventions.

4) If this is a new font project, add your source files in the `Source` directory and configure `project.yaml` for your new font project.

# Cloning this repository

If you have not used git much, I recommend you take a look at the information in the Git Resources section.

1) If you haven't already, install Git.

2) If you are on a mac, you need to install the [Microsoft Git Credential Manager for OSX](https://github.com/Microsoft/Git-Credential-Manager-for-Mac-and-Linux/blob/master/Install.md).

3) Go to the project site: [https://mstypography.visualstudio.com/<project_name>](https://mstypography.visualstudio.com/<project_name>)

4) Select Repos / Files from the left menu.

5) On the right side of the screen, there is a Clone button. Click that.

6) Hit the copy button to copy the https link.

7) Use the git command-line to clone the repo:

```bash
git clone <paste URL here>
```

For example:

```bash
git clone https://mstypography.visualstudio.com/_git/NeueHaasGrotesk
```

8) To verify everything is running correctly, do the following on the command-line:

```bash
cd <project_name>   # e.g. cd NeueHaasGrotesk
git pull
```

In either step 7 or step 8, you will be given a URL to go to and a security code to type in to complete authentication. Once you have done that, you can switch to using a GUI git client app, or continue using the git command-line as you like.

If you are on a mac and get an `unexpected error` from git, see the [Troubleshooting git-credential-manager on OSX](#troubleshooting-git-credential-manager-on-OSX) section.

## Troubleshooting git-credential-manager on OSX

### Git client not responding

If you are trying to use a git client app, like one of those listed in the [Git Client apps](@git_client_apps) section below, and it does not appear to be doing anything or responding to the server, it's likely that you have not completed the authentication. Open a command prompt and run `git pull` as described in step 8 of the [Cloning this repository](#cloning_this_repository) section above. 

### Unexpected error

If you get an `unexpected error` while trying to clone a repo, the problem is very likely either that you don't have java installed, or it is a [known bug](https://github.com/Microsoft/Git-Credential-Manager-for-Mac-and-Linux/issues/71) that the credential manager tries to use Java 9 (now the default on OSX), but is built with dependencies on Java 8 runtimes. To fix this problem, do the following (this assumes you set up homebrew):

```bash
git-credential-manager uninstall
brew update                      # Get the latest homebrew indices
brew tap caskroom/versions       # lets us referene downlevel versions
brew cask uninstall java         # uninstalls Java 9
brew cask install java8          # install Java 8
git-credential-manager install
```

# Git Resources

## Git training

The following videos are helpful for beginning gitusers:

- Git for noobs. These videos are much less boring than most git videos. They do reference github, but VSO is very similar - same functionality in slightly different places in the web UI.
  - [Episode 2](https://www.youtube.com/watch?v=_ALeswWzpBo)
  - [Episode 3](https://www.youtube.com/watch?v=BKr8lbx3uFY)
  - [Episode 4](https://www.youtube.com/watch?v=JPKOESR1k04)
- [Git tutorial for beginners](https://www.youtube.com/watch?v=ugN-IYV1NTM) 
  - This includes more details.
  - Command line based, but GUIs generally have a pretty direct mapping.

## Git clients

Be sure you have the latest command-line git client:

- Windows (2.14.1 or better): [https://git-for-windows.github.io/](https://git-for-windows.github.io/)

- MacOS (2.14.1 or better): the easiest way to do this is via homebrew:

  - If you've never used homebrew, install homebrew using the following commandline:

      ```bash
      /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
      brew install git
      ```

  - If you have homebrew:

      ```bash
      brew install git
      ```

When using git, some people prefer to use a GUI-based application rather than the command line. The following are recommended:

- Mac
  - [Git fork](https://git-fork.com)
  - [Visual Studio Code](https://code.visualstudio.com/) (text editor with git integrated) 
- Windows
  - [Visual Studio Code](https://code.visualstudio.com/)
- If using Visual Studio Code
  - Add Git History plugin, too. To see history graph, go to View -> Command Palette -> type Git History -> pick which type of git history you want to see -> pick which branch you want to see.

# Branches & Source control

Please see [Branches.md](Branches.md) for a discussion of the branch naming conventions.

# Setting up the build environment

Microsoft project use the `msfontlib`/`msfl` system to build, test, regress, and package fonts. You can find detailed instructions on using msfl on the [wiki](https://mstypography.visualstudio.com/MSFontTools/_wiki/wikis/MSFontTools.wiki/).

To run `msfl` locally on your machine, you have two options:

1) Run a standalone executable. Setup is fairly easy and there are no other dependencies or system requirements. This option is slightly slower than option 2, below.

2) Install `msfontlib` as a python module in a virtual environment. For those who have a python environment and are already used to working with python modules.

## Setup instructions: Standalone executable

1. Go to the [`msfontlib` releases page](https://github.com/microsoft/msfontlib/releases) and download the latest version for your operating system.

1. Unzip the zip file, which will only contain a single file: the `msfl` executable.

1. Copy the executable to somewhere that is in your path.

   On a mac: copy the file to either `/usr/local/bin` or `/opt/homebrew/bin`, whichever is present.

   On windows: you will need to create a directory, then go to System Properties -> Environment and edit your path to include that directory.

1. To test if it works, open a command-line window and run `msfl --version`. You should see the version that you downloaded.

## Setup instructions: python module

1. Create a virtual environment for font development.

1. Clone the `msfontlib` repository somewhere

    ```bash
    git clone https://github.com/microsoft/msfontlib.git
    ```

1. Install with pip

   ```bash
   pip install -e msfontlib
   ```

# Building the font

Building the font is easy with msfl:

```bash
msfl build
```

You can find detailed instructions on using msfl on the [wiki](https://mstypography.visualstudio.com/MSFontTools/_wiki/wikis/MSFontTools.wiki/).
