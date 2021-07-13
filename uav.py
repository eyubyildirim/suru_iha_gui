class UAV:
    def __init__(self, address, d, z) -> None:
        self.address = address
        self.d = d
        self.z = z
        pass

    def get_address(self):
        return self.address

    def get_d(self):
        return self.d

    def get_z(self):
        return self.z

    def set_address(self, address):
        self.address = address

    def set_d(self, d):
        self.d = d

    def set_z(self, z):
        self.z = z
