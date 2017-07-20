#create a base class
class Computer:
    def __init__(self):
        self.serial = None
        self.memory = None      # in gigabytes
        self.hdd = None         # in gigabytes
        self.gpu = None

    def __str__(self):
        info = ('serial_number: {}'.format(self.serial),
        'Memory: {}GB'.format(self.memory),
                'Hard Disk: {}GB'.format(self.hdd),
                'Graphics Card: {}'.format(self.gpu))
        return '\n'.join(info)

class Tablet:
    def __init__(self):
        self.serial = None
        self.memory = None      # in gigabytes
        self.hdd = None         # in gigabytes
        self.screenSize = None

    def __str__(self):
        info = ('serial_number: {}'.format(self.serial),
        'Memory: {}GB'.format(self.memory),
                'Hard Disk: {}GB'.format(self.hdd),
                'Screen Size: {}'.format(self.screenSize))
        return '\n'.join(info)
#extend class
class ComputerBuilder:
    def __init__(self):
        self.computer = Computer()

    def configure_memory(self, amount):
        self.computer.memory = amount

    def configure_hdd(self, amount):
        self.computer.hdd = amount

    def configure_gpu(self, gpu_model):
        self.computer.gpu = gpu_model
    def configure_serial(self,computer_num):
        self.computer.serial = computer_num

class TabletBuilder:
    def __init__(self):
        self.tablet = Tablet()

    def configure_memory(self, amount):
        self.tablet.memory = amount

    def configure_hdd(self, amount):
        self.tablet.hdd = amount

    def configure_screenSize(self, screen_size):
        self.tablet.screenSize = screen_size
    def configure_serial(self,computer_num):
        self.tablet.serial = computer_num
class HardwareEngineer:
    def __init__(self):
        self.builder = None

    def construct_computer(self, serial,memory, hdd, gpu):
        self.builder = ComputerBuilder()
        [step for step in ( self.builder.configure_serial(serial),
                           self.builder.configure_memory(memory),
                           self.builder.configure_hdd(hdd),
                           self.builder.configure_gpu(gpu))]

    def construct_tablet(self, serial,memory, hdd, screenSize):
        self.builder = TabletBuilder()
        [step for step in ( self.builder.configure_serial(serial),
                       self.builder.configure_memory(memory),
                       self.builder.configure_hdd(hdd),
                       self.builder.configure_screenSize(screenSize))]

    @property
    def computer(self):
        return self.builder.computer

    @property
    def tablet(self):
        return self.builder.tablet

def main():

    print("Computer configure")
    engineer = HardwareEngineer()
    engineer.construct_computer(serial='G23385193',hdd=500, memory=8, gpu='GeForce GTX 650 Ti')
    computer = engineer.computer
    print(computer)
    print("Tablet configure")
    tabletEng = HardwareEngineer()
    tabletEng.construct_tablet(serial='G23385193',hdd=20, memory=4, screenSize=7)
    tablet = tabletEng.tablet
    print(tablet)
if __name__ == '__main__':
    main()
