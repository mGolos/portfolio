import tools.utils
import streamlit as st
sss = st.session_state


def main():        
    link1 = "(https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1004644)"
    link2 = "(https://www.sciencedirect.com/science/article/pii/S2213158216300869)"

    if sss['language'] == "fr":
        st.header("Publications Scientifiques", anchor='publications', divider="orange")
        t1, t2 = st.tabs(['Papier', 'Résumé'])
        t1.markdown(f"""
            * Golos M & al. (2015), *Multistabilité dans des modèles d'activité cérébrale à grande échelle*, PLOS Computational Biology 
            ([publication]{link1})  
            `Systèmes dynamiques`, `Réseaux de neurones`, `Analyse des réseaux`, `Connectomique`, `Entropie`, `Imagerie par résonance magnétique fonctionnelle`, `Signaux des réseaux`, `Comportement`
            
            * Wirsich J & al. (2016), *Les mesures analytiques du cerveau entier de la communication en réseau révèlent
            une corrélation structure-fonction accrue dans l'épilepsie du lobe temporal droit*, Elsevier 
            ([publication]{link2})  
            `Connectivité structurale`, `Connectivité fonctionnelle`, `Épilepsie temporale`, `Communication du réseau`, `Statistiques basées sur le réseau`
        """)
        t2.write(f"""
            #### [Multistabilité dans des modèles d'activité cérébrale à grande échelle]{link2}
            Des développements récents en imagerie cérébrale non invasive permettent de créer des cartes très détaillées des trajets axoniques, formant ainsi des réseaux réalistes pour étudier la communication régionale.  
            Insipirés par le comportement dynamique des verres de spin, nous explorons comment ces modèles de réseau traitent l'information et améliorent leurs capacités grâce à diverses études qui révèlent les motifs d'activation pendant la performance des tâches.  
            En analysant les données issues de la théorie des graphes en parallèle avec les examens en imagerie cérébrale au repos, nous découvrons les facteurs clés influençant de telles dynamiques dans les grands systèmes cérébraux.  
        """)
        t2.write("---")
        t2.write(f"""
            #### [Les mesures analytiques du cerveau entier de la communication en réseau révèlent une corrélation structure-fonction accrue dans l'épilepsie du lobe temporal droit]{link2}
            L'étude a analysé la relation entre le structure du cerveau et ses fonctions chez les patients atteints de TLE (épilepsie temporale latérale droite) à l'aide de données d'imagerie par diffusion (dMRI) et de fMRI au repos pour comprendre comment les changements dans le structure influencent leurs fonctionnalités.  
            En utilisant des métriques de communication analytiques du réseau, ils ont trouvé un réseau fonctionnel hypercorrélé largement distribué chez ces patients avec plus d'informations de recherche (search information) émanant de la connectomie structurale et une corrélation globale plus élevée entre le structure et la connectivité fonctionnelle.  
            Cela indiquait un répertoire fonctionnel moins diversifié chez les patients atteints de TLE tout en préservant le cœur du réseau, ce qui pourrait faciliter la propagation des crises.  
        """)
        
    elif sss['language'] == "en":
        st.header("Scientific Publications", anchor='publications', divider="orange")
        t1, t2 = st.tabs(['Paper', 'Abstract'])
        t1.markdown(f"""
            * Golos M & al. (2015), *Multistability in large scale models of brain activity*, PLOS Computational Biology 
            ([publication]{link1})  
            `Dynamical systems` , `Neural networks `, `Network analysis `, `Connectomics `, `Entropy `, `Functional magnetic resonance imaging `, `Signaling networks `, `Behavior`
            
            * Wirsich J & al. (2016), *Whole-brain analytic measures of network communication reveal increased
            structure-function correlation in right temporal lobe epilepsy*, Elsevier 
            ([publication]{link2})  
            `Structural connectivity`, `Functional connectivity`, `Temporal lobe epilepsy` `Network communication`, `Rich club`, `Network based statistics`
        """)
        t2.write(f"""
            #### [Multistability in large scale models of brain activity]{link2}
            Recent developments in non-invasive brain imaging enable detailed mapping of axonal tracts, forming realistic networks to study regional communication.  
            Inspired by the dynamic behavior of spin glasses, we explore how these network models process information and enhance their capabilities through various behavioral studies that reveal activation patterns during task performance.  
            By analyzing graph theory data alongside resting-state fMRI scans, we uncover key factors influencing such dynamics in large brain systems.  
        """)
        t2.write("---")
        t2.write(f"""
            #### [Whole-brain analytic measures of network communication reveal increased structure-function correlation in right temporal lobe epilepsy]{link2}
            The study analyzed the relationship between brain structure and function in rTLE patients through diffusion MRI and resting-state fMRI data, using analytical network communication metrics to understand how structural changes affect their functionality.  
            It found widespread hypercorrelated functional networks in these patients with greater search information branching from the structural connectome and higher global correlation between structural and functional connectivity.  
            This indicated a smaller functional repertoire for rTLE patients while possibly preserving pathways facilitating seizure spread.  
        """)

if __name__ == "__main__":
    utils.always()
    main()
    utils.footer()
    utils.background()
