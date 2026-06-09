class CPU:
    def __init__(self, model, cores):
        self.model = model
        self.cores = cores

    def describe(self):
        # TODO: Print CPU model and core count
        print(f'  CPU: {self.model} ({self.cores} cores)')
        

class RAM:
    def __init__(self, size_gb):
        self.size_gb = size_gb

    def describe(self):
        # TODO: Print RAM size
        print('  RAM: ',self.size_gb,'GB')
        

class HardDrive:
    def __init__(self, capacity_gb):
        self.capacity_gb = capacity_gb

    def describe(self):
        # TODO: Print hard drive capacity
        print('  Storage: ',self.capacity_gb,'GB')
        

class Computer:
    def __init__(self, name, cpu_model, cpu_cores, ram_gb, storage_gb):
        self.name = name
        # TODO: Create CPU, RAM, and HardDrive internally
        self.cpu = CPU(cpu_model,cpu_cores)
        self.ram = RAM(ram_gb)
        self.hard_drive = HardDrive(storage_gb)

    def describe_specs(self):
        # TODO: Print computer name and describe all components
        print('Computer:',self.name)
        self.cpu.describe()
        self.ram.describe()
        self.hard_drive.describe()
        

    def upgrade_ram(self, new_size_gb):
        # TODO (Challenge): Replace RAM with a higher-capacity on
        self.ram.size_gb=new_size_gb

if __name__ == "__main__":
    pc = Computer("Dev Workstation", "Intel i7-13700K", 16, 32, 1000)

    pc.describe_specs()

    # Challenge: upgrade RAM and verify
    pc.upgrade_ram(64)
    print("\nAfter RAM upgrade:")
    pc.describe_specs()

    # When pc is destroyed, all components are destroyed with it.