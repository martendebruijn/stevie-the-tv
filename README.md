# stevie-the-tv

Control Stevie the TV

![Reclining best friends](https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExZjB6dzN4dnM2Z3FsZGVpNGl5NGJ1Mm00NXRrb3F4OGZ2ZHFxdGZrcyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/r728rYRDDKzp6/giphy.gif)

- [stevie-the-tv](#stevie-the-tv)
  - [Install](#install)
  - [Usage](#usage)
    - [Switch](#switch)
      - [Turn Stevie ON](#turn-stevie-on)
        - [Successful response](#successful-response)
        - [Unsuccessful response](#unsuccessful-response)
      - [Turn Stevie OFF](#turn-stevie-off)
        - [Successful response](#successful-response-1)
        - [Unsuccessful response](#unsuccessful-response-1)
    - [Audio volume](#audio-volume)
      - [Successful response](#successful-response-2)
      - [Unsuccessful response](#unsuccessful-response-2)
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

### Switch

Turn Stevie on or off.

- **Flag**: `--turn`
- **Options**: `on`, `off`

#### Turn Stevie ON

```sh
python src/stevie.py --turn on
```

<details>
<summary>Responses</summary>

##### Successful response

```sh
Stevie is turned on!
```

##### Unsuccessful response

```sh
Error sending command: <code>
```

</details>

#### Turn Stevie OFF

```sh
python src/stevie.py --turn off
```

<details>
<summary>Responses</summary>

##### Successful response

```sh
Stevie is turned off!
```

##### Unsuccessful response

```sh
Error sending command: <code>
```

</details>

### Audio volume

Change how loud Stevie is.

- **Flag**: `--volume`
- **Options**: integer `0-100`

```sh
python src/stevie.py --volume int[0...100]
```

<details>
<summary>Responses</summary>

#### Successful response

```sh
Stevie's volume is set to {volume}!
```

#### Unsuccessful response

```sh
Error sending command: <code>
```

</details>

## References

- [SmartThings API](https://developer.smartthings.com/docs/api/public)
- [Capabilities reference](https://developer.smartthings.com/docs/devices/capabilities/capabilities-reference)
