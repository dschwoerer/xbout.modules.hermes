print("hermes got hooked")

from xbout.modules import skeleton, avail


class hermes(skeleton):
    name = "hermes-2"

    def does_match(self, ds):
        return True

    def update(self, ds):
        ds["Ti"] = ds.Pi / ds.Ne
        return ds


avail.append(hermes())
