"""Virtual IOTile device for CoreTools Walkthrough"""

from iotile.core.hw.virtual import SimpleVirtualDevice, rpc

from typedargs import iprint


import logging

class RadiationDevice(SimpleVirtualDevice):
    """A  virtual Radiation IOTile device that has RPCs that emulate what our radiation device will do
    at a high level.

    Args:
        args (dict): Any arguments that you want to pass to create this device.
    """

    def __init__(self, args):
        super(RadiationDevice, self).__init__(1, 'RProxy')
        self._logger = logging.getLogger(__name__)

    @rpc(8, 0x0004, "", "H6sBBBB")
    def controller_status(self):
        """Return the name of the controller as a 6 byte string"""

        status = (1 << 1) | (1 << 0)  # Report configured and running
        return [0xFFFF, self.name, 1, 0, 0, status]

    @rpc(8, 0x9900, "L", "")
    def add_radiation_reading(self, reading):
        """Add radiation reading to the list

        Args:
            reading (int): Reading to add to the list

        """
        # TODO: implement me

    @rpc(8, 0x9901, "", "")
    def clear_radiation_readings(self):
        """Clears radiation readings"""
        # TODO: implement me

    @rpc(8, 0x9902, "", "f")
    def get_average(self):
        """Returns the average of all readings so far.

        Returns 0 if no readings are present
        """
        # TODO: implement me

    @rpc(8, 0x9903, "", "LL")
    def get_min_max(self):
        """Returns the min and max reading seen so far.

        If there are no readings, return [0, 0].
        """
        # TODO: implement me

    @rpc(8, 0x9904, "", "f")
    def get_median(self):
        """Return median of the readings"""
        # TODO: implement me

    @rpc(8, 0x9905, "", "L")
    def get_mode(self):
        """Definition of mode : https://www.purplemath.com/modules/meanmode.htm

        For this function, we should return the mode with the lowest value, if there is one.

        If there is no mode, return 0.

        The provided unit tests should help clarify this further.
        """
        # TODO: implement me
