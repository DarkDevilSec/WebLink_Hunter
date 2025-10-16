#!/usr/bin/env bash
# ============================================
# setup.sh - Install requirements & prepare WebLink Hunter project
# Author: Ashish Prajapati
# ============================================

set -e

PROJECT_NAME="WebLink Hunter"
VENV_DIR=".venv"
USE_SYSTEM_PYTHON=0

# simple banner
print_banner() {
cat <<BANNER
${RED}  ╔═══════════════════════════════════════════╗
  ║       Web VAPT Link Harvester (CLI)       ║
  ║       Created by: Ashish Prajapati        ║
  ╚═══════════════════════════════════════════╝${NC}
BANNER
}

usage() {
  echo "Usage: $0 [--system]"
  echo "  --system    : don't create a virtualenv, install into system Python"
  exit 1
}

# parse args
if [ $# -gt 0 ]; then
  if [ "$1" = "--system" ]; then
    USE_SYSTEM_PYTHON=1
  else
    usage
  fi
fi

print_banner
echo

# check python3
if ! command -v python3 >/dev/null 2>&1; then
  echo "[!] python3 not found. Install Python 3.8+ and re-run."
  exit 1
fi

PYTHON_BIN="python3"

# create virtualenv unless user asked system install
if [ $USE_SYSTEM_PYTHON -eq 0 ]; then
  echo "[+] Creating virtualenv at ./${VENV_DIR} ..."
  ${PYTHON_BIN} -m venv "${VENV_DIR}"
  # shellcheck disable=SC1091
  source "${VENV_DIR}/bin/activate"
  PIP="${VENV_DIR}/bin/pip"
else
  echo "[!] Using system Python (no virtualenv)."
  PIP="$(command -v pip || command -v pip3)"
  if [ -z "$PIP" ]; then
    echo "[!] pip not found for system Python. Install pip and re-run or omit --system."
    exit 1
  fi
fi

# write requirements.txt
cat > requirements.txt <<'REQ'
requests
beautifulsoup4
colorama
lxml
tqdm
REQ

echo "[+] Installing Python packages from requirements.txt ..."
$PIP install --upgrade pip setuptools wheel >/dev/null
$PIP install -r requirements.txt

# create folder structure
echo "[+] Creating project folders..."
mkdir -p core
mkdir -p output/reports
mkdir -p output/logs

# create minimal core/__init__.py if missing
if [ ! -f core/__init__.py ]; then
  echo "[+] Creating core/__init__.py"
  cat > core/__init__.py <<'PYINIT'
# core package for WebLink Hunter
PYINIT
fi

# make main.py executable if it exists
if [ -f main.py ]; then
  echo "[+] Making main.py executable"
  chmod +x main.py
else
  echo "[!] main.py not found in current directory — create it before running the tool."
fi

echo
echo "========================================"
echo "Setup complete!"
if [ $USE_SYSTEM_PYTHON -eq 0 ]; then
  echo "To start using the virtualenv:"
  echo "  source ${VENV_DIR}/bin/activate"
fi
echo "Run the tool like this:"
echo "  python3 main.py"
echo "or (if main.py has shebang + executable):"
echo "  ./main.py"
echo "HTML reports will be saved to: output/reports/"
echo "Logs (if any) to: output/logs/"
echo "========================================"
