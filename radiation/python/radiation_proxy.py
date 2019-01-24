from iotile.core.hw.proxy.proxy import TileBusProxyObject
from iotile.core.utilities.typedargs.annotate import return_type, context, param
import struct

@context("RadiationProxy")
class RadiationProxyObject(TileBusProxyObject):
    """A demo proxy object for the CoreTools walkthrough
    """

    @classmethod
    def ModuleName(cls):
        """The 6 byte name by which CoreTools matches us with an IOTile Device
        """

        return 'RProxy'

    @param("reading", "integer")
    def add_radiation_reading(self, reading):
        pass
        # TODO: implement me

    def clear_readings(self):
        pass
        # TODO: implement me


    @return_type("float")
    def get_average(self):
        pass
        # TODO: implement me

    @return_type("list(int)")
    def get_min_max(self):
        pass
        # TODO: implement me

    @return_type("float")
    def get_median(self):
        pass
        # TODO: implement me

    @return_type("int")
    def get_mode(self):
        pass
        # TODO: implement me