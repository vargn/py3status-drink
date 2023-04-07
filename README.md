# py3status-drink
This is a py3status module that every full and half hour, for a duration of five minutes, will output a reminder to drink water.

Place module in one of these paths:
```sh
~/.config/py3status/modules
~/.config/i3status/py3status
~/.config/i3/py3status
~/.i3/py3status
```

Add this to your `i3status.conf`

```sh
order += "drink"
drink {
    external = "/path/to/drink.py"
}
```

Reload i3!
