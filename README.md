# utility-server
Small and free server for some common task for deploying at https://deta.sh

## Features

- [x] Compute favhash
- [ ] Basic https://requestbin.net feature
- [x] RCE

## How to deploy

1. Create new account at https://www.deta.sh/ an instal deta-cli locally to your machine.
2. Login to deta with `deta login`
3. Create new micro:

```
deta new --python --name my-utility-server
```

4. Copy source code in this repo to `my-utility-server`
5. Run `deta deploy` and check dashboard for your micro link (something like `https://xxxxxx.deta.dev/`)
