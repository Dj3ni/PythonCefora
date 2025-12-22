from abc import ABC, abstractmethod

# classe abstraite
class AbstractReport(ABC):
    
    def get_header(self):
        return "Une entête générique"
    
    def get_footer(self):
        return "Un bas de page générique"
    
    # obliger les enfants doivent définir le fonctionnement de 
    # cette méthode
    @abstractmethod
    def get_content(self) -> str:
        pass

    # Une méthode concréte qui va exploiter la méthode défini
    # dans les classes qui héritent
    def display_report(self):
        print(self.get_header())
        print(self.get_content())
        print(self.get_footer())

class CustomReport(AbstractReport):
    # Définission de la méthode
    def get_content(self):
        return "Le contenu venant de la classe enfant"
    
customReport = CustomReport()
customReport.display_report()