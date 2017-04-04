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
    wc.pop('agua',None); wc.pop('Agua',None);wc.pop('dos',None);wc.pop('Tunjuelito',None); wc.pop('gato',None);
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
    wc.pop('apoyo',None);wc.pop('cerros',None);wc.pop('suelos',None);wc.pop('Cerros',None); wc.pop('Acción',None);wc.pop('para…',None);
    wc.pop('China',None);wc.pop('Valle',None);wc.pop('destrucción',None);wc.pop('intervención',None); wc.pop('plan',None);
    wc.pop('Carlos',None);wc.pop('IDEAMColombia',None);wc.pop('naturaleza',None);wc.pop('Beijing',None);wc.pop('Bogota',None);
    wc.pop('Bolivia',None);wc.pop('Caribe',None);wc.pop('Cundinamarca',None);wc.pop('Conoce',None);wc.pop('Córdoba',None);
    wc.pop('Desarrollan',None);wc.pop('Desarrollan',None);wc.pop('EEUU',None);wc.pop('Gobierno',None);wc.pop('GrandesMedios',None);
    wc.pop('Impacto',None);wc.pop('Día',None);wc.pop('Lee',None);wc.pop('Ley',None);wc.pop('Magdalena',None);wc.pop('Magdalena',None);
    wc.pop('México',None);wc.pop('Nación',None);wc.pop('importancia',None);wc.pop('indigenas',None);wc.pop('Municipios',None);
    wc.pop('Nativos',None);wc.pop('Naturaleza',None);wc.pop('ONU',None);wc.pop('Parques',None);wc.pop('Perú',None);wc.pop('co…',None);
    wc.pop('Proyecto',None);wc.pop('Radio',None);wc.pop('Sistema',None);wc.pop('Ucrania',None);wc.pop('Uds',None);wc.pop('Vida',None);wc.pop('moratoria',None);
    wc.pop('Vivo',None);wc.pop('animal',None);wc.pop('area',None);wc.pop('arquitectura',None);wc.pop('auditiva',None);wc.pop('belleza',None);wc.pop('calor',None);
    wc.pop('carbón',None);wc.pop('cierre',None);wc.pop('ciudad',None);wc.pop('comunidades',None);wc.pop('concepto',None);wc.pop('derechos',None);wc.pop('diario',None);
    wc.pop('educación',None);wc.pop('efectos',None);wc.pop('elespectador',None);wc.pop('empresas',None);wc.pop('esfuerzo',None);wc.pop('esfuerzos',None);wc.pop('explotación',None);
    wc.pop('función',None);wc.pop('generación',None);wc.pop('hielo',None);wc.pop('hogar',None);wc.pop('huella',None);wc.pop('impacto',None);wc.pop('infopresidencia',None);
    wc.pop('meses',None);wc.pop('mar',None);wc.pop('lumínica',None);wc.pop('localidad',None);wc.pop('la…',None);wc.pop('inteligencia',None);wc.pop('indigenas',None);
    wc.pop('metro',None);wc.pop('mitad',None);wc.pop('momento',None);wc.pop('objetivo',None);wc.pop('n',None);wc.pop('oeste',None);wc.pop('oso',None);wc.pop('parte',None);  
    wc.pop('pasos',None);wc.pop('personas',None);wc.pop('petróleo',None);wc.pop('por…',None);wc.pop('potrero',None);wc.pop('producción',None);wc.pop('programa',None);
    wc.pop('proyectos',None);wc.pop('pueblos',None);wc.pop('puertas',None);wc.pop('puerto',None);wc.pop('tráfico',None);wc.pop('variedad',None);wc.pop('video',None);
    wc.pop('¿para',None);wc.pop('árboles',None);wc.pop('-->',None);wc.pop('Ciudadana',None);wc.pop('José',None);wc.pop('conservemos',None);wc.pop('divisas',None);
    wc.pop('→',None);wc.pop('¿para',None);wc.pop('mujeres',None);wc.pop('mineros',None);wc.pop('Mineros',None);wc.pop('Mundial',None);wc.pop('ind\xc3\xadgenas',None);
    wc.pop('indígenas',None);wc.pop('Fiscal\xc3\xada',None);wc.pop('Fiscalía',None);wc.pop('mineros',None);wc.pop('riesgo',None);wc.pop('AEstaHora',None);
    wc.pop('Cambio',None);wc.pop('Carrizosa',None);wc.pop('Centro',None);wc.pop('Desarrollo',None);wc.pop('División',None);wc.pop('EAFIT',None);
    wc.pop('EE',None);wc.pop('Ecuador',None);wc.pop('Educación',None);wc.pop('Energía',None);wc.pop('EstaSemana',None);wc.pop('Evaluación',None);
    wc.pop('G20',None);wc.pop('Importancia',None);wc.pop('Julio',None);wc.pop('Justicia',None);wc.pop('Madre',None);wc.pop('Mayabeque',None);
    wc.pop('Medellín',None);wc.pop('Medio',None);wc.pop('N9PiX2Cyqz',None);wc.pop('Noticias',None);wc.pop('Plan',None);wc.pop('Programa',None);
    wc.pop('Repú',None);wc.pop('Revisa',None);wc.pop('Torres',None);wc.pop('Trump',None);wc.pop('UU',None);wc.pop('Venezuela',None);
    wc.pop('afectaría',None);wc.pop('aguas',None);wc.pop('aguas',None);wc.pop('autoridades',None);wc.pop('barrio',None);wc.pop('basura',None);
    wc.pop('conciencia',None);wc.pop('congresoperu',None);wc.pop('consumo',None);wc.pop('control',None);wc.pop('cuidado',None);wc.pop('círculo',None);
    wc.pop('denuncia',None);wc.pop('diversidad',None);wc.pop('emergencia',None);wc.pop('en…',None);wc.pop('estrategias',None);wc.pop('estudios',None);
    wc.pop('forma',None);wc.pop('foro',None);wc.pop('ingresados',None);wc.pop('is',None);wc.pop('jueves',None);wc.pop('justicia',None);
    wc.pop('manera',None);wc.pop('marina',None);wc.pop('marzo',None);wc.pop('norte',None);wc.pop('opinas',None);wc.pop('p',None);
    wc.pop('forma',None);wc.pop('foro',None);wc.pop('ingresados',None);wc.pop('is',None);wc.pop('patrimonio',None);wc.pop('peces',None);
    wc.pop('prensa',None);wc.pop('productos',None);wc.pop('razón',None);wc.pop('recursos',None);wc.pop('restauración',None);wc.pop('socio',None);
    wc.pop('tasa',None);wc.pop('via',None);wc.pop('vicioso',None);wc.pop('violencia',None);wc.pop('zona',None);wc.pop('alimentación',None);
    wc.pop('conservación',None);wc.pop('estrategia',None);wc.pop('mina',None);wc.pop('violencia',None);wc.pop('zona',None);wc.pop('alimentación',None);
    wc.pop('Amazonas',None);wc.pop('Mercurio',None);wc.pop('Mocoa',None);wc.pop('Abogabir',None);wc.pop('Actualidad',None);wc.pop('Archivar',None);
    wc.pop('Argentina',None);wc.pop('Australia',None);wc.pop('Bahía',None);wc.pop('Bolívar',None);wc.pop('Bosque',None);wc.pop('C',None);
    wc.pop('Brigittelgb',None);wc.pop('CLozanoAcosta',None);wc.pop('Cajamarca',None);wc.pop('Calidad',None);wc.pop('Catorce',None);wc.pop('Cauca',None);
    wc.pop('Cerro',None);wc.pop('Cesar',None);wc.pop('Ciudad',None);wc.pop('Clara',None);wc.pop('Cloquis',None);wc.pop('Consejo',None);
    wc.pop('Consulta',None);wc.pop('Control',None);wc.pop('Cundi',None);wc.pop('DEL',None);wc.pop('Dangond',None);wc.pop('Del',None);
    wc.pop('Der',None);wc.pop('Distinción',None);wc.pop('Dominga',None);wc.pop('ELTIEMPO',None);wc.pop('EPN',None);wc.pop('Escondida',None);
    wc.pop('España',None);wc.pop('Especial',None);wc.pop('Estado',None);wc.pop('Estrategia',None);wc.pop('Europea',None);wc.pop('FicoGutierrez',None);
    wc.pop('Fotos',None);wc.pop('GIAndradeP',None);wc.pop('Dominga',None);wc.pop('ELTIEMPO',None);wc.pop('EPN',None);wc.pop('Escondida',None);
    wc.pop('Hora',None);wc.pop('Instituto',None);wc.pop('Juan',None);wc.pop('Lago',None);wc.pop('Lagos',None);wc.pop('LuisGMurillo',None);
    wc.pop('Manuel',None);wc.pop('Marcelo',None);wc.pop('Marzo',None);wc.pop('Medellin',None);wc.pop('Metálica',None);wc.pop('Mundo',None);
    wc.pop('Obama',None);wc.pop('Opinión',None);wc.pop('Orinoco',None);wc.pop('Oro',None);wc.pop('París',None);wc.pop('Putumayo',None);
    wc.pop('QUE',None);wc.pop('Quito',None);wc.pop('Regional',None);wc.pop('Revista',None);wc.pop('Rica',None);wc.pop('Rodriguez',None);
    wc.pop('Río',None);wc.pop('Salud',None);wc.pop('Salvador',None);wc.pop('Stories',None);wc.pop('Silvestre',None);wc.pop('Sumapaz',None);
    wc.pop('TSJ',None);wc.pop('Thomas',None);wc.pop('Tolima',None);wc.pop('Torca',None);wc.pop('UE',None);wc.pop('VIDEO',None);
    wc.pop('X',None);wc.pop('Verde',None);wc.pop('Ximena',None);wc.pop('YouTube',None);wc.pop('Zar',None);wc.pop('abril',None);
    wc.pop('acción',None);wc.pop('actividad',None);wc.pop('actividades',None);wc.pop('activistas',None);wc.pop('adaptarse',None);wc.pop('agenda',None);
    wc.pop('agricultura',None);wc.pop('alimentos',None);wc.pop('alternativa',None);wc.pop('amazonas',None);wc.pop('amp',None);wc.pop('apagón',None);
    wc.pop('aportes',None);wc.pop('aumento',None);wc.pop('autor',None);wc.pop('avance',None);wc.pop('aves',None);wc.pop('bienes',None);
    wc.pop('bogotanos',None);wc.pop('calidad',None);wc.pop('calle',None);wc.pop('campaña',None);wc.pop('campo',None);wc.pop('cantaran',None);
    wc.pop('caos',None);wc.pop('capacidad',None);wc.pop('casa',None);wc.pop('caso',None);wc.pop('caza',None);wc.pop('celebración',None);
    wc.pop('centro',None);wc.pop('chinos',None);wc.pop('cielo',None);wc.pop('ciudadanos',None);wc.pop('clave',None);wc.pop('concienciar',None);
    wc.pop('construcción',None);wc.pop('contenedor',None);wc.pop('convertirse',None);wc.pop('cosa',None);wc.pop('cosas',None);wc.pop('cultura',None);
    wc.pop('decisiones',None);wc.pop('defensor',None);wc.pop('delito',None);wc.pop('democracia',None);wc.pop('departamento',None);wc.pop('desarrollo',None);
    wc.pop('desastre',None);wc.pop('de…',None);wc.pop('dignidad',None);wc.pop('dinero',None);wc.pop('diputados',None);wc.pop('diálogo',None);
    wc.pop('d…',None);wc.pop('efecto',None);wc.pop('el…',None);wc.pop('energía',None);wc.pop('escala',None);wc.pop('estrellas',None);
    wc.pop('estudiantes',None);wc.pop('estudio',None);wc.pop('es…',None);wc.pop('evento',None);wc.pop('experiencia',None);wc.pop('expertos',None);
    wc.pop('e…',None);wc.pop('falta',None);wc.pop('fecha',None);wc.pop('fiebre',None);wc.pop('fin',None);wc.pop('focos',None);
    wc.pop('fondos',None);wc.pop('frontera',None);wc.pop('fuente',None);wc.pop('fuentes',None);wc.pop('fuerza',None);wc.pop('ganadería',None);
    wc.pop('gestión',None);wc.pop('golpe',None);wc.pop('grandesMedios',None);wc.pop('grupo',None);wc.pop('herencia',None);wc.pop('historia',None);
    wc.pop('historia"',None);wc.pop('hombre',None);wc.pop('huelga',None);wc.pop('incendio',None);wc.pop('industria',None);wc.pop('información',None);
    wc.pop('iniciativa',None);wc.pop('investigación',None);wc.pop('invitamos',None);wc.pop('jirafa',None);wc.pop('jornada',None);wc.pop('jóvenes',None);
    wc.pop('lista',None);wc.pop('litigio',None);wc.pop('lluvia',None);wc.pop('lugar',None);wc.pop('luz',None);wc.pop('límites',None);
    wc.pop('mercurio',None);wc.pop('modelo',None);wc.pop('materia',None);wc.pop('materiales',None);wc.pop('mañana',None);wc.pop('mentira',None);
    wc.pop('motor',None);wc.pop('muerte',None);wc.pop('muertes',None);wc.pop('mujer',None);wc.pop('narcotráfico',None);wc.pop('negocio',None);
    wc.pop('nivel',None);wc.pop('noche',None);wc.pop('normativa',None);wc.pop('obras',None);wc.pop('operaciones',None);wc.pop('orden',None);
    wc.pop('organizaciones',None);wc.pop('out',None);wc.pop('pajaros',None);wc.pop('pantalla',None);wc.pop('papel',None);wc.pop('parque',None);
    wc.pop('partido',None);wc.pop('pasado',None);wc.pop('pase',None);wc.pop('peligro',None);wc.pop('pico',None);wc.pop('placa',None);
    wc.pop('planificación',None);wc.pop('planta',None);wc.pop('plantas',None);wc.pop('plomo',None);wc.pop('plástico',None);wc.pop('pobres',None);
    wc.pop('pobreza',None);wc.pop('poder',None);wc.pop('premio',None);wc.pop('presentación',None);wc.pop('prevención',None);wc.pop('principio',None);
    wc.pop('proceso',None);wc.pop('procesos',None);wc.pop('profesor',None);wc.pop('prohibición',None);wc.pop('prohibir',None);wc.pop('propuesta',None);
    wc.pop('puerta',None);wc.pop('pérdida',None);wc.pop('realidad',None);wc.pop('recolección',None);wc.pop('recuperación',None);wc.pop('reflexion',None);
    wc.pop('reforma',None);wc.pop('regiones',None);wc.pop('relación',None);wc.pop('renuncia',None);wc.pop('responsabilidad',None);wc.pop('respuesta',None);
    wc.pop('resultados',None);wc.pop('reunión',None);wc.pop('riesgos',None);wc.pop('rodb',None);wc.pop('rumbo',None);wc.pop('sector',None);
    wc.pop('seguridad',None);wc.pop('sembrar',None);wc.pop('servicio',None);wc.pop('servicios',None);wc.pop('silenciosos',None);wc.pop('situación',None);
    wc.pop('submundo',None);wc.pop('suma',None);wc.pop('televisión',None);wc.pop('tema',None);wc.pop('territorio',None);wc.pop('tiempo',None);
    wc.pop('tierra',None);wc.pop('tierras',None);wc.pop('tituladas',None);wc.pop('titular',None);wc.pop('trabajos',None);wc.pop('tragedia',None);
    wc.pop('tragedias',None);wc.pop('trágica',None);wc.pop('uso',None);wc.pop('valor',None);wc.pop('verdad',None);wc.pop('virus',None);
    wc.pop('visita',None);wc.pop('vivo…',None);wc.pop('vulnerabilidad',None);wc.pop('wilcheschaux',None);wc.pop('y…',None);wc.pop('¿Cómo',None);
    wc.pop('árbol',None);wc.pop('Edomex',None);wc.pop('Rodríguez',None);wc.pop('Sur',None);wc.pop('cine',None);wc.pop('cuerpo',None);
    wc.pop('CDMX',None);wc.pop('impactos',None);wc.pop('manejo',None);wc.pop('marcelomena',None);wc.pop('humanidad’',None);wc.pop('“agencia',None);
    wc.pop('‘patrimonio',None);wc.pop('historia”',None);wc.pop('–',None);wc.pop('marcelomena',None);wc.pop('humanidad’',None);wc.pop('cancerígeno',None);
    wc.pop('EnriqueViale',None);wc.pop('LuisGMurillo',None);wc.pop('–',None);wc.pop('marcelomena',None);wc.pop('humanidad’',None);wc.pop('cancerígeno',None);
    
    
    PalabrasTema={k: sigmoid(v) for k, v in wc.items()}
    PalabrasTema=dict((k, v) for k, v in PalabrasTema.items() if v>0.97)
    #PalabrasTema = dict(sorted(wc.iteritems(), key=operator.itemgetter(1), reverse=True)[:len(wc)/30]);
    PalabrasTema['Sostenibilidad']=PalabrasTema[max(PalabrasTema, key=PalabrasTema.get)]
    PalabrasTema['Climático']=PalabrasTema[max(PalabrasTema, key=PalabrasTema.get)] 
    PalabrasTema['COP21']=PalabrasTema[max(PalabrasTema, key=PalabrasTema.get)] 
    PalabrasTema['COP13']=PalabrasTema[max(PalabrasTema, key=PalabrasTema.get)] 
    PalabrasTema['COP22']=PalabrasTema[min(PalabrasTema, key=PalabrasTema.get)] 
    PalabrasTema['extractivismo']=PalabrasTema[min(PalabrasTema, key=PalabrasTema.get)]
    PalabrasTema['Habitat3']=PalabrasTema[min(PalabrasTema, key=PalabrasTema.get)]
    PalabrasTema['ecología']=PalabrasTema[min(PalabrasTema, key=PalabrasTema.get)]
    PalabrasTema['#CambioClimatico']=PalabrasTema[min(PalabrasTema, key=PalabrasTema.get)]
    PalabrasTema['ecoturismo']=PalabrasTema[min(PalabrasTema, key=PalabrasTema.get)]
    PalabrasTema['Biológica']=PalabrasTema[min(PalabrasTema, key=PalabrasTema.get)]
    PalabrasTema['Machalilla']=PalabrasTema[min(PalabrasTema, key=PalabrasTema.get)]
    PalabrasTema['Limoncocha']=PalabrasTema[min(PalabrasTema, key=PalabrasTema.get)]
    PalabrasTema['#REDD+']=PalabrasTema[min(PalabrasTema, key=PalabrasTema.get)]
    PalabrasTema['POT']=PalabrasTema[min(PalabrasTema, key=PalabrasTema.get)]
    PalabrasTema['POMCA']=PalabrasTema[min(PalabrasTema, key=PalabrasTema.get)]
    
    
    return PalabrasTema
       
    
    