from abc import ABC,abstractmethod
class RemoteControl(ABC):

    @abstractmethod
    def pause(self):
        pass

    @abstractmethod
    def play(self):
        pass

class TVRemoteControl(RemoteControl):

    def pause(self):
        print("TV paused")

    def play(self):
        print("TV playing")

class MusicRemoteControl(RemoteControl):

    def pause(self):
        print("Music paused")

    def play(self):
        print("Music playing")
class  RCF:

    def __init__(self,any_remote_control):
        self.any_remote_control = any_remote_control
    
    def set_remote(self,any_remote_control):
        self.any_remote_control = any_remote_control

if __name__ == "__main__":
    tv_remote = TVRemoteControl()
    music_remote = MusicRemoteControl()
    remote_control_factory = RCF(tv_remote)
    remote_control_factory.any_remote_control.play()  # Output: TV playing
    remote_control_factory.set_remote(music_remote)
    remote_control_factory.any_remote_control.play()  # Output: Music playing