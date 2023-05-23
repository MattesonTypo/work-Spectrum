Testing Pop
Trigger again

This project contains the sources for a revival of Bembo.

# Repository Contents

- `Source` &ndash; all the source materials for the font and the build script
- `Release` &ndash; the current TTF release
- `Tests` &ndash; test scripts and HMTL files for testing the released font (expected to be in the `Release` directory)
- `Artifacts` &ndash; interesting and useful artifacts generated during the project
- `azure-pipelines` $ndash; scripts for automated cloud-based builds

# Getting Started

1) Clone this repository (see [Cloning this repository](#cloning-this-repository) below).

2) Follow the instructions in [Setting up the build environment](#setting-up-the-build-enironment).

3) Read through Branches.md to understand our branch naming conventions.

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

The build enviroment uses python3. It is highly recommended to use python virtual environments to set everything up. Virtual environments are a container for python libraries. In addition to keeping everything tidier, and not having to use `sudo` to install libraries, virtual environments allow you to keep different versions of python libraries side by side. This is particularly useful for font development tools. The primary python libraries used by this build process, fontTools and fontmake, are in very active development and change rapidly. Virtual environments give you a way to keep a stable, tried and true version, and a bleeding-edge or development version, and easily switch between the two. 

This build environment saves the version of tools used to make a font in the bild tag of the font’s meta table. This makes it easy to track down how a given font was made.

## System requirements

### Mac

- Python 3.7
- Homebrew

### Windows

- Python 3.7

## Setup instructions

1. If you are not already using python virtual environments, create the directory in which to store all your virtual environments. In the examples below, we will assume you are using `~/py-env` (mac), or `\python\py-env (win)`.

   ```bash
   mkdir ~/py-env
   ```

2. Create a virtual environment for this project (e.g neuehaas).

   ```bash
   python3 -m venv ~/py-env/neuehaas
   ```

3. Activate the virtual environment.

   Mac:

   ```bash
   source ~/py-env/neuehaas/bin/activate
   ```

   Windows:

   ```cmd
   \python\py-env\neuehaas\scripts\activate
   ```

   Your prompt should change to show the name of your active virtual environment `(neuehaas)`.

4. Install the required python libraries. The following assumes you have cloned the repository to ~/git/NeueHaasGrotesk

   ```bash
   cd ~/git/NeueHaasGrotesk
   pip3 install -r requirements.txt
   ```

# Building the font

First, set up the build environment as described in [Setting up the build environment](#setting-up-the-build-enironment), above.

1. Activate the virtual environment if you haven't already

   Mac:

   ```bash
   source ~/py-env/neuehaas/bin/activate
   ```

   Windows:

   ```cmd
   \python\py-env\bin\activate
   ```

   Your prompt should change to show the name of your active virtual environment `(neuehaas)`.

2. Go to the Source directory of your local repository (e.g. `~/git/NeueHaasGrotesk/Source`)

   ```bash
   cd ~/git/NeueHaasGrotesk/Source
   ```

3. Build the font as follows:

   ```bash
   python3 build.py
   ```

   The fonts will be placed in the project's `Release` directory.

   By default, the build script will build the roman and the italic, but only if the UFO files are newer than the corresponding TTFs. You can force the build script to build the TTFs regardless of the UFOs date by including the `--force` parameter.

   You can also build individual fonts by specifying the target on the command-line:

    ```bash
    python3 build.py roman
    ```

4. On a Windows machine, load the fonts in VTT, hit Tools/Compile/Compile Everything for All Glyphs. Save the font, and Tools/Ship the font to produce the final binary font for shipment.

## Build targets

- `roman` &ndash; the Roman version of the font.
- `italic` &ndash; the Italic version of the font.

## Hinting the fonts
The build process integrates TT hints stored in TTF files (`Source/vtt`). 