# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 20:18:53 2016

@author: juang
Entra un archivo de texto con lineas de tweet que pertenecen a un tema especifico,
ejemplo Ambiente.txt y devuelve el numero de veces que aparecen las palabras relevantes.
"""
def CuentaTemaa():
#    from __future__ import division
    import re, string
    import operator
    import unicodedata
    import math
    
    def remove_punctuation ( text ):
        return re.sub('[%s]' % re.escape(string.punctuation), ' ', text)
    def sigmoid(x):
        return 1 / (1 + math.exp(-x))
    
    # convierte es.lexicon.txt en Diccionario llamado Lexico
    Lexico = {}
    with open('es-lexicon.txt') as f:
        for line in f:
           (key, val) = line.split()
           Lexico[key] = val
           
    # return Lexico
           
    # Remueve puntuación del texto T y luego crea ListaTexto con las palabras
    with open('Ambiente.txt', 'r') as myfile:
        Texto=myfile.read().replace('\n', '')
                           
    Texto=remove_punctuation (Texto)    
    
    ListaTexto=Texto.split();
    # Los tags que queremos contar
#    Tags=['NP','NCO','NCN','NCP','NCS','AQ',
#    'AO','W','I','NewCat','ZM','ZP','ZU']; 
    Tags=['NP','NCO','NCN','NCP','NCS',
          'W','I','NewCat','ZM','ZP','ZU']; 
    #Ciclo que cuenta
    wc={};
    for word in ListaTexto:
        try:
            tag=Lexico[word]
        except:
            Lexico[word]='NewCat'
            tag=Lexico[word]
        
        if tag in Tags:
            wc.setdefault(word,0)
            wc[word]+=1
        else:
            wc.setdefault(word,0)
            wc[word]=0  
            
 
    #El mundo y los temas se reinventan, por eso es necesario añadir a mano algunas palabras que se
    #intuya que deberían estar. Adicionalmente eliminar algunas otras que no discrecionalmente
    #se piense que no deben definir un tema
    wc.pop('Colombia',None); wc.pop('cifra',None);wc.pop('Queremos',None); wc.pop('NO',None);
    wc.pop('colombianos',None); wc.pop('colombiano',None);wc.pop('desvío',None); wc.pop('lamentable',None);
    wc.pop('Grande',None); wc.pop('ilegal',None);wc.pop('responsable',None); wc.pop('vehículos',None);
    wc.pop('Bogotá',None); wc.pop('Peñalosa',None);wc.pop('ciencia',None); wc.pop('Alexander',None);
    wc.pop('Santa',None); wc.pop('Marta',None);wc.pop('fenómeno',None); wc.pop('nevados',None);
    wc.pop('semana',None); wc.pop('JuanManSantos',None);wc.pop('Caquetá',None); wc.pop('médico',None);
    wc.pop('manuel',None); wc.pop('Santos',None);wc.pop('agroindustrial',None); wc.pop('car',None);
    wc.pop('paz',None); wc.pop('Paz',None);wc.pop('acuerdo',None); wc.pop('beneficios',None);
    wc.pop('país',None); wc.pop('al',None);wc.pop('zonas',None); wc.pop('Nacional',None);
    wc.pop('LA',None); wc.pop('canchas',None);wc.pop('consulta',None); wc.pop('Chipatecua',None);
    wc.pop('2015',None); wc.pop('años',None);wc.pop('derecho',None); wc.pop('artesanales',None);
    wc.pop('debate',None); wc.pop('oro',None);wc.pop('VPQpc4wVfM',None); wc.pop('anual',None);
    wc.pop('agua',None); wc.pop('dos',None);wc.pop('Tunjuelito',None); wc.pop('gato',None);
    wc.pop('Van',None); wc.pop('ambiente',None);wc.pop('detrimento',None); wc.pop('Nacional',None);
    wc.pop('Ambiente',None); wc.pop('río',None);wc.pop('licencia',None); wc.pop('nuevos',None);
    wc.pop('Reserva',None); wc.pop('reserva',None);wc.pop('Presidente',None); wc.pop('cifras',None);
    wc.pop('solo',None); wc.pop('EnLíneaConElPresidente',None);wc.pop('estado',None); wc.pop('Col',None); 
    wc.pop('mundo',None); wc.pop('Congreso',None);wc.pop('conflictos',None); wc.pop('síntesis',None);
    wc.pop('municipios',None); wc.pop('EnriquePenalosa',None);wc.pop('Isabel',None); wc.pop('fundamental',None);
    wc.pop('Alcalde',None); wc.pop('sistema',None);wc.pop('alto',None); wc.pop('exploración',None);
    wc.pop('100',None); wc.pop('proyecto',None);wc.pop('grande',None); wc.pop('Encuentro',None);
    wc.pop('ColombiaDiceSí',None); wc.pop('natural',None);wc.pop('Parque',None);
    wc.pop('der',None);  wc.pop('área',None);wc.pop('territorios',None);wc.pop('conflicto',None);
    wc.pop('cambio',None); wc.pop('lucha',None);wc.pop('Santuario',None);wc.pop('importante',None);
    wc.pop('incendios',None); wc.pop('salud',None); wc.pop('áreas',None); wc.pop('Foro',None);
    wc.pop('población',None); wc.pop('artículo',None); wc.pop('niños',None); wc.pop('piloto',None);
    wc.pop('AlAire',None); wc.pop('Frente',None); wc.pop('año',None); wc.pop('Brasil',None);
    wc.pop('comunidad',None); wc.pop('Frente',None); wc.pop('bosque',None); wc.pop('crisis',None);
    wc.pop('html',None); wc.pop('Frente',None); wc.pop('economía',None); wc.pop('protección',None);
    wc.pop('cultivosRT',None); wc.pop('cultivos',None); wc.pop('reporte',None); wc.pop('Latina',None);
    wc.pop('ojos',None); wc.pop('¿Qué',None); wc.pop('ríos',None); wc.pop('América',None);
    wc.pop('Región',None); wc.pop('Planeta',None); wc.pop('Análisis',None); wc.pop('Gestión',None);
    wc.pop('PaolaHolguin',None); wc.pop('Ártico',None); wc.pop('Informe',None); wc.pop('Internacional',None);
    wc.pop('riñon',None); wc.pop('meta',None); wc.pop('MashiRafael',None); wc.pop('Tasa',None);
    wc.pop('nacion',None); wc.pop('defensa',None); wc.pop('Uruguay',None); wc.pop('abastecimiento',None);
    wc.pop('Ochoa',None); wc.pop('planeación',None); wc.pop('acciones',None); wc.pop('ciudades',None);
    wc.pop('fútbol',None); wc.pop('https…RT',None); wc.pop('compromiso',None); wc.pop('daños',None);
    wc.pop('región',None); wc.pop('be',None); wc.pop('delitos',None); wc.pop('empresa',None); 
    wc.pop('ilícitos',None); wc.pop('probabilidad',None); wc.pop('equipo',None); wc.pop('gobierno',None);
    wc.pop('org',None); wc.pop('2da',None); wc.pop('humedales',None); wc.pop('ley',None); wc.pop('martes',None);
    wc.pop('público',None); wc.pop('vida',None); wc.pop('medidas',None); wc.pop('mesa',None); wc.pop('sitios',None);
    wc.pop('producto',None); wc.pop('vida',None); wc.pop('trabajo',None); wc.pop('vez',None); wc.pop('viceministro',None);
    wc.pop('daño',None); wc.pop('vida',None); wc.pop('labor',None); wc.pop('aire',None); wc.pop('Ministro',None);
    wc.pop('público',None); wc.pop('planeta',None); wc.pop('atún',None); wc.pop('Acuerdo',None); wc.pop('Digital',None)
    wc.pop('total',None); wc.pop('amenaza',None); wc.pop('Granma',None); wc.pop('Cuba',None); wc.pop('mano',None);
    wc.pop('política',None); wc.pop('contrario',None); wc.pop('necesitamos',None); wc.pop('día',None); wc.pop('futuro',None);
    wc.pop('problema',None); wc.pop('Pueblo',None); wc.pop('Madrid',None); wc.pop('#Madrid',None); wc.pop('Antioquia',None);
    wc.pop('Chile',None); wc.pop('Comisión',None); wc.pop('Costa',None); wc.pop('Guaviare',None); wc.pop('Lomas',None);
    wc.pop('Pacífico',None); wc.pop('San',None); wc.pop('Vicente',None); wc.pop('acceso',None); wc.pop('ahoga',None);
    wc.pop('animales',None); wc.pop('bienestar',None); wc.pop('circulación',None); wc.pop('coches',None); wc.pop('consecuencias',None);
    wc.pop('Antioquia',None); wc.pop('creación',None); wc.pop('días',None); wc.pop('fondo',None); wc.pop('gente',None);
    wc.pop('hora',None); wc.pop('lluvias',None); wc.pop('niveles',None); wc.pop('número',None); wc.pop('países',None);
    wc.pop('prioridad',None); wc.pop('pueblo',None); wc.pop('regulación',None); wc.pop('siglo',None); wc.pop('superficie',None);
    wc.pop('temblaba',None); wc.pop('veces',None); wc.pop('vía',None); wc.pop('vuelos',None); wc.pop('noticia',None);wc.pop('co...',None);
    wc.pop('apoyo',None);wc.pop('cerros',None);wc.pop('suelos',None);wc.pop('Cerros',None); wc.pop('Acción',None);wc.pop('co..',None);
    wc.pop('China',None);wc.pop('Valle',None);wc.pop('destrucción',None);wc.pop('intervención',None); wc.pop('plan',None);
    wc.pop('Carlos',None);wc.pop('IDEAMColombia',None);wc.pop('naturaleza',None);
    
    PalabrasTema={k: sigmoid(v) for k, v in wc.items()}
    PalabrasTema=dict((k, v) for k, v in PalabrasTema.items() if v>0.8)
    #PalabrasTema = dict(sorted(wc.iteritems(), key=operator.itemgetter(1), reverse=True)[:len(wc)/30]);
    PalabrasTema['Sostenibilidad']=PalabrasTema[max(PalabrasTema, key=PalabrasTema.get)]
    PalabrasTema['Climático']=PalabrasTema[max(PalabrasTema, key=PalabrasTema.get)] 
    PalabrasTema['COP21']=PalabrasTema[max(PalabrasTema, key=PalabrasTema.get)] 
    PalabrasTema['COP13']=PalabrasTema[max(PalabrasTema, key=PalabrasTema.get)] 
    PalabrasTema['COP22']=PalabrasTema[min(PalabrasTema, key=PalabrasTema.get)] 
    PalabrasTema['extractivismo']=PalabrasTema[min(PalabrasTema, key=PalabrasTema.get)]
    PalabrasTema['Habitat3']=PalabrasTema[min(PalabrasTema, key=PalabrasTema.get)]
    return PalabrasTema
       
    
    