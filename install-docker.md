# Install Docker 

In the course, we will be using Docker Desktop to work with containers on your local computer.

Docker Desktop is a tool that simplifies the process of building, running, and managing containers. It is available for Linux, macOS, and Windows operating systems.

We will reserve time in the course to troubleshoot the installation process, if you encounter any issues. Please note down any errors or issues you face during the installation. 

## Prerequisites

* **Linux:** 
   - Check Docker Desktop's specific system requirements for supported distributions: [https://docs.docker.com/desktop/install/linux-install/](https://docs.docker.com/desktop/install/linux-install/). 
   - Adminstrator / sudo privileges to install packages.

* **macOS:** 
   - macOS 12.7.4 Monterey or newer (as of March 2024). Chipsets: Intel or Apple Silicon (M1 chip or newer). Note that Docker works only on the three most recent macOS versions.
   - Adminstrator rights to install applications.

* **Windows:** 
   - Windows 11 or Windows 10 Pro/Enterprise 64-bit (Build 2004 or higher)
   - Enable the Windows Subsystem for Linux (WSL2) feature. Instructions:  [https://docs.microsoft.com/windows/wsl/install](https://docs.microsoft.com/windows/wsl/install)
   - Likely, you'll need administrator rights to install Docker Desktop on your system. If you don't have them, you may need to ask your local IT department for assistance.

## Installation Guides

The links below will take you to the official Docker Desktop installation guides for each operating system. In case of problems, have a look if the provided manuals provide help. This document provides a brief overview of the installation process for each operating system.

### Linux

For Linux, the installation process might vary depending on your distribution. 


1. **Download:** Get the Docker Desktop package for your Linux distribution from the Docker store: [https://docs.docker.com/desktop/install/linux-install/](https://docs.docker.com/desktop/install/linux-install/)
2. **Install:**  Use your distribution's package manager to install the downloaded package. Here are examples for common distributions:

Assuming, you downloaded the file `docker-desktop-4.28.0-amd64.deb`, on Ubuntu/Debian, run the following command in the terminal. 

```
cd Downloads;
sudo dpkg -i docker-desktop-4.28.0-amd64.deb
```

3. **Start Docker Desktop:** Find Docker Desktop in your application launcher and start it.


### macOS

**CPU architecture** Depending on the your Mac's architecture, you may need to download the Intel or Apple Silicon version. If your apple is newer than 2021, you likely have an Apple Silicon chip.


1. **Download:** Download the Docker Desktop for Mac installer from the Docker store: [https://docs.docker.com/desktop/install/mac-install/](https://docs.docker.com/desktop/install/mac-install/)

2. **Install:**
    * Double-click the `Docker.dmg` file.
    * Drag the Docker icon into your Applications folder.
3. **Start:** Double-click `Docker.app` in your Applications folder.
4. **Accept Terms:**  Accept the Docker Subscription Service Agreement  to continue.


### Windows

1. **Download:** Download the Docker Desktop for Windows installer from the Docker store: [https://docs.docker.com/desktop/install/windows-install/](https://docs.docker.com/desktop/install/windows-install/)
2. **Install:** 
    * Double-click `Docker Desktop Installer.exe`.
    * Follow the on-screen instructions. Ensure "Install required Windows components for WSL 2" is selected during installation.
3. **Start:** Find Docker Desktop in your Start menu and launch it.

### Post-Installation (All Systems, optional)

* **Verify installation:** Open a terminal/command prompt and run: `docker version`. This should output both client and server versions.

