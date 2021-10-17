#!/bin/bash -e

OP_ROOT=$(git rev-parse --show-toplevel)

sudo apt-get update && sudo apt-get install -y --no-install-recommends \
  curl \
  git \
  python-dev \
  python3-pip \
  sudo \
  wget


# install pyenv
if ! command -v "pyenv" > /dev/null 2>&1; then
  curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
fi

# taking care of submodules
git submodule init
git submodule update

# install python
PYENV_PYTHON_VERSION=$(cat "$OP_ROOT"/.python-version)
PATH=$HOME/.pyenv/bin:$HOME/.pyenv/shims:$PATH
pyenv install -s "${PYENV_PYTHON_VERSION}"
pyenv global "${PYENV_PYTHON_VERSION}"
pyenv rehash
eval "$(pyenv init -)"


# **** in python env ****
pip install --upgrade pip==20.2.4
pip install pipenv==2020.8.13
pipenv install --dev --system --deploy

echo
echo "----   FINISH DEVELOPER SETUP   ----"
echo "source ~/.bashrc"
