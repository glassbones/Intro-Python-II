class Content:
    def __init__(self, desc, inspection, entity):
        self.desc = desc
        self.inspection = inspection
        self.entity = entity
    
class Secret(Content):
    def __init__(self, desc, inspection, entity, requisite, isVisible = False):
        self.requisite = requisite
        self.isVisible = isVisible
        super().__init__(desc, inspection, entity)