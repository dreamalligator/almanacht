#[Almanacht](https://github.com/digitalvapor/almanacht)

This code puts a sky gazing almanac on your desktop with conky. It uses the [digitalvapor fork of PySkyAlmanac](https://github.com/digitalvapor/PySkyAlmanac) for the functions. Thank you [atakan](https://github.com/atakan) for writing [the original awesome tool](https://github.com/atakan/PySkyAlmanac).

#Setup
There is an almanac image already included, but you'll probably want your own location, [this one is for San Francisco](https://digitalvapor.github.io/PySkyAlmanac/). Then again, San Francisco is close enough to the often-used 40°N that it might be okay with you.

1. `git clone --recursive https://github.com/digitalvapor/almanacht.git`
2. Test conky with the included image `conky -c .conky`.
3. See the [instructions](https://github.com/digitalvapor/PySkyAlmanac#instructions) for setting up your location. I recommend testing `display_bg=False` or `True` depending on your desktop background image.
4. In the `almanacht` folder, `python gen_resize.py`. This generates the png, then resizes it. Depending on your location, the almanac may be wider or skinnier and you'll want to change the `width` and `height` to keep things proportional. You can of course also just run `python skyalmanac.py` (or `shift+ENTER` if you are using the [script](https://atom.io/packages/script) package in [Atom](https://atom.io/)). Then manually resize using your image graphics tool of choice.
5. Test conky with the included image `conky -c .conky`.

#Screenshots
![screenshot0](screenshot0.png)
[background image  source](http://gate-to-nowhere.deviantart.com/art/Looking-Towards-Home-75210894)

#License
This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/).
