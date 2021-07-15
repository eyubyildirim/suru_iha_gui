from uav import UAV


class UAVManagerMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class UAVManager(metaclass=UAVManagerMeta):
    def __init__(self) -> None:
        self.real_uav_count = 0
        self.virtual_uav_count = 0
        self.real_uavs = []

    def set_real_uav_count(self, count):
        self.real_uavs = []
        self.real_uav_count = count
        for i in range(count):
            self.real_uavs.append(UAV('', 0, 0))

    def set_virtual_uav_count(self, count):
        self.virtual_uav_count = count

    def set_real_uav_address(self, uav, address):
        self.real_uavs[uav].set_address(address)
    
    def set_uav_parameters(self, uav, d, z):
        self.real_uavs[uav].set_d(d)
        self.real_uavs[uav].set_z(z)
