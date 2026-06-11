from abc import ABC, abstractmethod

class Plugin(ABC):
    @abstractmethod
    def execute(self,text:str) -> str:
        pass
    @abstractmethod
    def get_name(self) -> str:
        pass

class SpellCheckerPlugin(Plugin):
    def __init__(self):
        self.name = "Spell Checker"
    def execute(self,text:str) -> str:
        return text.replace("teh", "the").replace("adn", "and")
    def get_name(self) -> str:
        return self.name

class WordCountPlugin(Plugin):
    def __init__(self):
        self.name = "Word Count"
    def execute(self,text:str) -> str:
        return f"Word count: {len(text.split())}"
    def get_name(self) -> str:
        return self.name

class UpperCasePlugin(Plugin):
    def __init__(self):
        self.name = "Upper Case"
    def execute(self,text:str) -> str:
        return text.upper()
    def get_name(self) -> str:
        return self.name

class TextEditer:
    def __init__(self):
        self.plugins=[]
    
    def register_plugin(self,plugin:Plugin):
        self.plugins.append(plugin)
    def run_plugins(self,text:str):
        for plugin in self.plugins:
            print(f"Running {plugin.get_name()} plugin:")
            print(plugin.execute(text))
            print()
text = "This is teh sample text with some misspelled words adn it will be processed by the plugins."
text_editor=TextEditer()
text_editor.register_plugin(SpellCheckerPlugin())
text_editor.register_plugin(WordCountPlugin())
text_editor.register_plugin(UpperCasePlugin())
text_editor.run_plugins(text)