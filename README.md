# Port Scanner Lab

Simple port scanner for your own machine or authorized lab environments.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
port-scan scan 127.0.0.1 --ports 22,80,8000,8001
```
