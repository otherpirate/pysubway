import yaml

class Configurations:
    def __init__(self, store_file="default_values.yml"):
        with open(store_file, 'r') as file:
            self.configs = yaml.load(file)

        if len(self) == 0:
            raise EnvironmentError("No store in %s" % store_file)

    def first(self):
        return self.configs.keys()[0]

    def to(self, store):
        if store in self.configs:
            return self.configs[store]
        else:
            raise ValueError("Config don't found to %s" % store)

    def __len__(self):
        if self.configs:
            return len(self.configs)
        else:
            return 0
