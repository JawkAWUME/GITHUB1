from datetime import datetime

def rep_simp(input_text):
    mes_compte = str(input_text).lower()
    
    if mes_compte in ("bonjour","salut","bonsoir") :
        return "Salut ,quel bon vent t'amène ?"
    if mes_compte in ("qui es-tu ?","quel est ton nom ?") :
        return "Je m'appelle JawkBot mais tu peux m'appeler J !"
    if mes_compte in ("quelle heure est-il ?","l'heure s'il te plait ?","tu peux me donner l'heure") :
        now = datetime.now()
        temps_actuel = now.strftime("%a  %d  %B %Y ,%H:%M:%S")
        return str(temps_actuel)