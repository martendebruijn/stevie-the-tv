# stevie-the-tv

Control Stevie the TV

![Reclining best friends](https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExZjB6dzN4dnM2Z3FsZGVpNGl5NGJ1Mm00NXRrb3F4OGZ2ZHFxdGZrcyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/r728rYRDDKzp6/giphy.gif)

- [stevie-the-tv](#stevie-the-tv)
  - [Install](#install)
  - [Usage](#usage)
    - [Turn Stevie ON](#turn-stevie-on)
    - [Turn Stevie OFF](#turn-stevie-off)
  - [References](#references)

## Install

1. Register with Samsung SmartThings and obtain an API key.
2. Retrieve the device ID:

```sh
curl -X GET "https://api.smartthings.com/v1/devices" \
  -H "Authorization: Bearer <API_KEY>"
```

3. Create a .env file and set the environment variables:

```sh
 cp src/.env.example src/.env
```

4. Install the `requests` module and the `python-dotenv` module for Python:

```sh
pip install requests
pip install python-dotenv
```

## Usage

### Turn Stevie ON

```sh
python src/stevie.py --turn on
```

### Turn Stevie OFF

```sh
python src/stevie.py --turn off
```

## References

- [SmartThings API](https://developer.smartthings.com/docs/api/public)
- [Capabilities reference](https://developer.smartthings.com/docs/devices/capabilities/capabilities-reference)
