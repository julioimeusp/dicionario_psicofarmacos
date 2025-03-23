# A chave do dicionário representa a categoria medicamentosa criada
# O valor da chave é a lista dos medicamentos que correspondem à categoria
# Cada linha das listas representa uma única medicação com seus diferentes nomes (não necessariamente todos existentes)
# Em geral, o primeiro nome da linha é o princípio ativo do medicamento e os outros são os nomes comerciais

classificacao_psicofarmacos = {
    "Antidepressivos \n Tricíclicos": [
        "imipramina", "tofranil",
        "clomipramina", "anafranil", "clo",
        "amitriptilina", "trytanol", "amytril", "limbitrol", "protanol",
        "nortriptilina", "pamelor",
        "maprotilina", "ludiomil"
    ],
    "Inibidores Seletivos da \n Recaptação de Serotonina": [
        "fluoxetina", "prozac", "daforin", "verotina", "fluxene", "prozen",
        "sertralina", "setralina", "zoloft", "serenata", "assert", "tolrest", "dieloft",
        "paroxetina", "aropax", "pondera", "paxil", "celebrin", "paxan", "paxtrat",  'roxetin',
        "citalopram", "cipramil", "procimax", "citta", "denyl", "maxapran",
        "escitalopram", "lexapro", "reconter", "exodus", "espran", "esc", "sedopan", "unitram",
        "fluvoxamina", "revoc", "luvox"
    ],
    "Inibidores Seletivos da Recaptação \n de Serotonina e Noradrenalina": [
        "venlafaxina", "efexor", "venlift", "venlaxin", "alenthus",
        "desvenlafaxina", "pristiq", "desve", "desduo", "desventag", "deller", "elifore", "aviv", "vellana", "andes", "imense",
        "duloxetina", "cymbalta", "velija", "neulox"
    ],
    "Inibidores da Recaptação \n de Noradrenalina e Dopamina": [
        "bupropiona", "welbutrin", "zyban", "bup", "zetron", "noradop", 'bupium'
    ],
    "Inibidores Seletivos da \n Recaptação de Noradrenalina": [
        "reboxetina", "prolift",
        'atomoxetina', 'atentah'
    ],
    "Inibidores da Monoaminoxidase": [
        "tranilcipromina", "parnate",
        "moclobemida", "aurorix"
    ],
    "Antidepressivos atípicos": [
        "trazodona", "donaren", "sonic",
        "mirtazapina", "remeron", "menelat", "razapina",
        "agomelatina", "valdoxan",
        'vortioxetina', 'voextor', 'vurtuoso', 'brintelix',
        'vilazodona',
        'esketamina', 'escetamina'
    ],
    
    "Antipsicóticos típicos": [
        "clorpromazina", "amplictil", "longactil",
        "levomepromazina", "neozine", "levozine", "meprozin",
        "flufenazina", "anatensoll", "flufenan",
        "haloperidol", "haldol",
        "tioridazina", "melleril", "unitidazin",
        "pimozida", "orap",
        'periciazina', 'neuleptil'],

    "Antipsicóticos atípicos": ["risperidona", "risperdal", "riss", "rispidon", "zargus", "risperidon",
        "olanzapina", "zyprexa", "axonium", "neupine", "zap", "zopix",
        "quetiapina", "seroquel", "neutiapim", "quetiapin", "quetros", "queropax",
        "ziprasidona", "geodon",
        "aripiprazol", "abilify", "aristab", "arpejo",
        "sulpirida", "equilid", "dogmatil", "sulpan",
        "amisulprida", "socian",
        "asenapina", "saphris",
        "clozapina", "leponex", "pinazan",
        'lurasidona', "latuda",
        'brexpiprazol', 'rexulti'
    ],

    "Estabilizadores de Humor": [
        "litio", "carbolitium", 'literata',
        "vapoico", "valproico", 'divalproato', 'divalcon', "valpi", "valproato", "torval", "depakene", "depakine", "depakote",
        "carbamazepina", "tegretol",
        "oxcarbazepina", "trileptal", "oxcarb", "oleptal",
        "lamotrigina", "lamictal", "lamitor",
        "topiramato", "topamax", "amato", "egide"],

    "Benzodiazepinicos": [
        "diazepam", "valium", "somaplus", "ansilive", "dienpax",
        "clonazepam", "rivotril", "clonotril", "clopam", "epileptil",
        "alprazolam", "alprazolan", "frontal", "apraz", "tranquinal", "altrox",
        "bromazepam", "lexotan", "somalium", "brozepax", "nervium", "novazepan",
        "lorazepam", "lorax", "lorium", "ansirax", "lorapan",
        "clobazam", "frisium", "urbanil",
        "cloxazolam", "olcadil", "elum", "anoxolan",
        "nitrazepam", "sonebon", "nitrazepol", "nitrapan",
        "flunitrazepam", "rohypnol", "rohydorm",
        "flurazepam", "dalmadorm",
        "midazolam", "dormonid", "dormire", "dormium", "hipnazolam",
        "clordiazepoxido", "psicosedin"],
    
    'Antagonistas opioides': [
        'naloxona',
        'naltrexona', 'uninaltrex'],

    "Psicoestimulantes": [
        'metilfenidato', "ritalina", "medato",  "concerta", "ragione", "foq",
        'lisdexanfetamina', "venvanse", 'juneve',
        'modafinila', 'modafinil', "stavigile"],
    
    'Anticonvulsivantes': [
        'pregabalina', 'lyrica', 'dorene', 'konduz',
        'lacosamida',
        'gabapentina',
        'levetiracetam'],
    
    'Azapironas': [
        'buspirona', 'ansitec'],
    
    'Hipnóticos \n Não Benzodiazepínicos': [
        'zolpidem', 'prysma', 'stilnox',
        'eszopiclona',
        'ramelteona', 'rozerem'],
    
    'Outras Medicações': []
    # Esta categoria é opcional, e pode abranger medicamentos fitoterapicos, antroposóficos e outros que não se encaixam nas categorias acima.
    # No projeto que deu fruto a esse dicionário, colocou-se também termos genéricos de medicamentos como "calmantes", "ansiolíticos" ou "antidepressivos".
}
    
