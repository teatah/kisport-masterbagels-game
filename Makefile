PYTHON=python3
PYINSTALLER=pyinstaller
WINDOWS_SOURCE=.\source\masterbagels_console.py
WEB_SCRIPT=build_web.py
WEB_SOURCE=.\source\masterbagels.py
WEB_TEMPLATE=.\source\web\index.html
WEB_OUTPUT=.\\artifact.html
LINUX_SOURCE=`pwd`/source/masterbagels_console.py
WINDOWS_OUTPUT=.\output\windows
LINUX_OUTPUT=`pwd`/output/linux
WINDOWS_OPTIONS=--onefile --console
LINUX_OPTIONS=--onefile --console
CLEANING_FILE=clear.py

all: windows linux web

windows:
	pip install -r requirements.txt
	@echo "Building for Windows..."
	$(PYINSTALLER) $(WINDOWS_OPTIONS) $(WINDOWS_SOURCE) --distpath $(WINDOWS_OUTPUT)
	$(WINDOWS_OUTPUT)\masterbagels_console.exe

web:
	@echo "Building for web..."
	python $(WEB_SCRIPT) $(WEB_SOURCE) $(WEB_TEMPLATE) $(WEB_OUTPUT)

linux:
	@echo "Building for Linux..."
	@echo
	@echo "Installing python, pip, PyInstaller...\n"
	@apt install -y python3 python3-pip make
	@pip install --break-system-packages -r requirements.txt
	@echo "Done\n"
	@echo "Building Binary file..."
	@$(PYINSTALLER) $(LINUX_OPTIONS) $(LINUX_SOURCE) --distpath $(LINUX_OUTPUT)
	@echo "Done\n"
	@echo
	@echo "Built file located in $(LINUX_OUTPUT)"
	@echo

clean:
	@echo "Cleaning..."
	python $(CLEANING_FILE)

.PHONY: all windows linux web clean