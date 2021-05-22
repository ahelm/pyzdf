FROM python:3.9

ARG dev_user=pyzdfdev
ARG home_dir=/home/${dev_user}

RUN \
  pip install -U pip \
  && pip install poetry \
  && pip install pre-commit \
  && pip install black \
  && pip install mypy \
  && pip install pylint

RUN \
  adduser \
  --disabled-password \
  --home ${home_dir} \
  "${dev_user}"

USER ${dev_user}
