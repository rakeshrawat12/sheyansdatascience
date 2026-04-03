class Aimodel:
    def __init__(self, name, version):
        self.name = name
        self.version = version

    def info(self):
        return f"{self.name} (version {self.version})"
    

class ollama(Aimodel):
    def __init__(self, name, version,language):
        super().__init__(name,version)
        self.language=language
    def ollama_info(self):
        return f"{self.name} (version {self.version}) and language is {self.language}"
    
ollama_model=ollama("ollama",1.0,"english")
print(ollama_model.info())
print(ollama_model.ollama_info())
ai_model=Aimodel("generic ai",0.1)
print(ai_model.info())

        
