# Plateforme de streaming

### **Contexte métier**

Une entreprise propose un service de streaming vidéo. Elle propose plusieurs types d’abonnement :
- **Basique** : lecture sur 1 appareil, pas de contenu HD
- **Standard** : lecture sur 2 appareils, HD disponible
- **Premium** : lecture sur 4 appareils, HD et Ultra HD disponibles

Chaque utilisateur peut souscrire un abonnement et a un historique de facturation. Le service veut pouvoir :

1. Créer et gérer des utilisateurs et leurs abonnements
2. Calculer le montant mensuel à facturer pour chaque utilisateur
3. Permettre la mise à jour du type d’abonnement
4. Lister tous les abonnés par type d’abonnement

---

### **Contraintes business**

- Un utilisateur ne peut avoir **qu’un seul abonnement actif**.

- Le prix des abonnements est fixe :
    - Basique : 5€/mois
    - Standard : 10€/mois
    - Premium : 15€/mois

- Si un utilisateur change d’abonnement en cours de mois, le système **ne fait pas de prorata**, il prend le tarif du nouveau mois complet.

- Chaque abonnement a un **historique des changements de prix** pour audit.


---

### **Propositions de classes avec quelques attributs**

1. **User** : représente un utilisateur
    
    - Attributs :  `customer_number`, `name`, `email`, `subscription`

2. **Subscription** : représente un type d’abonnement
    
    - Attributs : `name`, `price`, `devices`, `quality`

3. **StreamingService** : gestion des utilisateurs et abonnements
    
    - Attributs : `users`, `subscriptions`
