PYINSTALLER=pyinstaller
GAME_NAME=masterbagels
CONSOLE_PATH=_console
GAME_CONSOLE=$(GAME_NAME)$(CONSOLE_PATH)
ifeq ($(OS),Windows_NT)
    PYTHON=python
    WINDOWS_SOURCE=.\source\$(GAME_CONSOLE).py
    WEB_SCRIPT=build_web.py
    WEB_SOURCE=.\source\$(GAME_NAME).py
    WEB_TEMPLATE=.\source\web\index.html
    WEB_OUTPUT=.\\artifact.html
    WINDOWS_OUTPUT=.\output\windows
else
    PYTHON=python3
    LINUX_SOURCE=`pwd`/source/$(GAME_CONSOLE).py
    WEB_SCRIPT=build_web.py
    WEB_SOURCE=./source/$(GAME_NAME).py
    WEB_TEMPLATE=./source/web/index.html
    WEB_OUTPUT=./artifact.html
    LINUX_OUTPUT=`pwd`/output/linux
endif
WINDOWS_OPTIONS=--onefile --console
LINUX_OPTIONS=--onefile --console
CLEANING_FILE=clean.py


all: windows linux web

windows:
	pip install -r requirements.txt
	@echo "Building for Windows..."
	$(PYINSTALLER) $(WINDOWS_OPTIONS) $(WINDOWS_SOURCE) --distpath $(WINDOWS_OUTPUT)
	$(WINDOWS_OUTPUT)\$(GAME_CONSOLE).exe

web:
	@echo "Building for web..."
	$(PYTHON) $(WEB_SCRIPT) $(WEB_SOURCE) $(WEB_TEMPLATE) $(WEB_OUTPUT)

linux:
	@echo "Building for Linux..."
	@rm -rf /tmp/_MEI*
	@apt install -y $(PYTHON) $(PYTHON)-pip
	@$(PYTHON) -m pip install --upgrade pip
	@pip install --break-system-packages -r requirements.txt
	@$(PYINSTALLER) $(LINUX_OPTIONS) $(LINUX_SOURCE) --distpath $(LINUX_OUTPUT)
	@sudo $(LINUX_OUTPUT)/$(GAME_CONSOLE)

clean:
	@echo "Cleaning..."
	$(PYTHON) $(CLEANING_FILE)

.PHONY: all windows linux web clean