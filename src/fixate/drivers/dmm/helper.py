from abc import ABCMeta, abstractmethod, abstractproperty
from fixate.core.discover import open_visa_instrument


def open():
    """Open is the public api for the dmm driver for discovering and opening a connection
    to a valid Digital Multimeter.
    At the moment opens the first dmm connected
    :param restrictions:
    A dictionary containing the technical specifications of the required equipment
    :return:
    A instantiated class connected to a valid dmm
    """
    return open_visa_instrument("DMM")


class DMM(metaclass=ABCMeta):
    REGEX_ID = "DMM"
    is_connected = False

    def __init__(self, instrument):
        self.instrument = instrument
        self.samples = 1

    @abstractmethod
    def measure(self, *mode, trigger=True, **mode_params):
        pass

    @abstractmethod
    def measurement(self):
        pass

    @abstractmethod
    def voltage_ac(self, _range=None):
        pass

    @abstractmethod
    def voltage_dc(self, _range=None):
        pass

    @abstractmethod
    def current_ac(self, _range):
        pass

    @abstractmethod
    def current_dc(self, _range):
        pass

    def analog_filter(self, bandwidth=None):
        pass

    def digital_filter(self):
        pass

    def resistance(self, _range=None):
        raise NotImplementedError()

    def frequency(self, _range=None):
        raise NotImplementedError()

    def fresistance(self, _range=None):
        raise NotImplementedError()

    def period(self, _range=None):
        raise NotImplementedError()

    def capacitance(self, _range=None):
        raise NotImplementedError()

    def temperature(self):
        raise NotImplementedError()

    def ftemperature(self):
        raise NotImplementedError()

    def continuity(self):
        raise NotImplementedError()

    def diode(self, low_current=True, high_voltage=False):
        raise NotImplementedError()

    def samples(self, num_samples=1):
        raise NotImplementedError()

    @abstractproperty
    def range(self, set_range=None):
        pass

    @abstractproperty
    def mode(self):
        pass

    @abstractmethod
    def reset(self):
        pass
